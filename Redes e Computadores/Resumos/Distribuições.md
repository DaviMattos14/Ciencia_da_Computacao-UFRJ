### Dicionário de variáveis

| Símbolo         | Significado                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| $m$             | Número total de usuários (ou tentativas/ensaios)                                                             |
| $p$             | Probabilidade de um único usuário estar ativo (ou de sucesso em uma tentativa)                               |
| $a$             | Número específico de sucessos que estamos calculando a probabilidade (ex: "exatamente $a$ usuários ativos")  |
| $Z_i$           | Variável de Bernoulli do usuário $i$ (1 = ativo, 0 = inativo)                                                |
| $A$             | Variável Binomial — número total de usuários ativos simultaneamente                                          |
| $\lambda$       | Parâmetro (taxa média) da Poisson — número médio esperado de ocorrências no intervalo observado              |
| $\tilde\lambda$ | Taxa de ocorrências por unidade de tempo (ex: pacotes/segundo)                                               |
| $T$             | Duração do intervalo de tempo observado                                                                      |
| $W$             | Variável de Poisson — número de ocorrências no intervalo $T$                                                 |
| $q$             | Probabilidade de "sucesso" em uma única tentativa/slot (ex: probabilidade de um slot estar descongestionado) |
| $S$             | Variável Geométrica — número de tentativas (slots) até o primeiro sucesso                                    |

---

### 1) Bernoulli — $Z \sim \text{Ber}(p)$

$$Z = \begin{cases} 1, & \text{prob. } p \ 0, & \text{prob. } 1-p \end{cases}$$

**Interpretação textual:** modela um **único experimento** com dois resultados possíveis (sucesso/fracasso, ativo/inativo). É o "tijolo" mais básico — todas as outras três distribuições desta lista são construídas a partir de Bernoullis.

---

### 2) Binomial — $A = \sum_{i=1}^{m} Z_i \sim \text{Binomial}(m, p)$

$$\Pr(A=a) = \binom{m}{a}p^a(1-p)^{m-a}, \quad a \in {0, 1, ..., m}$$

**Interpretação textual:** responde "**quantos sucessos** ocorrem em **$m$ tentativas independentes**?" — é a soma de $m$ variáveis de Bernoulli. No contexto de rede: quantos, dos $m$ usuários, estão ativos ao mesmo tempo.

**Interpretação da fórmula:** $\binom{m}{a}$ conta **de quantas formas diferentes** é possível escolher **quais** $a$ usuários (entre os $m$) estão ativos; $p^a(1-p)^{m-a}$ é a probabilidade de **uma** dessas combinações específicas ocorrer (a sucessos, m−a fracassos). Multiplicamos porque somamos a probabilidade de todas as combinações equivalentes possíveis.

**Suporte:** finito, $a \in {0, 1, ..., m}$ (não dá pra ter mais sucessos que tentativas).

---

### 3) Poisson — $W \sim \text{Poi}(\lambda)$

$$\Pr(W=w) = e^{-\lambda}\frac{\lambda^w}{w!}, \quad w \in {0, 1, 2, ...}$$

**Interpretação textual:** responde "**quantas ocorrências** acontecem em um **intervalo de tempo $T$**?" — é o que a Binomial se torna quando $m \to \infty$, $p \to 0$, mantendo $\lambda = mp$ fixo (muitas "chances" de ocorrência, cada uma rara individualmente). O parâmetro $\lambda = \tilde\lambda \cdot T$ é sempre um **número médio de ocorrências**, não uma probabilidade.

**Interpretação da fórmula:** $\frac{\lambda^w}{w!}$ pesa a chance relativa de observar exatamente $w$ ocorrências; $e^{-\lambda}$ é o fator de normalização que garante que a soma de todas as probabilidades seja 1.

**Suporte:** infinito, $w \in {0, 1, 2, ...}$ (sem teto — diferente da Binomial, já que "m" desapareceu no limite).

---

### 4) Geométrica — $S \sim \text{Geom}(q)$

$$\Pr(S=s) = (1-q)^{s-1} \cdot q, \quad s \in {1, 2, 3, ...}$$

**Interpretação textual:** responde "**quantas tentativas** são necessárias até o **primeiro sucesso**?" — sem intervalo de tempo fixo, o "relógio" corre até o sucesso acontecer. No contexto do professor: quantos slots futuros até o sistema voltar a estar **descongestionado**.

**Interpretação da fórmula:** $(1-q)^{s-1}$ é a probabilidade das primeiras $s-1$ tentativas **falharem** todas; $q$ é a probabilidade da $s$-ésima tentativa (a última) **ter sucesso**. Multiplicamos porque as tentativas são independentes.

**Suporte:** infinito, começando em $s=1$ (nunca $s=0$ — por definição, é preciso pelo menos uma tentativa para haver um "primeiro sucesso").

---

### Quadro comparativo — qual pergunta cada uma responde

| Distribuição   | Pergunta que responde                            | Suporte                     |
| -------------- | ------------------------------------------------ | --------------------------- |
| **Bernoulli**  | Sucesso ou fracasso em **1** tentativa?          | ${0, 1}$                    |
| **Binomial**   | **Quantos** sucessos em **$m$** tentativas?      | ${0, ..., m}$ (finito)      |
| **Poisson**    | **Quantas** ocorrências em um **intervalo $T$**? | ${0, 1, 2, ...}$ (infinito) |
| **Geométrica** | **Quantas tentativas** até o **1º sucesso**?     | ${1, 2, 3, ...}$ (infinito) |
