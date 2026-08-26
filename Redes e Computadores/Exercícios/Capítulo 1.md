> **Nome**: Davi dos Santos Mattos            **DRE**: 119133049

1) P2 -- explique porque o uso de store-and-forward implica que o atraso de transmissão aumente em função do número de links envolvidos no caminho origem-destino, enquanto que cut-through não

Equação 1.1 (um único pacote, N enlaces, todos com taxa R):

$$d_{fim-a-fim} = N \cdot \frac{L}{R}$$

Agora, para P pacotes enviados consecutivamente (back-to-back), assim que o host de origem termina de transmitir o pacote 1 (o que leva L/R segundos), ele já começa a transmitir o pacote 2 imediatamente, e assim por diante, sem esperar o pacote 1 chegar ao destino.

O "gargalo" desse é: o último pacote (o P-ésimo) só pode começar a ser transmitido pela origem depois que os P−1 pacotes anteriores já tiverem sido totalmente transmitidos. Isso adiciona $(P−1)·(L/R)$ de atraso extra antes mesmo do último pacote começar sua jornada. A partir daí, esse último pacote ainda precisa percorrer os N enlaces normalmente, levando $N·(L/R)$.

Logo, o atraso total (tempo até o **último bit do último pacote** chegar ao destino) é:

$$d_{fim-a-fim} = (P-1)\cdot\frac{L}{R} + N \cdot \frac{L}{R} = (N + P - 1)\cdot\frac{L}{R}$$
**Store-and-forward:** cada roteador no caminho segue a regra de esperar receber o pacote inteiro antes de começar a retransmiti-lo para o próximo enlace. Ou seja, cada um dos N enlaces do caminho "cobra" seu próprio L/R inteiro, de forma sequencial e cumulativa. O roteador N não pode começar a transmitir enquanto não recebeu 100% do pacote vindo do roteador N−1. É exatamente por isso que a fórmula tem o fator **N·(L/R)**: o atraso de transmissão se **multiplica** pelo número de saltos (hops).

**Cut-through switching:** nessa abordagem alternativa, o roteador não espera o pacote inteiro chegar. Assim que ele lê apenas o cabeçalho (o suficiente para saber por qual enlace de saída o pacote deve seguir), ele já começa a retransmitir os bits que já chegaram, à medida que os bits seguintes ainda estão chegando pelo enlace anterior. Ou seja, os "estágios" (enlaces) passam a operar de forma sobreposta/paralela, e não mais sequencial.

Por isso, no cut-through, o componente de atraso de transmissão deixa de ser proporcional a N, ele fica próximo de apenas $L/R$ , e os demais saltos adicionam apenas pequenos atrasos de processamento/propagação, não um L/R completo cada. O atraso deixa de "empilhar" a cada roteador extra no caminho.

2) P3  

	a) A comutação de circuitos seria mais apropriada para esse cenário. Ela consegue garantir a taxa constante que a aplicação precisa (sem risco de atraso de fila ou perda de pacotes por disputa de enlace), e não desperdiça recursos porque não há ociosidade a "aproveitar".

	b) Não, não é necessário nenhuma forma de controle de congestionamento nesse cenário específico. O controle de congestionamento existe justamente para lidar com situações em que a demanda pode, em algum momento, superar a capacidade e neste cenário esta situação nunca ocorre.
	
3) P4 -- circuit switch  

	a) 16 conexões simultâneas.
	b) 8 conexões simultâneas entre A e C.
	c) Sim, é possível acomodar as 8 conexões simultaneamente, desde que o roteamento seja feito de forma balanceada (2 conexões de cada grupo por cada rota alternativa), usando os 16 circuitos da rede em sua capacidade máxima.
  
4) P6 -- diferença propagação e transmissão  

	a) Atraso de propagação
$$d_{prop} = \frac{m}{s}$$
	b) Atraso de transmissão
$$d_{trans} = \frac{L}{R}$$
	c) Atraso fim-a-fim (ignorando processamento e fila)

	Os dois atrasos são **somados**, pois são sequenciais: primeiro A precisa empurrar todos os bits para o enlace (transmissão), e o **último bit** só termina de "viajar" depois de percorrer toda a distância (propagação):

