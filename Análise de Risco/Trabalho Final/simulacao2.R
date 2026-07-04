# -------------------------------------------------------------------------
# Simulador de Fluxo Institucional: Cadeia Aberta (Simulação 2)
# -------------------------------------------------------------------------

library(jsonlite)

# 1. Configurações
set.seed(123)
N_simulacoes <- 3000
t_max_fluxo <- 10
N_ingressantes_anual <- 120
urnas_macro <- fromJSON("matrizes/urnas_bootstrap.json")$simulacao_2_fluxo

# Estado inicial observado no último censo disponível
censo_2024 <- read.csv("dados/UFRJ_CENSO_2024.csv", fileEncoding = "UTF-8-BOM")
linha_censo <- subset(censo_2024, CO_CURSO == 85783 & NU_ANO_CENSO == 2024)
A0 <- as.integer(linha_censo$QT_MAT[1])
F0 <- as.integer(linha_censo$QT_CONC[1])

# A evasão da trajetória é um evento acumulado, não um estoque em t0.
# Mantemos o estado inicial absorvente em zero e usamos a trajetória apenas
# como referência analítica para a calibração das taxas.
trajetoria_2024 <- read.csv("dados/INDICADORES_TRAJETORIA_PROCESSADO.csv", fileEncoding = "UTF-8-BOM")
linha_trajetoria <- subset(trajetoria_2024, CO_CURSO == 85783 & NU_ANO_REFERENCIA == 2024)
E0 <- 0

# Histórico: [Simulação, Ano, Estados]
historico_fluxo <- array(0, dim = c(N_simulacoes, t_max_fluxo, 3))
dimnames(historico_fluxo)[[3]] <- c("Ativo", "Evadido", "Formado")

# 2. Simulação
for (s in 1:N_simulacoes) {
  ativos <- A0
  evadidos_ano <- E0
  formados_ano <- F0
  
  for (t in 1:t_max_fluxo) {
    ativos <- ativos + N_ingressantes_anual
    
    # Sorteio bootstrap das taxas macro
    pE <- sample(urnas_macro$evasao_macro_pE, 1)
    pF <- sample(urnas_macro$formatura_macro_pF, 1)
    pA <- 1 - (pE + pF)
    if (pA < 0) {
      soma <- pE + pF
      pE <- pE / soma
      pF <- pF / soma
      pA <- 0
    }
    
    # Fluxo anual categórico: uma única transição por aluno ativo
    transicoes <- rmultinom(1, size = ativos, prob = c(pA, pE, pF))
    ativos_final <- as.integer(transicoes[1, 1])
    evadidos_ano <- as.integer(transicoes[2, 1])
    formados_ano <- as.integer(transicoes[3, 1])
    
    ativos <- ativos_final

    historico_fluxo[s, t, ] <- c(ativos, evadidos_ano, formados_ano)
  }
}

# 3. Análise de Resultados
final <- historico_fluxo[, t_max_fluxo, ]

base_ano_final <- final[, "Ativo"] + final[, "Evadido"] + final[, "Formado"]
taxas_finais <- sweep(final, 1, base_ano_final, FUN = "/")

medianas <- apply(final, 2, median)
medianas_taxas <- apply(taxas_finais, 2, median)

ic_taxas <- apply(taxas_finais, 2, quantile, probs = c(0.025, 0.975))
ic_contagens <- apply(final, 2, quantile, probs = c(0.025, 0.975))

cat("\n--- Projeção de Fluxo: 2024 vs 2034 ---\n")
cat(sprintf("Estado inicial do censo 2024: Ativo=%d | Evadido=%d | Formado=%d\n", A0, E0, F0))
cat(sprintf("Trajetória 2024 observada: Desistências=%d | Permanências=%d | Concluintes=%d\n",
            sum(linha_trajetoria$QT_DESISTENCIA, na.rm = TRUE),
            sum(linha_trajetoria$QT_PERMANENCIA, na.rm = TRUE),
            sum(linha_trajetoria$QT_CONCLUINTE, na.rm = TRUE)))
cat(sprintf("Mediana de Ativos em 2034: %.0f\n", medianas["Ativo"]))
cat(sprintf("Mediana de Evasão em 2034: %.0f\n", medianas["Evadido"]))
cat(sprintf("Mediana de Formação em 2034: %.0f\n", medianas["Formado"]))
cat(sprintf("Mediana da taxa de Evasão 2034:   %.2f%%\n", medianas_taxas["Evadido"]*100))
cat(sprintf("Mediana da taxa de Formação 2034: %.2f%%\n", medianas_taxas["Formado"]*100))
cat(sprintf("Mediana da taxa de Retenção 2034:  %.2f%%\n", medianas_taxas["Ativo"]*100))

cat("\nIC95% das taxas em 2034:\n")
cat(sprintf("Retenção: [%.2f%%, %.2f%%]\n", ic_taxas[1, "Ativo"]*100, ic_taxas[2, "Ativo"]*100))
cat(sprintf("Evasão:   [%.2f%%, %.2f%%]\n", ic_taxas[1, "Evadido"]*100, ic_taxas[2, "Evadido"]*100))
cat(sprintf("Formação: [%.2f%%, %.2f%%]\n", ic_taxas[1, "Formado"]*100, ic_taxas[2, "Formado"]*100))

cat("\nIC95% das contagens finais em 2034:\n")
cat(sprintf("Ativos:   [%.0f, %.0f]\n", ic_contagens[1, "Ativo"], ic_contagens[2, "Ativo"]))
cat(sprintf("Evadidos: [%.0f, %.0f]\n", ic_contagens[1, "Evadido"], ic_contagens[2, "Evadido"]))
cat(sprintf("Formados: [%.0f, %.0f]\n", ic_contagens[1, "Formado"], ic_contagens[2, "Formado"]))

# --- Visualizações de validação ---
medianas_fluxo <- apply(historico_fluxo, c(2,3), median)

par(mfrow = c(2, 2))

plot(1:t_max_fluxo, medianas_fluxo[, "Ativo"], type = "l", col = "blue", lwd = 3,
  ylim = c(0, max(medianas_fluxo) * 1.1),
  main = "Evolução mediana anual",
     xlab = "Ano", ylab = "Quantidade de alunos")
lines(1:t_max_fluxo, medianas_fluxo[, "Evadido"], col = "red", lwd = 3)
lines(1:t_max_fluxo, medianas_fluxo[, "Formado"], col = "green", lwd = 3)
legend("topleft", legend = c("Ativo", "Evadido no ano", "Formado no ano"), 
       col = c("blue", "red", "green"), lwd = 3, bty = "n")

boxplot(historico_fluxo[, t_max_fluxo, ], col = c("blue", "red", "green"),
        main = "Distribuição final após 10 anos", ylab = "Quantidade de alunos")

plot(ecdf(taxas_finais[, "Formado"]), main = "ECDF da taxa anual de formados em 2034",
  xlab = "Taxa de formados no ano", ylab = "Probabilidade acumulada")
abline(h = 0.9, col = "red", lty = 2)

hist(historico_fluxo[, t_max_fluxo, "Evadido"], breaks = 20, col = "salmon", border = "white",
  main = "Distribuição da evasão anual em 2034", xlab = "Evasão no ano")

par(mfrow = c(1, 1))
