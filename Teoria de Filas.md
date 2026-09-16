## Parte 0 — Notação de Kendall (o significado de "M/M/1")

Antes de tudo, vale explicar essa notação, já que você mencionou lembrar vagamente dela. A **notação de Kendall** descreve uma fila com três (ou mais) símbolos separados por barras: **A/B/c**, onde:

- **A** = distribuição dos **tempos entre chegadas** (processo de chegada)
- **B** = distribuição dos **tempos de serviço**
- **c** = **número de servidores**

Os símbolos mais comuns para A e B:

| Símbolo | Significado                                                                              |
| ------- | ---------------------------------------------------------------------------------------- |
| **M**   | _Markoviano_ — tempos exponenciais (chegadas: processo de Poisson; serviço: exponencial) |
| **D**   | _Determinístico_ — tempo fixo, sempre o mesmo valor                                      |
| **G**   | _Geral_ (General) — qualquer distribuição, sem hipótese específica                       |

Então:

- **M/M/1** = chegadas Poisson, serviço exponencial, 1 servidor
- **M/D/1** = chegadas Poisson, serviço determinístico (tempo fixo), 1 servidor
- **D/D/1** = chegadas determinísticas, serviço determinístico, 1 servidor (caso "perfeitamente previsível" — vimos que pode ter I=1 sem instabilidade)
- **M/G/1** = chegadas Poisson, serviço com distribuição genérica qualquer, 1 servidor (caso mais geral — a fórmula de Pollaczek-Khinchine, que faz o $S_R$ aparecer com $E[S^2]$, é para esse caso)

---

## Glossário completo de variáveis

| Símbolo         | Nome                                     | Significado                                                                                                               |
| --------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| $L$             | Tamanho do pacote                        | Em bits                                                                                                                   |
| $R$             | Taxa do enlace                           | Em bits/segundo                                                                                                           |
| $\lambda$       | Taxa de chegada                          | Pacotes/segundo — quantos pacotes chegam, em média, por segundo                                                           |
| $\mu$           | Taxa de serviço                          | Pacotes/segundo — quantos pacotes o servidor consegue atender por segundo, $\mu = R/L$                                    |
| $S$             | Tempo de serviço                         | Segundos — tempo médio para transmitir um pacote, $S = 1/\mu = L/R$                                                       |
| $S_R$           | Tempo residual de serviço                | Segundos — tempo **restante** (não o total) do pacote que já está sendo atendido, no instante em que um novo pacote chega |
| $I$ (ou $\rho$) | Intensidade de tráfego / utilização      | Adimensional, $I = \lambda/\mu = \lambda L/R$; também é a fração de tempo em que o servidor fica ocupado                  |
| $N_q(t)$        | Pacotes na fila de espera                | Não conta o pacote em transmissão, só quem está esperando                                                                 |
| $N_s(t)$        | Pacotes no servidor                      | Só pode ser 0 (livre) ou 1 (ocupado)                                                                                      |
| $N(t)$          | Pacotes no sistema                       | $N(t) = N_q(t) + N_s(t)$ — fila + servidor juntos                                                                         |
| $N_q, N_s, N$   | Versões médias (no tempo) das três acima | Podem ser fracionárias (ex: $N_s=0{,}8$ = servidor ocupado 80% do tempo)                                                  |
| $W$             | Tempo médio de espera na fila            | Não inclui o tempo de serviço                                                                                             |
| $T$             | Tempo médio total no sistema             | $T = W + S$                                                                                                               |
| $U$             | Utilização do servidor                   | Fração de tempo ocupado — numericamente igual a $I$                                                                       |
| $\pi_0$         | Probabilidade do sistema estar vazio     | $\pi_0 = 1 - I$                                                                                                           |

**Nota sobre notação alternativa (conectando com Harchol-Balter):** no livro dela, é comum ver $\lambda$ para chegada (igual aqui) e $\mu$ para serviço (igual aqui) — essa parte costuma bater. As diferenças mais comuns entre autores aparecem em: tempo de espera na fila (alguns usam $W_q$, outros $W$; aqui o professor usa $W$ para fila e $T$ para sistema total — confira sempre se o "W" do seu outro livro é fila ou sistema completo), e no número médio (alguns usam $L$ ou $L_q$ para número de clientes — cuidado, porque aqui $L$ já está sendo usado para **tamanho do pacote**! Isso é uma fonte clássica de confusão entre livros de redes e livros de teoria de filas genérica).