$$d_{fim-a-fim} = d_{trans} + d_{prop} = \frac{L}{R} + \frac{m}{s}$$
	d) Em t = d_trans, onde está o **último bit** do pacote?
	
	Em t = d_trans, o Host A **acabou de terminar** de transmitir o pacote inteiro — ou seja, o último bit **acabou de sair de A e entrar no enlace**. Ele ainda não percorreu nenhuma distância significativa além do ponto de partida (está "no início" do enlace, saindo do host A).
	
	e) Se d_prop > d_trans, onde está o **primeiro bit** em t = d_trans?
	
	Se d_prop > d_trans, isso significa que a propagação é **mais lenta** que a transmissão — ou seja, o primeiro bit, mesmo tendo saído em t=0, **ainda não teve tempo suficiente para percorrer todo o enlace** até t = d_trans. Portanto: o primeiro bit está **em algum ponto no meio do enlace** (ainda "a caminho", não chegou a B).

	f) Se d_prop < d_trans, onde está o **primeiro bit** em t = d_trans?

	Se d_prop < d_trans, a propagação é **mais rápida** que a transmissão. Isso significa que o primeiro bit **já teve tempo de sobra** para percorrer todo o enlace antes mesmo de A terminar de transmitir o pacote inteiro. Portanto: o primeiro bit **já chegou ao Host B** (está no receptor, esperando o resto do pacote chegar).

	g) Encontrar m tal que d_prop = d_trans
	
	Dados: s = 2,5 × 10⁸ m/s, L = 1500 bytes, R = 10 Mbps

	Primeiro, converter unidades:
	- L = 1500 bytes × 8 bits/byte = **12.000 bits**
	- R = 10 Mbps = **10 × 10⁶ bits/s**

	Calculando d_trans:
	$$d_{trans} = \frac{L}{R} = \frac{12.000}{10 \times 10^6} = 1,2 \times 10^{-3} \text{ s} = 1,2 \text{ ms}$$

	Queremos d_prop = d_trans, ou seja:
	$$\frac{m}{s} = d_{trans} \implies m = s \times d_{trans}$$

	$$m = (2,5 \times 10^8) \times (1,2 \times 10^{-3}) = 3 \times 10^5 \text{ m} = 300 \text{ km}$$

	**Resposta:** m = 300.000 metros (300 km).

5) P7 -- exercício interessante por olhar para camada de aplicação VoIP  

O Host A gera um fluxo digital contínuo a **64 kbps**. Cada pacote tem **56 bytes**. Primeiro, convertendo para bits:

$$56 \text{ bytes} \times 8 = 448 \text{ bits por pacote}$$

O tempo necessário para **acumular** 448 bits a uma taxa de geração de 64.000 bits/segundo:

$$d_{empacot} = \frac{448 \text{ bits}}{64.000 \text{ bits/s}} = 0{,}007 \text{ s} = 7 \text{ ms}$$

Uma vez que o pacote está completo, o Host A o envia pelo enlace de 10 Mbps:

$$d_{trans} = \frac{L}{R} = \frac{448 \text{ bits}}{10 \times 10^6 \text{ bits/s}} = 0{,}0448 \text{ ms}$$

Somando as três etapas

$$d_{total} = d_{empacot} + d_{trans} + d_{prop} = 7 + 0{,}0448 + 10 = 17{,}0448 \text{ ms}$$

**Resposta: aproximadamente 17,04 ms**.

