# Capítulo 1: Redes de Computadores e a Internet

## 1.1 O que é a Internet?

### 1.1.1 Descrição por Componentes (_Nuts-and-Bolts_)

A Internet é a maior infraestrutura de engenharia construída pela humanidade. Ela é composta por três elementos de _hardware_ e _software_ fundamentais:

1. **Sistemas Finais (_Hosts_ ou _End Systems_):** Dispositivos conectados à rede que executam aplicações na periferia (borda). Incluem computadores, servidores em _datacenters_, _smartphones_, veículos conectados e dispositivos IoT.
2. **Enlaces de Comunicação (_Links_):** Meios físicos (fibra óptica, cabo coaxial, par trançado, rádio) que transportam dados entre dispositivos a uma determinada **taxa de transmissão** ou largura de banda ( R ), medida em **bits por segundo (bits/s)**.
3. **Comutadores de Pacotes (_Packet Switches_):** Equipamentos intermediários no núcleo da rede que recebem blocos de dados (**pacotes**), examinam seus cabeçalhos e os encaminham em direção ao destino. Os dois tipos principais são os **roteadores** (camada de rede) e os **_switches_ de enlace** (camada de enlace).

Os sistemas finais conectam-se à Internet por meio de **Provedores de Serviços de Internet (ISPs)** de diferentes níveis (locais, regionais e globais).

---

### 1.1.2 Descrição por Serviços (_Services Description_)

Sob a perspectiva das aplicações, a Internet é uma **infraestrutura que fornece serviços** para aplicações distribuídas (Web, _streaming_ de vídeo, jogos _online_, e-mail, e-commerce).

Ela disponibiliza para os programas finais uma **Interface de Programação de Aplicação (API)** — um conjunto de regras que permite que um programa rodando em um sistema final solicite à infraestrutura da Internet a entrega de dados a outro programa rodando em outro hospedeiro.

---

### 1.1.3 O que é um Protocolo?

Toda a atividade de comunicação na Internet é governada por **protocolos**.

- **Analogia Humana:** Quando você deseja saber as horas, diz "Com licença, que horas são?". Se a outra pessoa entender o idioma e a convenção social, responderá com a hora. Se você falar em um idioma desconhecido, a comunicação falha.
- **Definição de Rede:** Um **protocolo** define o **formato** e a **ordem** das mensagens trocadas entre duas ou mais entidades comunicantes na rede, bem como as **ações tomadas** na transmissão e/ou recepção de uma mensagem ou outro evento.

---

## 1.2 A Borda da Rede (_Network Edge_)

A borda da rede é o local onde ficam os sistemas finais (_hosts_), que abrigam os programas de aplicação (clientes e servidores).

```
[ Aplicações / Hosts ]<--->[ Rede de Acesso ]<--->[ Núcleo da Rede (Roteadores) ]
    (Borda da Rede)        (DSL, FTTH, Wi-Fi)      (Comutação de Pacotes)
```

---

### 1.2.1 Redes de Acesso (_Access Networks_)

A rede de acesso é a infraestrutura física que conecta fisicamente um sistema final ao seu primeiro roteador (_edge router_) no caminho para o núcleo. As principais tecnologias são:

- **DSL (_Digital Subscriber Line_):** Utiliza a linha telefônica de par trançado de cobre existente para transmitir dados em frequências mais altas do que a voz.
- **Cabo / HFC (_Hybrid Fiber-Coaxial_):** Utiliza a infraestrutura de TV a cabo com multiplexação por divisão de frequência (FDM). Múltiplos canais de dados e TV compartilham o mesmo cabo coaxial até um nó óptico residencial.
- **FTTH (_Fiber to the Home_):** Leva a fibra óptica diretamente da central telefônica até a residência, oferecendo taxas de transmissão de centenas de Mbps a Gbps por meio de arquiteturas como PON (_Passive Optical Network_).
- **Wireless e Celular:**
    - **Wi-Fi (802.11):** Acesso sem fio de curto alcance conectado a um Ponto de Acesso (AP) que se conecta à rede cabeada.
    - **4G LTE / 5G:** Acesso sem fio de grande área conectado a torres de celular (_base stations_) operadas por provedores móveis.

---

### 1.2.2 Meios Físicos de Transmissão (_Physical Media_)

A informação física navega pela rede na forma de ondas eletromagnéticas ou impulsos ópticos guiados ou não guiados:

1. **Meios Guiados (_Guided Media_):** O sinal se propaga contido dentro de um meio sólido.
    - **Par Trançado de Cobre (_Twisted Pair - UTP_):** O meio mais comum para redes locais (Ethernet). Os fios são trançados em pares para reduzir a interferência eletromagnética de pares vizinhos.
    - **Cabo Coaxial:** Formado por dois condutores de cobre concêntricos. Suporta taxas mais altas e transmissão banda larga (múltiplos canais por FDM).
    - **Fibra Óptica:** Condutor de vidro flexível e fino que carrega pulsos de luz. Suporta taxas extremamente altas (dezenas a centenas de Gbps) com imunidade a interferências eletromagnéticas e atenuação muito baixa por quilômetro.
2. **Meios Não Guiados (_Unguided Media_):** O sinal se propaga livremente na atmosfera ou no espaço.
    - **Rádio:** Onda eletromagnética enviada pelo ar. Sofre com degradação devido a barreiras físicas, reflexão e interferência de outros dispositivos. Exemplos: canais de rádio de redes Wi-Fi, celulares e enlaces por satélite (LEO e GEO).

---
## 1.3 O Núcleo da Rede (_Network Core_)

O núcleo da rede é a malha interconectada de comutadores de pacotes (_roteadores_ e _switches_) e enlaces que conectam as redes de acesso entre si. Sua função primária é transportar dados de um sistema final de origem para um de destino através de nós intermediários.

---

### 1.3.1 Comutação de Pacotes (_Packet Switching_)

#### Conceito

Na comutação de pacotes, os sistemas finais dividem as mensagens em blocos discretos de dados chamados **pacotes**. Cada pacote atravessa a rede transitando por enlaces e comutadores de pacotes. Os dados são transmitidos à taxa total do enlace de saída.

##### 1. Transmissão Armazena-e-Reenvia (_Store-and-Forward_)

A maioria dos comutadores de pacotes opera segundo o princípio de **armazena-e-reenvia**: o comutador precisa receber o pacote por inteiro em seu _buffer_ de entrada antes de poder começar a transmitir o primeiro bit do pacote para o enlace de saída.

- **Análise de Atraso Simples:** Se enviarmos 1 pacote de (L) bits através de (N) enlaces idênticos em série, cada um com taxa de transmissão (R) (e ignorando a propagação por enquanto), o atraso fim a fim é: $d_{\text{fim-a-fim}} = N \cdot \frac{L}{R}$

