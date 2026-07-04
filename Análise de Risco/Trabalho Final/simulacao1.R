# -------------------------------------------------------------------------
# Simulador de Coorte: Cadeia de Markov Não-Homogénea (Simulação 1)
# -------------------------------------------------------------------------

# Carregar bibliotecas
if (!require("jsonlite")) install.packages("jsonlite")
library(matrixStats)
library(jsonlite)

# 1. Configurações da Simulação
N_simulacoes <- 3000
N_alunos_inicial <- 60
t_max <- 10
estados <- c("Ativo", "Evadido", "Formado")

# 2. Carregar dados das urnas
# Certifique-se que o ficheiro está na pasta 'matrizes/'
urnas <- fromJSON("matrizes/urnas_bootstrap.json")$simulacao_1_coorte

# Matriz para armazenar o resultado final de cada simulação (estado no Ano 10)
resultados <- matrix(0, nrow = N_simulacoes, ncol = 3)
colnames(resultados) <- estados

# Guardar a trajetória anual para validar a dinâmica da coorte
historico <- array(0, dim = c(N_simulacoes, t_max, 3))
dimnames(historico)[[3]] <- estados

# 3. Motor de Monte Carlo
set.seed(123) 

for (s in 1:N_simulacoes) {
  
  # Estado inicial da coorte
  status_alunos <- rep("Ativo", N_alunos_inicial)
  
  for (t in 1:t_max) {
    
    # LÓGICA DINÂMICA (Não-Homogénea):
    # O comportamento muda dependendo do ano (t) que o aluno está no curso
    
    if (t < 4) {
      # FASE DE CICLO BÁSICO: Taxas iniciais
      pE_atual <- sample(urnas$evasao_inicial_pE_A, 1)
      pF_atual <- 0 # Trava curricular: formatura proibida
    } else {
      # FASE DE CICLO FINAL: Taxas tardias
      pE_atual <- sample(urnas$evasao_tardia_pE_R, 1)
      pF_atual <- sample(urnas$formatura_tardia_pF_R, 1)
    }
    
    # Garantia de integridade: pA é o complemento para fechar 1.0
    # O pA representa a probabilidade de o aluno continuar no estado "Ativo"
    pA_atual <- 1 - (pE_atual + pF_atual)
    if (pA_atual < 0) {
      soma <- pE_atual + pF_atual
      pE_atual <- pE_atual / soma
      pF_atual <- pF_atual / soma
      pA_atual <- 0
    }
    
    # Aplicação da Roleta Individual
    for (i in 1:N_alunos_inicial) {
      if (status_alunos[i] == "Ativo") {
        # Sorteio do próximo estado
        proximo <- sample(estados, size = 1, 
                          prob = c(pA_atual, pE_atual, pF_atual))
        status_alunos[i] <- proximo
      }
    }

    historico[s, t, "Ativo"]   <- sum(status_alunos == "Ativo")
    historico[s, t, "Evadido"] <- sum(status_alunos == "Evadido")
    historico[s, t, "Formado"] <- sum(status_alunos == "Formado")
  }
  
  # Registrar o "saldo" final desta fotografia (simulação)
  resultados[s, "Ativo"]   <- sum(status_alunos == "Ativo")
  resultados[s, "Evadido"] <- sum(status_alunos == "Evadido")
  resultados[s, "Formado"] <- sum(status_alunos == "Formado")
}

# 4. Análise e Resumo
cat("--- Simulação 1: Coorte de Computação UFRJ ---\n")
cat("Mediana de alunos após 10 anos:\n")
print(colMedians(resultados))

cat("\nIntervalos de Confiança 95% (2.5% - 97.5%):\n")
print(apply(resultados, 2, quantile, probs = c(0.025, 0.975)))

totais_finais <- rowSums(resultados)
proporcoes_finais <- sweep(resultados, 1, totais_finais, FUN = "/")
cat("\nProporções médias ao final de 10 anos:\n")
print(colMeans(proporcoes_finais))

# Sugestão: Salvar resultados para plotar no relatório
# write.csv(resultados, "resultados_simulacao1.csv")

# Plotar o Histograma de Formados
hist(resultados[, "Formado"], main="Distribuição de Formados (10 anos)", 
     xlab="Nº de Alunos", col="lightblue", border="white")
abline(v = quantile(resultados[, "Formado"], 0.9), col="red", lwd=2, lty=2)

# Plotar a ECDF de Formados
plot(ecdf(resultados[, "Formado"]), main="ECDF: Probabilidade Acumulada", 
     xlab="Nº de Alunos", ylab="Probabilidade")
abline(h = 0.9, col="red", lty=2)

# 5. Visualização e Análise de Validade
cores <- c("Ativo" = "blue", "Evadido" = "red", "Formado" = "green")
mat_media <- apply(historico, c(2, 3), mean)
mat_inf <- apply(historico, c(2, 3), quantile, probs = 0.1)
mat_sup <- apply(historico, c(2, 3), quantile, probs = 0.9)

par(mfrow = c(2, 2))

plot(1:t_max, mat_media[, "Ativo"], type = "n", ylim = c(0, N_alunos_inicial),
     xlab = "Ano", ylab = "Quantidade de alunos", main = "Coorte média e faixa 10%-90%")
for (est in estados) {
  polygon(c(1:t_max, rev(1:t_max)), c(mat_inf[, est], rev(mat_sup[, est])),
          col = adjustcolor(cores[est], alpha.f = 0.15), border = NA)
  lines(1:t_max, mat_media[, est], col = cores[est], lwd = 3)
}
abline(v = 3.5, col = "gray40", lty = 2)
legend("right", legend = c("Ativo", "Evadido", "Formado", "Virada curricular"),
       col = c("blue", "red", "green", "gray40"), lwd = c(3, 3, 3, 1), lty = c(1, 1, 1, 2), bty = "n")

hist(resultados[, "Formado"], breaks = 20, col = "lightblue", border = "white",
     main = "Distribuição final de formados", xlab = "Nº de formados em 10 anos")
abline(v = mean(resultados[, "Formado"]), col = "darkblue", lwd = 2)
abline(v = quantile(resultados[, "Formado"], 0.9), col = "red", lwd = 2, lty = 2)

plot(ecdf(proporcoes_finais[, "Formado"]), main = "ECDF da proporção final de formados",
     xlab = "Proporção de formados", ylab = "Probabilidade acumulada")
abline(h = 0.9, col = "red", lty = 2)

boxplot(resultados, col = c("blue", "red", "green"),
        main = "Composição final da coorte", ylab = "Quantidade de alunos")

par(mfrow = c(1, 1))

limites_inf <- apply(resultados, 2, quantile, probs = 0.05)
limites_sup <- apply(resultados, 2, quantile, probs = 0.95)

cat("--- Frase para o Relatório: Nível de Confiança de 90% ---\n")
cat(sprintf(
  "Com 90%% de confiança, após 10 anos, a distribuição da coorte estará dentro do intervalo:\nAtivo: [%d a %d] | Evadidos: [%d a %d] | Formados: [%d a %d]\n",
  limites_inf["Ativo"], limites_sup["Ativo"],
  limites_inf["Evadido"], limites_sup["Evadido"],
  limites_inf["Formado"], limites_sup["Formado"]
))