6) P23 -- muito importante -- packet pair 
	a) Pacote 1:
	- Termina de ser transmitido pelo servidor em: **L/Rs**
	- Chega **completo** ao roteador em: **L/Rs + d_prop**
	- Roteador começa a retransmitir imediatamente (sem fila, pois é o primeiro pacote) e termina de transmitir no link 2 em: **L/Rs + d_prop + L/Rc**
	- Chega ao cliente (último bit) em: **L/Rs + d_prop + L/Rc + d_prop**

	Pacote 2 (enviado back-to-back, logo começa em t = L/Rs):
	- Chega completo ao roteador em: **2L/Rs + d_prop**
	- Como **Rc > Rs** (link 2 é mais rápido, não é o gargalo), o roteador **já terminou** de transmitir o pacote 1 no link 2 antes do pacote 2 chegar completo — ou seja, **não há fila** no roteador. O pacote 2 começa a ser retransmitido assim que chega completo.
	- Chega ao cliente em: **2L/Rs + d_prop + L/Rc + d_prop**

	Intervalo entre chegadas (inter-arrival time):

$$\Delta t = (2L/Rs + d_{prop} + L/Rc + d_{prop}) - (L/Rs + d_{prop} + L/Rc + d_{prop}) = \frac{L}{Rs}$$

Resposta: o intervalo de chegada no destino é exatamente L/Rs
### b) Agora o link 2 é o gargalo (Rc < Rs)

**É possível o pacote 2 enfileirar na fila de entrada do link 2?**

Sim, é possível — e vamos justificar formalmente. Repetindo o raciocínio de chegada ao roteador:
- Pacote 1 chega completo ao roteador em **L/Rs + d_prop**, e começa a ser transmitido no link 2, terminando em **L/Rs + d_prop + L/Rc**
- Pacote 2 chega completo ao roteador em **2L/Rs + d_prop**

Como agora **Rc < Rs**, temos que **L/Rc > L/Rs**, o que significa que o pacote 1 **ainda está sendo transmitido** no link 2 quando o pacote 2 já chegou completo ao roteador (basta comparar: o pacote 1 só libera o link 2 em L/Rs + d_prop + L/Rc, que é **depois** de 2L/Rs + d_prop, já que L/Rc > L/Rs). Ou seja: **sim, o pacote 2 fica enfileirado**, esperando o link 2 ficar livre — porque agora o link de saída do roteador (mais lento) não consegue "escoar" os pacotes tão rápido quanto eles chegam pelo link de entrada (mais rápido).

**Qual o T mínimo (intervalo entre envios) para evitar essa fila?**

Agora o servidor não envia mais back-to-back — espera T segundos entre o início do envio do pacote 1 e do pacote 2. Queremos que o pacote 2 **só chegue** completo ao roteador **depois** que o link 2 já estiver livre (ou seja, depois que o pacote 1 tenha terminado de ser transmitido nele).

- Pacote 1 libera o link 2 em: **L/Rs + d_prop + L/Rc**
- Pacote 2 chega completo ao roteador em: **T + L/Rs + d_prop**

Para não haver fila, precisamos que:

$$T + \frac{L}{Rs} + d_{prop} \geq \frac{L}{Rs} + d_{prop} + \frac{L}{Rc}$$

Simplificando (os termos L/Rs + d_prop se cancelam dos dois lados):

$$T \geq \frac{L}{Rc}$$

**Resposta: T deve ser pelo menos L/Rc** — ou seja, o servidor precisa esperar, entre o envio dos dois pacotes, pelo menos o **tempo de transmissão de um pacote no enlace gargalo (mais lento)**. Isso garante que, quando o pacote 2 chegar ao roteador, o link 2 já esteja livre (o pacote 1 já foi totalmente escoado).

---

Essa questão amarra muito bem tudo que vimos: store-and-forward, atraso de transmissão, atraso de propagação e enlace gargalo — todos aparecendo juntos numa aplicação prática real (medição de banda). Pode mandar a próxima quando quiser.
  