##### 2. Atraso de Fila e Perda de Pacotes

Cada comutador possui múltiplos enlaces de saída. Para cada enlace, o comutador mantém um **buffer de saída** (ou fila):

- **Formação de Fila:** Se um pacote chega e encontra o enlace ocupado transmitindo outro pacote, ele precisa aguardar no _buffer_.
- **Perda de Pacote (_Packet Loss_):** Como a memória do _buffer_ é finita, se um pacote chegar e encontrar o _buffer_ completamente cheio, o comutador não terá onde armazená-lo e o descartará (_drop_).

##### 3. Tabelas de Repasse e Protocolos de Roteamento

Como o roteador sabe para qual enlace de saída enviar determinado pacote?

- Cada pacote contém em seu cabeçalho o **endereço IP de destino**.
- O roteador possui uma **tabela de repasse** (_forwarding table_) que mapeia endereços IP de destino para seus enlaces de saída físicos.
- As tabelas de repasse são construídas automaticamente por **protocolos de roteamento** (como OSPF e BGP) que calculam os caminhos mais curtos e eficientes através da malha.

---

### 1.3.2 Comutação de Circuitos (_Circuit Switching_)

#### Conceito

Na comutação de circuitos, os recursos necessários ao longo de um caminho para prover a comunicação entre os sistemas finais (largura de banda, tempos de comutação) são **reservados e dedicados exclusivamente** durante toda a duração da sessão de comunicação.

```
[ Usuário A ]  ===(Recursos Reservados/Dedicados)===  [ Usuário B ]
```

##### Multiplexação na Comutação de Circuitos

Para permitir que múltiplos circuitos compartilhem o mesmo cabo físico, utilizam-se duas técnicas clássicas de multiplexação:

1. **FDM (_Frequency-Division Multiplexing_):** O espectro de frequência do meio é dividido em faixas fixas. Cada conexão recebe sua própria faixa dedicada.
2. **TDM (_Time-Division Multiplexing_):** O tempo é dividido em quadros (_frames_) com número fixo de compartimentos de tempo (_slots_). Cada conexão recebe um _slot_ exclusivo por quadro.

---

### 1.3.3 Comparação e Unificação Matemática: Multiplexação Estatística (Kurose + UFRJ)

#### Fenômeno de Rede

Por que a Internet moderna utiliza comutação de pacotes em vez de comutação de circuitos? Os usuários de rede não transmitem dados continuamente; o tráfego de aplicações Web, e-mail e áudio/vídeo é essencialmente **em rajadas** (_bursty_) — alternando períodos curtos de transmissão intensa com longos períodos de ociosidade.

---

#### Unificação Matemática 1: O Modelo Binomial de Usuários Ativos

##### 1. O que representa?

Modela o número aleatório de usuários ativamente transmitindo dados ao mesmo tempo em um enlace compartilhado por uma população finita de usuários independentes.

##### 2. Por que estamos usando esse modelo?

Para provar quantitativamente por que a comutação de pacotes permite admitir **muito mais usuários** na mesma infraestrutura do que a comutação de circuitos, mantendo a probabilidade de congestionamento (_sobrecarga_) extremamente baixa.

##### 3. Significado das Variáveis e Unidades

-  m  (ou  N ): Número total de usuários independentes que compartilham o enlace.
-  p : Probabilidade de um usuário individual estar ativo (transmitindo dados) em um dado instante.
-  A  (ou  X ): Variável aleatória discreta que representa o **número de usuários ativos simultaneamente** em um dado instante.
-  R : Capacidade total do enlace de saída (ex: $1\text{ Mbps}$).
- ($r$) (ou $C$): Número máximo de usuários simultâneos que a rede consegue atender sem formar fila (ex: se cada usuário precisa de $100\text{ kbps}$ , um enlace de $1\text{ Mbps}$ suporta $r = \frac{1\text{ Mbps}}{100\text{ kbps}} = 10$  usuários dedicados).

##### 4. Hipóteses do Modelo
- Os  m  usuários comportam-se de maneira totalmente **independente**.
- Cada usuário tem a mesma probabilidade  p  de estar ativo em qualquer instante.
##### 5. Aplicação da Fórmula

Como cada usuário está ativo ( 1 ) com probabilidade  p  ou inativo ( 0 ) com probabilidade  1-p , o número total de ativos  A  segue uma **Distribuição Binomial**:

$$A \sim \text{Binomial}(m, p)$$

A probabilidade de haver exatamente  a  usuários ativos no mesmo instante é dada pela Função de Massa de Probabilidade (PMF):

$$P(A = a) = \binom{m}{a} p^{a} (1-p)^{m-a} = \frac {m!}{a!(m-a)!} p^{a} (1-p)^{m-a}$$

A **Carga Esperada** (número médio de usuários ativos) é: $$E[A] = m \cdot p$$

- **Em Comutação de Circuitos:** Admitimos no máximo  m = r  usuários. Se  r=10 , apenas 10 usuários podem ser aceitos, mesmo que passem a maior parte do tempo em silêncio.
- **Em Comutação de Pacotes:** Permitimos que  m > r  usuários compartilhem o enlace. Haverá **sobrecarga/congestionamento** quando  A > r . A probabilidade de sobrecarga  P(A > r)  é a cauda da distribuição binomial:

$$P(A > r) = \sum_{a=r+1}^{m} \binom{m}{a} p^a (1-p)^{m-a} = 1 - \sum_{a=0}^{r} \binom{m}{a} p^a (1-p)^{m-a}$$

##### 6. Cálculo e Interpretação (Exemplo Clássico Kurose / Prova UFRJ)

Considere um enlace de  $1\text{ Mbps}$ , onde cada usuário consome  $100\text{ kbps}$  quando ativo, mas fica ativo apenas durante  10%) do tempo ( $p = 0{,}1$ ).

1. **Comutação de Circuitos:** Cada usuário requer  $100\text{ kbps}$  reservados. O enlace suporta estritamente  r = 10  usuários. O 11º usuário é bloqueado.
2. **Comutação de Pacotes:** Conectamos **m = 35  usuários** no mesmo enlace!
    - Carga média esperada:  E[A] = $35 \times 0{,}1 = 3{,}5$  usuários ativos em média.
    - Probabilidade de sobrecarga (mais de 10 usuários ativos simultaneamente): $P(A > 10)$ = $\sum_{a=11}^{35} \binom{35}{a}$ $(0{,}1)^a (0{,}9)^{35-a}$ $\approx 0{,}0004$ $\quad(0{,}04\%)$