---

## Parte A — As quatro distribuições

|Distribuição|Pergunta que responde|PMF|Suporte|
|---|---|---|---|
|**Bernoulli** $Z\sim\text{Ber}(p)$|Sucesso/fracasso em 1 tentativa?|$\Pr(Z=1)=p$|${0,1}$|
|**Binomial** $X\sim\text{Bin}(m,p)$|Quantos sucessos em $m$ tentativas?|$\binom{m}{a}p^a(1-p)^{m-a}$|${0,...,m}$|
|**Poisson** $W\sim\text{Poi}(\lambda)$|Quantas ocorrências num intervalo $T$?|$e^{-\lambda}\lambda^w/w!$|${0,1,2,...}$|
|**Geométrica** $S\sim\text{Geo}(q)$|Quantas tentativas até o 1º sucesso?|$(1-q)^{s-1}q$|${1,2,3,...}$|

**Relações:** Binomial = soma de $m$ Bernoullis independentes | Geométrica = posição do primeiro sucesso entre Bernoullis | Poisson = limite da Binomial quando $m\to\infty$, $p\to0$, com $mp=\lambda$ fixo | Gaussiana = limite da Binomial quando $m\to\infty$ (Teorema Central do Limite)

---

## Parte B — Teoria de filas

### Relações gerais (valem para QUALQUER fila, sem hipótese de distribuição)

$$N = N_q + N_s \qquad T = W + S$$

**Lei de Little** (aplicada a cada "compartimento" separadamente):

$$N_q = \lambda W \qquad N_s = \lambda S \qquad N = \lambda T$$

**Interpretação textual:** "número médio presente = taxa de chegada × tempo médio passado ali". É uma **relação de conservação** — não calcula W ou T sozinha, só garante consistência entre as três grandezas. Precisa de hipóteses extras (tipo M/M/1) para virar fórmula fechada.

**Intensidade de tráfego:**

$$I = \frac{\lambda}{\mu} = \frac{\lambda L}{R}$$

**Interpretação:** fração da capacidade do enlace sendo demandada, em média. Também é numericamente igual a $N_s$ (número médio no servidor) e a $U$ (utilização).

**Condição de estabilidade:** $I < 1$ (necessário quando há aleatoriedade — exceção: D/D/1 pode ter $I=1$ estável, pois não há variabilidade nenhuma pra causar fila).

### Tempo residual de serviço (fórmula geral, qualquer distribuição)

$$S_R = \frac{E[S^2]}{2E[S]}$$

**Interpretação:** tempo restante esperado do pacote **já em atendimento**, no instante em que um novo pacote chega. Depende do **segundo momento** de S (não só da média) — quanto mais variável o tempo de serviço, maior o tempo residual esperado.

$$W = N_q \cdot S + N_s \cdot S_R$$

**Interpretação:** o pacote que chega espera pelos $N_q$ pacotes já na fila (cada um leva o tempo de serviço **completo** $S$) mais o tempo **residual** do pacote já em transmissão.

### Caso M/M/1 (serviço exponencial)

Pela falta de memória: $S_R = S = 1/\mu$

$$W = \frac{I}{\mu-\lambda} = \frac{IS}{1-I} \qquad T = \frac{1}{\mu-\lambda} \qquad N = \frac{I}{1-I} \qquad N_q = \frac{I^2}{1-I}$$

### Caso M/D/1 (serviço determinístico)

Pelo paradoxo da inspeção: $S_R = S/2$

$$W_{M/D/1} = \frac{IS}{2(1-I)} = \frac{1}{2}W_{M/M/1}$$

**Interpretação central de toda a Aula 8:** dois sistemas podem ter a **mesma** intensidade de tráfego $I$ e ainda assim ter atrasos médios **diferentes** — o que muda é a **variabilidade** do tempo de serviço (capturada pelo segundo momento $E[S^2]$), não só a média.