7) Vídeo distribuições -- assista e resuma o vídeo, trazendo perguntas: [https://www.youtube.com/watch?v=C8DxAQT5goE](https://www.youtube.com/watch?v=C8DxAQT5goE)  

## Distribuição Discreta

Uma **distribuição de probabilidade discreta** descreve as chances de uma variável assumir determinado valor dentro de um conjunto **finito** ou **contável** de números inteiros.

### Distribuição Geométrica

> **A Pergunta-Chave:** *"Quantas tentativas eu preciso fazer ATÉ conseguir o PRIMEIRO sucesso?"*

#### Características:

* Cada tentativa é **independente** e tem apenas dois resultados: **Sucesso** (probabilidade $p$) ou **Fracasso** (probabilidade $q = 1 - p$).
* Possui a propriedade da **falta de memória**: o resultado de uma tentativa passada não afeta as próximas.

#### Fórmulas:

* **Probabilidade do 1º sucesso ocorrer na tentativa $n$:**
$$P(X = n) = q^{n-1} \cdot p$$
> *Significa: você fracassou $n-1$ vezes e depois acertou na $n$-ésima tentativa)*.

* **Número Médio de Tentativas (Esperança):**
$$E(X) = \frac{1}{p}$$
### Distribuição Binomial

> **A Pergunta-Chave:** *"Em um número FIXO de $n$ tentativas, QUANTOS sucessos eu vou obter?"*

#### Características:

* O número total de experimentos ($n$) é fixo e determinado antes de começar.
* As tentativas são independentes e a probabilidade de sucesso ($p$) é sempre a mesma em cada uma.
#### Fórmulas:

* **Probabilidade de obter $r$ sucessos em $n$ tentativas:**
$$P(X = r) = \binom{n}{r} \cdot p^r \cdot q^{n-r}$$
> *(Sendo $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ o número de combinações possíveis)*.

* **Número Médio de Sucessos (Esperança):**
$$E(X) = n \cdot p$$

### Distribuição de Poisson

> **A Pergunta-Chave:** *"Quantas vezes um evento raro acontece dentro de um INTERVALO contínuo (tempo, espaço, área)?"*
#### Características:

* Eventos ocorrem de forma **aleatória e independente** ao longo de um intervalo determinado (ex.: 2 minutos, 1 km, 1 hora).
* A taxa média de ocorrências no intervalo é conhecida e fixa, representada por $\lambda$ (lambda).
* É equivalente à Distribuição Binomial quando o número de tentativas ($n$) tende ao infinito e a probabilidade ($p$) é muito pequena.

#### Fórmulas:

* **Probabilidade de ocorrerem $k$ eventos:**
$$P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}$$
> *(Onde $e \approx 2,71828$ é a base do logaritmo natural)*.

* **Média de Eventos (Esperança):**
$$E(X) = \lambda$$

| Distribuição   | O que mede a variável $X$?            | Parâmetros Necessários                     | Média $E(X)$  |
| -------------- | ------------------------------------- | ------------------------------------------ | ------------- |
| **Geométrica** | Nº de tentativas até o **1º sucesso** | $p$ (chance de sucesso)                    | $\frac{1}{p}$ |
| **Binomial**   | Nº de **sucessos em $n$ tentativas**  | $n$ (tentativas) e $p$ (chance de sucesso) | $n \cdot p$   |
| **Poisson**    | Nº de **eventos por intervalo**       | $\lambda$ (taxa média do intervalo)        | $\lambda$     |