- **Interpretação:** Em  $99{,}96\%$  do tempo, há 10 ou menos usuários ativos e a rede funciona sem nenhum atraso de fila. Suportamos **3,5 vezes mais usuários** do que na comutação de circuitos com uma taxa de sobrecarga insignificante (menos de 4 vezes em 10.000 instantes). Isso é o poder da **multiplexação estatística**.

---

#### Unificação Matemática 2: A Aproximação de Poisson (UFRJ)

##### 1. O que representa?

Modela o número de usuários ativos quando a população total de usuários ( m ) é muito grande, mas a probabilidade de cada um estar ativo ( p ) é muito pequena.

##### 2. Por que estamos usando esse modelo?

Calcular somatórios binomiais com números combinatórios  $\binom{m}{a}$  para  $m = 1000$  ou mais é computacionalmente custoso e suscetível a estouros de precisão. A distribuição de Poisson fornece uma aproximação analítica rápida e precisa.

##### 3. Significado das Variáveis e Unidades

-  $\lambda = m \cdot p$ : Carga média total mantida constante (unidade: número médio de usuários ativos).

##### 4. Hipóteses

-  $m \to \infty$  (grande número de fontes).
-  $p \to 0$  (cada fonte raramente ativa).
-  $\lambda = m \cdot p$  permanece moderado.

##### 5. Aplicação da Fórmula

Substituindo o limite da Binomial quando  $m \to \infty$ , obtemos a PMF da **Poisson**:

$$P(A = a) \approx \frac{e^{-\lambda} \cdot \lambda^a}{a!}$$

---

#### Unificação Matemática 3: O Tempo de Descongestionamento — Modelo Geométrico (Notas UFRJ)

##### 1. O que representa?

Modela o número de _slots_ de tempo necessários ( S ) para que a rede saia do estado de sobrecarga e volte a ficar descongestionada.

##### 2. Por que estamos usando esse modelo?

A variável binomial  A  tira apenas uma "fotografia" estática de um instante da rede. A variável temporal  S  responde à pergunta do operador de rede: _"Dado que a rede congestionou no slot atual, quantos slots levaremos, em média, até a rede voltar ao normal?"_

##### 3. Significado das Variáveis e Unidades

-  q : Probabilidade de um _slot_ estar descongestionado (sucesso, ou seja,  $P(A \le r)$ ).
-  1 - q : Probabilidade de o _slot_ estar congestionado ( $P(A > r)$ ).
-  S : Número de _slots_ futuros até observar o primeiro _slot_ descongestionado ( $S \in {1, 2, 3, \dots}$ ).

##### 4. Hipóteses

- Os estados da rede em _slots_ consecutivos são temporalmente **independentes**.

##### 5. Aplicação das Fórmulas

Como estamos contando o número de tentativas até obter o primeiro sucesso (slot descongestionado),  S  segue uma **Distribuição Geométrica**:

$$S \sim \text{Geom}(q)$$ $$P(S = s) = (1 - q)^{s-1} \cdot q, \quad s = 1, 2, 3, \dots$$

O **Tempo Médio de Recuperação (Esperança de  S )** é:

$$E[S] = \frac{1}{q}$$

##### 6. Interpretação em Termos de Redes

Se a probabilidade de um slot estar normal for  $q = 0{,}50$ , o tempo médio de descongestionamento é  $E[S] = \frac{1}{0{,}50} = 2\text{ slots}$ . Se a rede estiver extremamente sobrecarregada com  $q = 0{,}20$ , levará em média  $E[S] = \frac{1}{0{,}20} = 5\text{ slots}$  para se recuperar.


### Packet Pair

Para estimar a capacidade física $R_b$ do enlace mais lento (o **gargalo**) ao longo de um caminho sem depender de acesso direto aos roteadores intermediários, envia-se um par de pacotes de mesmo tamanho $L$ em sequência imediata.

1. **O Fenômeno:**
    - Na emissão, os pacotes são enviados com um espaçamento inicial de entrada $\Delta_{\text{in}} = \frac{L}{R_1}$.
2. **A Matemática do Espaçamento de Saída:**
    - A dispersão temporal observada no receptor atende à relação: $$\Delta_{\text{out}} = \max\left(\frac{L}{R_1}, \frac{L}{R_2}\right) = \frac{L}{\min(R_1, R_2)}$$
3. **Análise dos Casos:**
    - **Enlace 2 é o Gargalo ($R_1 > R_2$):** O primeiro enlace injeta o segundo pacote no roteador antes que o primeiro pacote termine de ser transmitido no segundo enlace. O segundo pacote fica retido no _buffer_ por um tempo de fila $W_{q,2} = \frac{L}{R_2} - \frac{L}{R_1}$, e os pacotes saem separados por $\Delta_{\text{out}} = \frac{L}{R_2}$.
    - **Primeiro Enlace é o Gargalo ($R_1 < R_2$):** O segundo enlace transmite o primeiro pacote mais rápido do que o tempo que o primeiro enlace leva para entregar o segundo pacote. Não há formação de fila (o roteador fica temporariamente ocioso), e a dispersão original é mantida: $\Delta_{\text{out}} = \frac{L}{R_1}$.
4. **Estimativa de Capacidade:**
    - O receptor calcula a estimativa da capacidade do gargalo medindo o intervalo $\Delta_{\text{out}}$: $$\hat{R}_{\text{gargalo}} \approx \frac{L}{\Delta_{\text{out}}}$$
### 1.3.4 Redes de Redes (_A Network of Networks_)

Como os bilhões de sistemas finais se conectam globalmente? A Internet não é mantida por um único provedor, mas é uma **estrutura hierárquica de ISPs interconectados**:

```
[ ISPs Locais / Redes de Acesso ]
          ↓
  [ ISPs Regionais ]
          ↓
  [ ISPs de Nível 1 (Tier-1 ISPs) ] <---> [ Pontos de Troca de Tráfego (IXPs) ]
          ↑
  [ Redes de Provedores de Conteúdo (ex: Google, Akamai) ]
```

1. **ISPs de Nível 1 (_Tier-1 ISPs_):** Provedores globais com cobertura internacional (ex: AT&T, Cogent, NTT). Eles se interconectam diretamente por meio de enlaces privados de **peering** (sem custo de tráfego mútuo).
2. **Pontos de Troca de Tráfego (_IXPs - Internet Exchange Points_):** Estruturas físicas onde múltiplos ISPs de nível 1, 2 e redes de conteúdo se reúnem para trocar tráfego diretamente, reduzindo custos de trânsito.
3. **Redes de Provedores de Conteúdo (_Content Provider Networks_):** Grandes empresas (como Google, Microsoft e Facebook) constroem suas próprias redes privadas de fibra óptica e _datacenters_, ignorando os ISPs de nível superior e conectando-se diretamente aos ISPs locais/regionais para entregar conteúdo com menor latência.

## 1.4 Atraso, Perda e Vazão em Redes de Comutação de Pacotes

### 1.4.1 Visão Geral dos Atrasos Nodal e Fim a Fim

#### Fenômeno de Rede

Quando um pacote transita da origem ao destino, ele passa por uma sequência de roteadores intermediários. Em cada nó, o pacote não é repassado instantaneamente; ele sofre uma série de atrasos físicos e operacionais.

#### Conceito

O **Atraso Nodal Total** ($d_{\text{nodal}}$) em um único comutador de pacotes é a soma de quatro componentes fundamentais:

$$d_{\text{nodal}} = d_{\text{proc}} + d_{\text{fila}} + d_{\text{trans}} + d_{\text{prop}}$$

```
[ Chegada ] ---> [ Processamento (d_proc) ] ---> [ Fila de Espera (d_fila) ] ---> [ Transmissão (d_trans) ] ---> [ Enlace (d_prop) ] ---> [ Próximo Nó ]
```

1. **Atraso de Processamento ($d_{\text{proc}}$):** Tempo que a CPU do roteador leva para examinar o cabeçalho do pacote, verificar erros de _checksum_ e determinar a interface de saída pela tabela de repasse. Tipicamente na ordem de **microssegundos** ou menos.
2. **Atraso de Fila ($d_{\text{fila}}$ ou $W$):** Tempo que o pacote passa aguardando no _buffer_ de saída enquanto outros pacotes à sua frente são transmitidos. Varia dinamicamente de $0$ até milissegundos dependendo do tráfego.
3. **Atraso de Transmissão ($d_{\text{trans}}$ ou $S$):** Tempo para injetar (serializar) todos os $L$ bits do pacote no enlace. $d_{\text{trans}} = L/R$.
4. **Atraso de Propagação ($d_{\text{prop}}$):** Tempo para um único bit percorrer a distância física do meio à velocidade da luz no meio. $d_{\text{prop}} = d/s$.

---

### 1.4.2 Atraso de Fila e Intensidade de Tráfego

#### Fenômeno de Rede

Por que a fila se forma? Se a taxa na qual os bits chegam à porta de saída do roteador for maior do que a taxa na qual o enlace consegue transmiti-los, os pacotes precisam ser armazenados temporariamente no _buffer_.

#### Conceito

A métrica fundamental para avaliar o estado de congestionamento de um nó é a **Intensidade de Tráfego** ($I$, também denotada por $\rho$ em teoria de filas).

---

#### Unificação Matemática 1: Intensidade de Tráfego e Condição de Estabilidade

##### 1. O que representa?

A razão entre a taxa média de chegada de bits e a capacidade de transmissão do enlace. Representa também a **utilização do enlace** ($U$), ou seja, a fração de tempo em que o enlace fica ocupado transmitindo dados.

##### 2. Por que estamos usando este modelo?

Para estabelecer o limite físico sob o qual uma rede opera de forma estável.

##### 3. Significado das Variáveis e Unidades

- $a$ (ou $\lambda$): Taxa média de chegada de pacotes ao nó ($\text{pacotes/segundo}$).
- $L$: Tamanho médio dos pacotes ($\text{bits}$).
- $R$: Taxa de transmissão do enlace ($\text{bits/s}$).
- $\mu = \frac{R}{L}$: Taxa média de serviço do enlace ($\text{pacotes/segundo}$).
- $S = \frac{1}{\mu} = \frac{L}{R}$: Tempo médio de serviço/transmissão de um pacote ($\text{segundos}$).

##### 4. Hipóteses

- O sistema opera em **equilíbrio estacionário** (o que entra sai).
- O _buffer_ possui capacidade ilimitada para armazenar pacotes.

##### 5. Aplicação da Fórmula

$$I = \rho = \frac{a \cdot L}{R} = \frac{\lambda}{\mu} \quad \text{[adimensional]}$$

- **Se $I > 1$:** Chega mais trabalho do que o enlace pode processar. A fila cresce sem limite e o atraso tende ao infinito ($d_{\text{fila}} \to \infty$).
- **Se $I < 1$:** O sistema é estável. A utilização do servidor é $U = I$.
- **Se $I = 1$:** O sistema só é estável se as chegadas e os tempos de serviço forem estritamente **determinísticos** ($D/D/1$) sem nenhuma variabilidade. Na presença de aleatoriedade, $I=1$ causa estouro de fila.

---

#### Unificação Matemática 2: A Lei de Little (UFRJ)

##### 1. O que representa?

Uma lei fundamental e universal da teoria de filas que relaciona a quantidade média de entidades no sistema com a taxa de entrada e o tempo médio de permanência.

##### 2. Por que estamos usando este modelo?

Porque ela **não depende** da distribuição probabilística do tráfego nem da regra de atendimento; ela se aplica a qualquer sistema em equilíbrio.

##### 3. Significado das Variáveis e Unidades

- $a$ (ou $\lambda$): Taxa média efetiva de chegada de pacotes ($\text{pacotes/s}$).
- $T$: Tempo total médio que um pacote passa no sistema (fila + serviço) ($\text{s}$).
- $W$ (ou $d_{\text{fila}}$): Tempo médio de espera do pacote estritamente na **fila** ($\text{s}$).
- $S = \frac{L}{R}$: Tempo médio de transmissão no **servidor** ($\text{s}$).
- $N$: Número médio de pacotes no **sistema completo** ($N = N_q + N_s$).
- $N_q$ (ou $E[B]$): Número médio de pacotes aguardando na **fila**.
- $N_s$: Número médio de pacotes em transmissão no **servidor** ($N_s = U = I$).

##### 4. Hipóteses

- O sistema está em equilíbrio estatístico e conservação de taxa ($I < 1$).

##### 5. Aplicação das Fórmulas de Little

1. **Ao Sistema Completo:** $N = a \cdot T$
2. **Apenas à Fila de Espera:** $N_q = a \cdot W$
3. **Apenas ao Servidor:** $N_s = a \cdot S = a \cdot \frac{L}{R} = I$

---

#### Unificação Matemática 3: O Modelo de Fila $M/M/1$ (Gabarito Provas UFRJ)

##### 1. O que representa?

Modela o atraso e a ocupação de um buffer de roteador assumindo **chegadas de Poisson** ($M$) e **tempos de transmissão exponenciais** ($M$, ou seja, tamanhos de pacote aleatórios).

##### 2. Por que estamos usando este modelo?