8) Vídeo lei de Little -- assista e resuma o vídeo, trazendo perguntas: [https://www.youtube.com/watch?v=p1sG7mm1Ixo](https://www.youtube.com/watch?v=p1sG7mm1Ixo)  

## Lei de Little (Little's Law)


### O que é a Lei de Little?

Ela estabelece uma relação matemática simples, porém extremamente poderosa, entre três variáveis médias de qualquer sistema em estado estável:

1. Quantos itens/clientes estão **dentro** do sistema.
2. Com que **frequência** eles chegam.
3. Quanto **tempo** eles passam lá dentro.

### A Fórmula Fundamental

$$L = \lambda \cdot W \quad \text{ou} \quad \bar{N} = \lambda \cdot \bar{T}$$

* **$L$ ou $\bar{N}$ (Número Médio no Sistema):** Quantidade média de clientes ou itens presentes no sistema ao longo do tempo 
* **$\lambda$ (Lambda - Taxa Média de Chegada):** Quantidade média de clientes que chegam ao sistema por unidade de tempo 
* **$W$ ou $\bar{T}$ (Tempo Médio no Sistema):** Tempo médio que cada cliente passa no sistema (incluindo tempo de espera na fila + tempo de atendimento)
### Exemplo: A Loja de Donuts do Bruno) 

Para demonstrar a utilidade da lei, o vídeo apresenta a história de Bruno, que deseja abrir uma loja de donuts:

* **O que Bruno observou:**
* Em média, há **3 pessoas** dentro da loja ($\bar{N} = 3$) 
* O tempo médio que cada cliente leva desde a entrada até a saída é de **3 minutos** ($\bar{T} = 3\text{ min}$) 
* **A dúvida de Bruno:** Qual é a taxa média de chegada de clientes ($\lambda$)? 

Aplicando a Lei de Little:

$$
\bar{N} = \lambda \cdot \bar{T} \implies 3 = \lambda \cdot 3 \implies \lambda = 1 \text{ cliente por minuto}
$$

O grande diferencial do Resultado de Little é a sua **generalidade** 
* **Não depende do formato da fila:** Funciona para filas por ordem de chegada (FIFO), prioridade, etc 
* **Não depende das distribuições:** Vale independentemente de o tempo entre chegadas ou de atendimento seguir uma distribuição Normal, Exponencial ou de Poisson 
* **Aplica-se a qualquer janela de tempo:** Possa ser analisado em minutos, dias, meses ou no longo prazo 
### Aplicações Práticas

| Área                      | O que é $L$ ($\bar{N}$)?         | O que é $\lambda$?             | O que é $W$ ($\bar{T}$)?     |
| ------------------------- | -------------------------------- | ------------------------------ | ---------------------------- |
| **Computação / Redes**    | Pacotes na fila do roteador      | Pacotes recebidos por segundo  | Latência média do pacote     |
| **Gestão Ágil (Kanban)**  | Tarefas em andamento (*WIP*)     | Vazão / Entrega (*Throughput*) | Tempo de ciclo (*Lead Time*) |
| **Sistemas Hospitalares** | Pacientes leitados/na emergência | Taxa de admissão de pacientes  | Tempo médio de internação    |

9) Estude os slides [https://tinyurl.com/filaufrj20261](https://tinyurl.com/filaufrj20261) e liste 3 dúvidas  

	- Dúvida 1 : Por que a taxa de chegada "vira" a taxa de serviço na equação da utilização?
	- Dúvida 2 : A aproximação do "tempo residual" na equação de W. Na equação que dá origem ao tempo de espera W (a que soma Nq · d_transmissão com I · d_transmissão), o segundo termo parece representar o tempo restante do pacote que já está sendo atendido no servidor
	- Dúvida 3 : A relação entre N = I/(1-I) dos slides e o gráfico de atraso de fila do Kurose
  
10) derive, por conta própria, o resultado N = I/(I-I) usando a abordagem apresentada nos slides (é só reescrever com suas palavras)  
 
 $a$ = taxa média de chegada de pacotes (pacotes/segundo)
 $d_{trans} = L/R$ = tempo médio de serviço (tempo de transmissão de um pacote)
 $I = a·L/R$ = intensidade de tráfego (fração de tempo que o servidor está ocupado)
 $N_s$ = número médio de pacotes **no servidor** (só pode ser 0 ou 1, pois o servidor atende um pacote por vez)
 $N_q$ = número médio de pacotes **na fila de espera** (esperando, ainda não sendo atendidos)
 $N = N_q + N_s$ = número médio total de pacotes no sistema (fila + servidor)
 $W$ = tempo médio de espera **na fila** (antes de começar a ser servido)
 $T = W + d_{trans}$ = tempo total médio no sistema (fila + serviço)

A fração de tempo que ele está ocupado é, por definição, a própria intensidade de tráfego I. Então, em média:

$$N_s = 1 \cdot I + 0 \cdot (1-I) = I$$