Fornece uma expressão analítica exata para prever como o atraso de fila cresce de forma assintótica conforme a utilização $I$ se aproxima de $1$.

##### 3. Hipóteses do Modelo

- **Chegadas de Poisson** (propriedade **PASTA**: _Poisson Arrivals See Time Averages_ — o pacote que chega enxerga a média temporal do estado da rede).
- **Tempos de serviço exponenciais** (propriedade de **falta de memória** — o tempo residual de transmissão do pacote atual é em média igual ao tempo total de serviço $S$).

##### 4. Derivação Passo a Passo (Exigida nas Provas da UFRJ)

Um pacote recém-chegado encontra, em média, $N_q$ pacotes na fila e $N_s = I$ pacotes no servidor. Pela falta de memória e pela propriedade PASTA, seu tempo médio de espera na fila $W$ é:

$$W = (N_q + N_s) \cdot S = (N_q + I) \cdot \frac{L}{R}$$

Substituindo a Lei de Little $N_q = a \cdot W$:

$$W = \left(a \cdot W + I\right) \cdot \frac{L}{R} = a \cdot W \cdot \frac{L}{R} + I \cdot \frac{L}{R} = I \cdot W + I \cdot \frac{L}{R}$$

Isolando $W$:

$$W (1 - I) = I \cdot \frac{L}{R} \quad \implies \quad W_{M/M/1} = \frac{I}{1 - I} \cdot \frac{L}{R} = \frac{I}{\mu(1 - I)}$$

Aplicando as demais métricas pela Lei de Little:

- **Tempo Total no Sistema ($T$):** $$T = W + S = \frac{I}{1 - I} \frac{L}{R} + \frac{L}{R} = \frac{1}{1 - I} \cdot \frac{L}{R} = \frac{1}{\mu - a}$$
- **Número Médio de Pacotes no Sistema ($N$):** $$N = a \cdot T = \frac{a}{\mu - a} = \frac{I}{1 - I}$$
- **Número Médio de Pacotes na Fila ($N_q$):** $$N_q = a \cdot W = \frac{I^2}{1 - I}$$

---

#### Unificação Matemática 4: O Modelo de Fila $M/D/1$ (Pacotes Fixos)

##### 1. O que representa?

Modela a fila em um roteador onde todos os pacotes têm **tamanho fixo/determinístico** de $L$ bits (serviço $D$).

##### 2. Por que estamos usando este modelo?

Para demonstrar o **efeito da variabilidade do tamanho dos pacotes** no atraso da rede.

##### 3. Hipóteses e Aplicação da Fórmula

Como todos os pacotes têm exatamente o mesmo tamanho, o tempo residual de transmissão que um pacote recém-chegado encontra no servidor é, em média, **metade do tempo de transmissão** ($S_R = \frac{S}{2} = \frac{L}{2R}$).

Repetindo a dedução da UFRJ com tempo residual $S/2$:

$$W_{M/D/1} = N_q \cdot S + I \cdot \frac{S}{2} = a W \cdot S + \frac{I \cdot S}{2} = I \cdot W + \frac{I \cdot S}{2}$$

$$W_{M/D/1} (1 - I) = \frac{I \cdot S}{2} \quad \implies \quad W_{M/D/1} = \frac{I}{2(1 - I)} \cdot \frac{L}{R} = \frac{1}{2} W_{M/M/1}$$

##### 6. Interpretação em Termos de Redes

$$W_{M/D/1} = \frac{1}{2} W_{M/M/1}$$ Padronizar o tamanho dos pacotes na rede (tornando-os determinísticos) **reduz o tempo de espera na fila exatamente pela metade** em relação a uma rede com tamanhos de pacotes altamente variáveis ($M/M/1$).

---

### 1.4.3 Perda de Pacotes (_Packet Loss_)

#### Fenômeno de Rede

Na prática, a memória do _buffer_ de um roteador é **finita**. O que acontece quando chegam pacotes e a fila já está 100% cheia?

#### Conceito

Como não há espaço físico para armazenar o pacote recebido, o roteador simplesmente o **descarta** (_packet drop_).

- **Do ponto de vista do sistema final:** O pacote foi transmitido, mas "sumiu" no núcleo da rede.
- A fração de pacotes perdidos aumenta exponencialmente conforme a intensidade de tráfego $I$ se aproxima ou excede $1$.
- Protocolos da camada de transporte confiável (como o TCP) precisam detectar essa perda e retransmitir o pacote, gerando atraso adicional para a aplicação.

---

### 1.4.4 Atraso Fim a Fim (_End-to-End Delay_)

Acumulando os atrasos nodais ao longo de um caminho com $N-1$ roteadores intermediários ($H = N$ enlaces idênticos) sem congestionamento:

$$d_{\text{fim-a-fim}} = N \cdot (d_{\text{proc}} + d_{\text{trans}} + d_{\text{prop}}) = N \left( d_{\text{proc}} + \frac{L}{R} + \frac{d}{s} \right)$$

#### Ferramenta Prática de Diagnóstico: Traceroute

O programa **Traceroute** permite medir o atraso de ida e volta (RTT) real até cada roteador ao longo do caminho enviando múltiplos pacotes com valores crescentes de TTL (_Time-To-Live_). Se um roteador não responder ou descartar pacotes devido a congestionamento, o Traceroute exibe um asterisco (`*`).

---

### 1.4.5 Vazão em Redes de Computadores (_Throughput_)

#### Fenômeno de Rede

A qual taxa efetiva (em bits por segundo) um arquivo é transferido da origem ao destino através de uma sequência de enlaces compartilhados?

#### Conceito e O Enlace Gargalo (_Bottleneck Link_)

- **Vazão Instantânea:** A taxa em um dado instante de tempo.
- **Vazão Média:** Se a transferência de um arquivo de $F$ bits leva $T$ segundos, a vazão média é $F/T \text{ bits/s}$.

---

#### Modelo Matemático: A Vazão em Enlaces em Série e Compartilhados

##### 1. Aplicação da Fórmula

Considere um caminho com $N$ enlaces em série com taxas de transmissão $R_1, R_2, \dots, R_N$. A vazão fim a fim $R_{\text{vazão}}$ é dada estritamente pela taxa do **enlace mais lento** do caminho (o **gargalo**):

$$R_{\text{vazão}} = \min{R_1, R_2, \dots, R_N}$$

```
[ Servidor ] ---( R_1 = 100 Mbps )---> [ Roteador ] ---( R_2 = 1.5 Mbps )---> [ Roteador ] ---( R_3 = 10 Mbps )---> [ Cliente ]
                                                               ↑
                                                    ENLACE GARGALO (Vazão = 1.5 Mbps)
```

#### 2. Efeito de Enlaces Compartilhados e Caching (Notas UFRJ)

Se o enlace gargalo de taxa $R$ for compartilhado por $K$ conexões simultâneas, a vazão de cada conexão é $\min\left(R_s, R_c, \frac{R}{K}\right)$.

Ao instalar um **servidor Cache (Web Cache)** próximo aos clientes com uma taxa de acerto (_hit rate_) $h$, reduzimos a taxa de chegada no enlace de acesso de $a$ para uma taxa efetiva $a_{\text{efetiva}}$:

$$a_{\text{efetiva}} = (1 - h) \cdot a$$

Isso reduz drasticamente a intensidade de tráfego $I = \frac{L \cdot a_{\text{efetiva}}}{R}$, retirando o enlace da zona de congestionamento e reduzindo o atraso de fila de segundos para milissegundos!

## 1.5 Camadas de Protocolos e Seus Modelos de Serviço

### 1.5.1 Arquitetura em Camadas (Pilhas de Protocolos)

#### Fenômeno de Rede

A Internet é um sistema composto por bilhões de dispositivos, aplicações heterogêneas, comutadores e enlaces físicos de tecnologias distintas. Como projetar e manter uma infraestrutura tão vasta sem que uma alteração em uma placa de rede ou navegador quebre todo o sistema?

#### Conceito

Para estruturar o projeto, os projetistas organizam os protocolos (e o _hardware_/_software_ que os executam) em **camadas**.

- **Abstração de Serviços:** Cada camada oferece um **modelo de serviço** bem definido para a camada imediatamente superior.
- **Encapsulamento de Funções:** Uma camada realiza suas tarefas executando ações internas e utilizando os serviços fornecidos pela camada inferior.
- **Vantagem:** Modularidade. Se o protocolo de uma camada for atualizado (por exemplo, mudando de Wi-Fi para Ethernet na camada de enlace), as camadas superiores (como a camada de aplicação) continuam funcionando sem necessidade de modificação.
- **Desvantagem / _Trade-off_:** Uma camada pode duplicar funcionalidades de camadas inferiores (por exemplo, checagem de erros no enlace e no transporte) ou precisar de informações contidas em outra camada.

---

#### A Pilha de Protocolos da Internet (5 Camadas)

A arquitetura da Internet é organizada em **5 camadas**, abordada neste curso de cima para baixo (_top-down_):

```
+-----------------------------------+
|  5. Aplicação  (Mensagem)         |  <--->  HTTP, SMTP, DNS
+-----------------------------------+
|  4. Transporte (Segmento)         |  <--->  TCP, UDP
+-----------------------------------+
|  3. Rede       (Datagrama)        |  <--->  IP, Protocolos de Roteamento
+-----------------------------------+
|  2. Enlace     (Quadro / Frame)   |  <--->  Ethernet, Wi-Fi, PPP
+-----------------------------------+
|  1. Física     (Bits)             |  <--->  Sinais elétricos / ópticos / rádio
+-----------------------------------+
```

1. **Camada de Aplicação:** Onde residem as aplicações de rede e seus protocolos (HTTP para Web, SMTP para e-mail, DNS para tradução de nomes). A unidade de dados é a **mensagem**.
2. **Camada de Transporte:** Transporta as mensagens da aplicação entre os processos dos sistemas finais. Na Internet, destaca-se o **TCP** (serviço confiável, orientado à conexão e com controle de congestionamento) e o **UDP** (serviço sem conexão, não confiável e sem controle de fluxo). A unidade de dados é o **segmento**.
3. **Camada de Rede:** Responsável por mover pacotes chamados **datagramas** de um _host_ de origem a um de destino através dos roteadores no núcleo da rede. Contém o **Protocolo IP** e as tabelas de roteamento.
4. **Camada de Enlace:** Transfere um datagrama de um nó (host ou roteador) para o nó seguinte ao longo do caminho. Exemplo: Ethernet, Wi-Fi. A unidade de dados é o **quadro** (_frame_).
5. **Camada Física:** Move os bits individuais contidos no quadro ao longo do meio físico de transmissão (fibra, cabo trançado, ar).

---

#### O Modelo de Referência OSI (7 Camadas) vs. Pilha TCP/IP

O modelo da ISO/OSI possui **7 camadas**, adicionando duas camadas entre a Aplicação e o Transporte:

- **Camada de Apresentação:** Provê serviços como formatação de dados, compressão e criptografia.
- **Camada de Sessão:** Provê delimitação e sincronização do fluxo de dados (marcação de _checkpoints_).

_Na Internet (TCP/IP), essas funções não possuem camadas dedicadas._ Se uma aplicação precisar de compressão, criptografia ou controle de sessão, o próprio desenvolvedor constrói essa funcionalidade dentro da **camada de aplicação**.

---

### 1.5.2 O Processo de Encapsulamento

#### Fenômeno de Rede

Quando você clica em um link na Web, como o texto da sua requisição HTTP é transformado em impulsos elétricos ou luz sem perder o endereço de destino?

#### Conceito

Conforme os dados descem pela pilha de protocolos no sistema emissor, cada camada anexa suas próprias informações de controle na forma de um **cabeçalho** (_header_). O pacote completo da camada superior passa a ser a **carga útil** (_payload_) da camada inferior.

```
[Dados da Aplicação M]                                   --> Mensagem (Aplicação)
[ Cabeçalho H_t | Dados M ]                              --> Segmento (Transporte)
[ Cabeçalho H_n | Cabeçalho H_t | Dados M ]              --> Datagrama (Rede)
[ Cabeçalho H_l | Cabeçalho H_n | H_t | M | Trailer T_l ] --> Quadro (Enlace)
```

---

#### Qual camada cada dispositivo da rede processa?

Nem todos os nós da rede implementam as 5 camadas da pilha:

```
[ Host Emissor ]        [ Switch L2 ]          [ Roteador L3 ]         [ Host Receptor ]
 ( 5 Camadas )          ( 2 Camadas )           ( 3 Camadas )            ( 5 Camadas )
 +-----------+                                                           +-----------+
 | Aplicação |                                                           | Aplicação |
 +-----------+                                                           +-----------+
 | Transporte|                                                           | Transporte|
 +-----------+                                  +-----------+            +-----------+
 |   Rede    |                                  |   Rede    |            |   Rede    |
 +-----------+          +-----------+           +-----------+            +-----------+
 |  Enlace   |  <-----> |  Enlace   |  <----->  |  Enlace   |  <----->   |  Enlace   |
 +-----------+          +-----------+           +-----------+            +-----------+
 |  Física   |          |  Física   |           |  Física   |            |  Física   |
 +-----------+          +-----------+           +-----------+            +-----------+
```