Um pacote que chega precisa esperar por duas coisas:
1. Os pacotes que **já estão na fila** à sua frente (em média, N_q pacotes, cada um levando d_trans para ser servido)
2. O **"resto" do pacote que já está sendo atendido** no servidor, se houver um. Como o tempo de serviço é sempre d_trans (determinístico — todos os pacotes têm o mesmo tamanho L, mesmo enlace R), e a probabilidade de encontrar o servidor ocupado é I, esse termo contribui, em média, com **I · d_trans**

Logo:

$$W = N_q \cdot d_{trans} + I \cdot d_{trans}$$

$$N_q = a \cdot W$$

Substituindo isso na equação

$$W = (a \cdot W) \cdot d_{trans} + I \cdot d_{trans}$$

Colocando W em evidência:

$$W - a \cdot d_{trans} \cdot W = I \cdot d_{trans}$$
$$W \cdot (1 - a \cdot d_{trans}) = I \cdot d_{trans}$$

Lembrando que **a · d_trans = a·L/R = I**, substituo dentro do parênteses:

$$W \cdot (1 - I) = I \cdot d_{trans}$$

$$W = \frac{I \cdot d_{trans}}{1 - I}$$

Tempo total no sistema (T)

$$T = W + d_{trans} = \frac{I \cdot d_{trans}}{1-I} + d_{trans}$$

Colocando d_trans em evidência:

$$T = d_{trans} \left( \frac{I}{1-I} + 1 \right) = d_{trans} \left( \frac{I + (1-I)}{1-I} \right) = d_{trans} \cdot \frac{1}{1-I}$$

$$T = \frac{d_{trans}}{1-I}$$

Aplicando a Lei de Little novamente, agora ao sistema todo

$$N = a \cdot T = a \cdot \frac{d_{trans}}{1-I}$$

Como **a · d_trans = I**, substituo:

$$N = \frac{I}{1-I}$$


11) repita a mesma coisa, agora usando cadeias de Markov, e mostre que o resultado é o mesmo  

**Modelo:** processo de nascimento e morte, estado n = número de pacotes no sistema. Chegadas Poisson com taxa λ = a; serviço exponencial com taxa μ = R/L. Definimos **I = λ/μ = a·L/R**.


**Balanço detalhado** (fluxo n→n+1 = fluxo n+1→n):

$$\lambda p_n = \mu p_{n+1} \implies p_{n+1} = I \cdot p_n \implies p_n = I^n \cdot p_0$$

**Normalização** ($\sum p_n = 1$, com I < 1):

$$p_0 \sum_{n=0}^\infty I^n = p_0 \cdot \frac{1}{1-I} = 1 \implies p_0 = 1-I$$

Logo: $p_n = (1-I)\,I^n$ (distribuição geométrica).

**Número médio no sistema:**

$$N = \sum_{n=0}^\infty n \cdot p_n = (1-I)\sum_{n=0}^\infty n I^n = (1-I) \cdot \frac{I}{(1-I)^2}$$

$$\boxed{N = \frac{I}{1-I}}$$

12) o que acontece se o tempo de transmissão for determinístico igual a L/R ao invés de exponencial? Como fica a equação de N? E a equação de W?  
  
13) o que acontece se a taxa de chegada dobrar e a capacidade de serviço também? Ou seja, a'=2a e R'=2R. Quanto vale N e W depois das modificações? E La/R? Qual muda e qual não muda? Justifique intuitivamente sua resposta.  
  
14) P13 do livro 8a edição  
  
15)  P14 do livro 8a edição  
  
16)  P15 do livro 8a edição  
  
17) P16 do livro 8a edição -- esse enunciado talvez tenha um problema! caso encontre um problema, aponte o problema e conserte o enunciado, como julgar adequado. depois de propor um novo enunciado, resolva o problema que você mesmo bolou  
  
18) P17 do livro 8a edição  
  
19) P22 do livro 8a edição -- perda de pacotes  
  
20) melhorar o material em [https://www.overleaf.com/read/wmkckszznbjz#04ba5c](https://www.overleaf.com/read/wmkckszznbjz#04ba5c) possivelmente mexendo direto nos arquivos que estão no overleaf  criando uma cópia do repositório ou então listando sugestões