1. **Sistemas Finais (_Hosts_):** Processam as **5 camadas** da pilha.
2. **Roteadores (Comutadores da Camada de Rede):** Processam até a **Camada 3 (Rede)**. Eles examinam o cabeçalho IP para tomar decisões de repasse, mas não alteram nem examinam a carga útil do segmento de transporte.
3. **_Switches_ de Enlace (Camada 2):** Processam até a **Camada 2 (Enlace)**. Eles examinam endereços físicos (MAC) para repassar quadros dentro da mesma rede local.

---

## 1.6 Redes sob Ataque: Segurança de Redes

A Internet original foi projetada sob o modelo de um **grupo de usuários de confiança mútua** em uma rede transparente. Conforme se tornou a infraestrutura global da sociedade, surgiram diversas classes de ameaças maliciosas.

---

### 1.6.1 Malware: Infecção em Sistemas Finais

O _malware_ é qualquer software malicioso que entra e infecta um sistema final.

- **Vírus:** _Malware_ que exige alguma forma de interação do usuário (como executar um anexo de e-mail ou abrir um arquivo) para infectar o dispositivo.
- **Worm (Verme):** _Malware_ **autorreprodutivo** que busca ativamente outros sistemas vulneráveis na rede e se espalha de forma autônoma em velocidade exponencial, sem necessidade de ação humana.
- **Botnet:** Uma rede de milhares de dispositivos infectados (chamados de _zumbis_) controlada remotamente por um atacante para disparar e-mails de _spam_ ou ataques distribuídos de negação de serviço.

---

### 1.6.2 Ataques de Recusa de Serviço (DoS e DDoS)

Ataques de **Negação de Serviço (_Denial-of-Service - DoS_)** tornam uma rede, servidor ou infraestrutura inoperante para usuários legítimos. Dividem-se em três categorias:

1. **Ataque de Vulnerabilidade:** Envio de sequências de pacotes bem elaboradas a uma aplicação ou sistema operacional vulnerável para forçar uma falha ou parada do serviço.
2. **Inundação na Largura de Banda (_Bandwidth Flooding_):** O atacante envia uma quantidade maciça de pacotes ao servidor-alvo, tão alta que o enlace de acesso de taxa $R$ congestiona completamente, bloqueando pacotes legítimos.
3. **Inundação na Conexão (_Connection Flooding / SYN Flood_):** O atacante estabelece um grande número de conexões TCP semiabertas no servidor, esgotando sua memória e recursos de processamento.

#### DoS Distribuído (DDoS)

Se a taxa do enlace do servidor $R$ for muito grande, uma única fonte de ataque não consegue gerar tráfego suficiente para derrubá-lo. Em um **ataque DDoS**, o atacante utiliza uma **botnet** com milhares de zumbis para enviar tráfego simultâneo. A taxa agregada sobrecarrega a capacidade do alvo, tornando o ataque muito mais difícil de filtrar e conter.

---

### 1.6.3 Análise de Pacotes (_Packet Sniffing_)

Em meios de transmissão compartilhados (como redes Wi-Fi ou LANs Ethernet com hubs), um receptor passivo nas proximidades do transmissor pode obter uma cópia de todos os quadros e pacotes trafegados.

- **Características:** O analisador de pacotes (_packet sniffer_, como o software Wireshark) é passivo, ou seja, **não injeta pacotes** no canal, o que o torna extremamente difícil de ser detectado.
- **Defesa Principal:** Utilização de **criptografia** (HTTPS, TLS/SSL, IPsec) em todas as camadas para impedir que a cópia lida seja compreendida pelo bisbilhoteiro.

---

### 1.6.4 Falsificação de Identidade (_IP Spoofing_)

Como a Internet não autentica nativamente o endereço de origem no cabeçalho do pacote IP no momento da criação, um atacante pode injetar na rede um pacote contendo um **endereço IP de origem falso**.

- **Consequências:** O receptor é enganado achando que a mensagem veio de uma entidade confiável e pode executar comandos maliciosos ou enviar respostas para a vítima do IP falsificado.
- **Defesa:** Filtragem de entrada (_Ingress Filtering_ - RFC 2827) configurada no roteador do primeiro salto para descartar pacotes cujo IP de origem não pertença à sub-rede física daquela interface.

---

## 1.7 História das Redes de Computadores e da Internet

A evolução da Internet pode ser dividida em quatro fases históricas marcantes:

1. **1961–1972: A Era Pioneira da Comutação de Pacotes**
    
    - **Bases Teóricas:** Leonard Kleinrock desenvolve a teoria de filas demonstrando a eficiência da comutação de pacotes em 1961; Paul Baran e Donald Davies propõem de forma independente redes chaveadas por pacotes.
    - **ARPANET:** Em 1969, o primeiro nó da ARPANET é instalado na UCLA sob o patrocínio da DARPA. Em 1972, ocorre a primeira demonstração pública da ARPANET e o surgimento do primeiro protocolo de e-mail.
2. **1972–1980: Interconexão de Redes e Arquitetura Aberta**
    
    - **O Problema:** Redes independentes (ARPANET, ALOHANET via rádio, SATNET via satélite) não conseguiam se comunicar diretamente.
    - **Surgimento do TCP/IP:** Vinton Cerf e Robert Kahn desenvolvem os princípios da arquitetura de **interconexão de redes (_internetting_)**, definindo o protocolo TCP/IP para unificar redes heterogêneas sob uma cintura fina comum.
3. **1980–1990: Proliferação de Redes e Padronização**
    
    - Em **1 de janeiro de 1983**, o TCP/IP é oficialmente adotado como o único protocolo padrão da ARPANET.
    - Lançamento do **DNS (_Domain Name System_)** para substituir arquivos estáticos de mapeamento de nomes por um sistema hierárquico e distribuído.
    - A **NSFNET** constrói um backbone de alta velocidade interconectando supercomputadores universitários, expandindo o acesso acadêmico.
4. **1990–Presente: A Era Comercial, a Web e a Internet Moderna**
    
    - **Invenção da World Wide Web:** Tim Berners-Lee inventa o HTML, HTTP, os servidores Web e os navegadores no CERN entre 1989 e 1991.
    - **Privatização e Explosão Global:** Nos anos 90, a NSFNET desativa seu backbone comercial, dando lugar aos ISPs privados e à proliferação comercial.
    - **A Era Contemporânea:** Expansão das redes móveis (4G/5G), aparecimento de redes de distribuição de conteúdo (CDNs), redes definidas por software (SDN), nuvens e novos protocolos de transporte rápido como **HTTP/3 e QUIC**.
---
# Capítulo 2: Camada de Aplicação

A camada de aplicação é o topo da pilha de protocolos e a interface direta com o usuário final e os programas de computador. Ela permite a criação de aplicações distribuídas que se comunicam através da infraestrutura de rede sem que o desenvolvedor precise conhecer os detalhes físicos das camadas inferiores.

---
## 2.1 Princípios das Aplicações de Rede

### 2.1.1 Arquiteturas de Aplicação: Cliente-Servidor vs. Peer-to-Peer (P2P)

Ao projetar uma aplicação de rede, a primeira decisão do desenvolvedor é definir a arquitetura de comunicação entre os sistemas finais:

1. **Arquitetura Cliente-Servidor (_Client-Server_):**
    
    - **Servidor:** É um hospedeiro sempre ativo (_always-on_), com um endereço IP fixo e bem conhecido. Atende a requisições de potencialmente milhões de clientes. Para suportar altas cargas, os servidores são frequentemente organizados em _datacenters_ ou fazendas de servidores.
    - **Cliente:** É o processo que inicia a comunicação enviando uma requisição ao servidor. Os clientes podem ter endereços IP dinâmicos e não se comunicam diretamente entre si.
    - **Gargalo:** Conforme o número de clientes cresce, o enlace de _upload_ do servidor torna-se o gargalo, e o tempo de distribuição de dados cresce de forma linear.
2. **Arquitetura Peer-to-Peer (P2P):**
    
    - **Funcionamento:** Não depende de servidores dedicados sempre ativos. Duplas de hospedeiros intermitentemente conectados (**pares** ou _peers_) comunicam-se diretamente entre si.
    - **Autoescalabilidade (_Self-scalability_):** Embora cada novo par traga carga adicional ao solicitar arquivos, ele também adiciona capacidade de serviço ao sistema ao redistribuir pedaços do arquivo para outros pares.
    - **Sessão P2P (Visão de Prova UFRJ):** Em uma aplicação P2P, a afirmação de que _"não existe noção de cliente e servidor"_ é **falsa**. No contexto de uma sessão de comunicação individual entre dois pares, o processo que solicita o bloco age como **cliente** e o processo que envia o bloco age como **servidor**.

---

### 2.1.2 Comunicação entre Processos e Sockets

Um programa executado em um sistema final é um **processo**. Dois processos em _hosts_ distintos comunicam-se trocando mensagens através da rede.

#### A Interface Socket

A comunicação entre a camada de aplicação e a camada de transporte no sistema operacional ocorre por meio de uma API chamada **socket**.

- **Analogia:** O socket é a "porta de uma casa". A aplicação entrega a mensagem no socket do seu lado; a infraestrutura de transporte abaixo se encarrega de levar a mensagem até o socket do destino.
- O desenvolvedor tem controle total sobre a camada de aplicação, mas seu controle sobre a camada de transporte resume-se a: (1) escolher o protocolo de transporte (TCP ou UDP) e (2) ajustar alguns parâmetros (como tamanho de _buffers_ e portas).

#### Endereçamento de Processos

Para que uma mensagem atinja o processo correto em outro hospedeiro, são necessárias duas informações essenciais:

1. **Endereço IP (32 bits no IPv4 / 128 bits no IPv6):** Identifica univocamente o _host_ de destino na rede global.
2. **Número de Porta (_Port Number_, 16 bits):** Identifica o processo/aplicação específico no _host_ de destino.
    - Exemplo de portas padronizadas (_Well-Known Ports_):
        - **HTTP (Web):** Porta `80`
        - **HTTPS (Web Segura):** Porta `443`
        - **SMTP (E-mail):** Porta `25`
        - **DNS (Nomes):** Porta `53`

---

### 2.1.3 Requisitos de Transporte Exigidos pelas Aplicações

Diferentes aplicações possuem necessidades distintas quanto ao serviço fornecido pela camada de transporte:

1. **Confiabilidade e Integridade de Dados (_Data Loss_):**
    
    - _Aplicações tolerantes a perdas:_ Áudio e vídeo em tempo real ou jogos _online_ toleram uma pequena porcentagem de pacotes perdidos sem comprometer criticamente a experiência do usuário.
    - _Aplicações sensíveis à perda:_ Transferência de arquivos (FTP), e-mail, transações bancárias e texto Web exigem entrega 100% confiável e sem erros.
2. **Vazão (_Throughput_):**
    
    - _Aplicações sensíveis à largura de banda:_ _Streaming_ de vídeo em alta definição exige taxas de bits mínimas garantidas para evitar travamentos.
    - _Aplicações elásticas:_ E-mail, navegação Web e transferência de arquivos utilizam a largura de banda que estiver disponível no momento.
3. **Temporização (_Timing_ / Latência):**
    
    - Aplicações interativas em tempo real (telefonia IP, jogos multijogador) exigem garantias de baixos atrasos fim a fim (por exemplo, entrega de bits em menos de 100 ms) para evitar pausas artificiais na conversação.
4. **Segurança:**
    
    - Criptografia de dados de ponta a ponta, integridade de mensagem e autenticação das partes comunicantes.

---

### 2.1.4 Serviços de Transporte Fornecidos pela Internet: TCP vs. UDP

A camada de transporte da Internet oferece dois protocolos principais para as aplicações:

|Propriedade de Transporte|**TCP** (_Transmission Control Protocol_)|**UDP** (_User Datagram Protocol_)|
|:--|:--|:--|
|**Orientação à Conexão**|**Orientado à Conexão**: Exige o _handshake_ de três vias antes da troca de dados.|**Sem Conexão (_Stateless_)**: Envia datagramas sem estabelecimento de conexão prévia.|
|**Confiabilidade**|**Garantida**: Entrega ordenada e sem perdas (_Byte-stream_) por ACKs e retransmissões.|**Não Confiável**: Pacotes podem ser perdidos, duplicados ou chegar fora de ordem.|
|**Controle de Fluxo/Congestionamento**|**Sim**: Adapta a taxa de envio para não afogar o receptor nem sobrecarregar os roteadores.|**Não**: Envia na taxa que a aplicação injetar no socket.|
|**Garantia de Vazão/Delay**|**Não**: Não oferece garantias mínimas de banda ou limite máximo de atraso.|**Não**: Não oferece garantias mínimas de banda ou limite máximo de atraso.|
|**Sobrecarga (_Overhead_)**|Maior (cabeçalho de 20 bytes + latência de _handshake_).|Mínima (cabeçalho leve de 8 bytes, transmissão imediata).|
|**Uso Típico**|Web (HTTP), E-mail (SMTP), Transferência de Arquivos.|DNS (consultas rápidas), Streaming de Vídeo/Áudio em Tempo Real, VoIP.|

---
