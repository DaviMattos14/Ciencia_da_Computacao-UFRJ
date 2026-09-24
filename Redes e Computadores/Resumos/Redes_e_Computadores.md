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

##### Onde fica o estado da conexão? (Pegadinha clássica de prova)

- Na **comutação de circuitos**, cada comutador **ao longo de todo o caminho** (ou seja, no **núcleo** da rede, não só nas pontas) precisa armazenar um registro de estado da conexão — qual faixa de frequência ou qual _slot_ de tempo está reservado para aquela chamada. É esse estado guardado nos comutadores do núcleo que permite a reserva dedicada de recursos.
- Na **comutação de pacotes** (Internet), **nenhum estado de fluxo/conexão é mantido nos roteadores do núcleo**: cada pacote é tratado de forma independente ("sem memória" de pacotes anteriores). Isso é o que torna a arquitetura simples e escalável, mas também é a razão pela qual a rede não garante taxa de banda nem atraso máximo.
- Cuidado: alguma noção de "estado de conexão" (como no TCP) existe, mas ela fica armazenada **nos sistemas finais (hosts)**, na borda da rede — nunca nos roteadores do núcleo.

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

## 2.2 A Web e o HTTP

---

### 1. O Conceito de HTTP e a Semântica Sem Estado (_Stateless_)

#### Fenômeno de Rede

Quando um usuário navega pela Web, ele requisita arquivos HTML, imagens JPEG, arquivos CSS e scripts JS espalhados por servidores na rede.

#### Conceito

O **HTTP (_Hypertext Transfer Protocol_)** é o protocolo da camada de aplicação que governa a comunicação Web. Ele opera segundo a arquitetura **Cliente-Servidor**:

- **Navegador (Cliente):** Envia mensagens de requisição HTTP (_HTTP Request_) solicitando objetos.
- **Servidor Web:** Recebe a requisição, localiza o objeto e devolve uma mensagem de resposta (_HTTP Response_) contendo o objeto solicitado.

##### A Propriedade _Stateless_ (Sem Estado)

O HTTP é um **protocolo sem estado (_stateless_)**. O servidor Web atende às requisições do cliente sem armazenar informações sobre requisições anteriores feitas por aquele mesmo usuário.

- **Vantagem:** Simplifica drasticamente o projeto do servidor, permitindo que ele atenda a milhões de requisições simultâneas sem consumir memória para manter o histórico de cada cliente.
- **Contorno da Limitação:** Para aplicações que exigem estado (como carrinhos de compras e sessões de login), a camada de aplicação utiliza **cookies** e dados de sessão.

---

### 2. A Definição do RTT e o _Three-Way Handshake_ do TCP

Para calcular quanto tempo leva para carregar uma página Web, precisamos quantificar o tempo de viagem de um pacote de ida e volta na rede.

---

#### Modelo Matemático: O RTT e a Abertura de Conexão TCP

#### 1. O que representa?

- **RTT (_Round-Trip Time_):** O tempo necessário para um pequeno pacote viajar do cliente ao servidor e retornar ao cliente.
- **Composição do RTT:** O RTT inclui a soma de todos os atrasos físicos do caminho: atrasos de propagação nos enlaces, atrasos de fila nos roteadores e atrasos de processamento.

##### 2. Por que estamos usando este modelo?

O HTTP não transporta dados diretamente pelo meio físico; ele utiliza o protocolo **TCP** na camada de transporte para garantir uma entrega confiável. Antes de enviar o primeiro `GET` HTTP, o cliente precisa obrigatoriamente estabelecer uma conexão TCP via **Apresentação de Três Vias (_Three-Way Handshake_)**.

##### 3. Aplicação do Modelo de Conexão

1. **Passo 1 (SYN):** Cliente envia um segmento TCP SYN ao servidor.
2. **Passo 2 (SYN/ACK):** Servidor responde com um segmento TCP SYN/ACK. _(Estes dois passos consomem exatos **1 RTT**)._
3. **Passo 3 (ACK + GET):** O cliente envia o ACK de confirmação combinado com a mensagem de requisição `HTTP GET`.
4. **Passo 4 (Resposta):** O servidor processa o pedido e envia o arquivo HTML/Objeto de volta. _(A requisição e a recepção do objeto consomem mais **1 RTT**)._

##### 4. Interpretação em Termos de Latência Web

A transferência do primeiro arquivo de uma página Web (o HTML base) exige, no mínimo:

$$T_{\text{base}} = 2 \text{ RTT} + t_{\text{transmissão}}$$

onde **1 RTT** é gasto no _handshake_ TCP e **1 RTT** é gasto na requisição/resposta HTTP.

---

### 3. Os 4 Modelos de Conexão HTTP e a Análise Matemática de Latência (Kurose + UFRJ)

#### Fenômeno de Rede

Uma página Web moderna raramente possui apenas um arquivo HTML; ela contém um arquivo HTML base e **$n$ objetos referenciados** (imagens, vídeos, scripts) no mesmo servidor. Como o navegador deve organizar o transporte desses $n$ objetos pela rede?

Combinando as opções de **Persistência** da conexão TCP com o **Paralelismo** do navegador, surgem 4 modelos clássicos de transporte analisados na UFRJ:

---

#### Modelo 1: HTTP Não Persistente Sem Paralelismo (HTTP/1.0 Padrão)

##### 1. Funcionamento

A conexão TCP é aberta para transferir um único objeto e **imediatamente fechada** após a entrega. Os $n$ objetos referenciados são baixados estritamente em série.

##### 2. Análise Matemática do Tempo Total

Para o arquivo-base HTML e os $n$ objetos referenciados:

- O HTML base custa $2 \text{ RTT}$ (1 RTT para TCP + 1 RTT para HTTP).
- Cada um dos $n$ objetos exige uma nova conexão TCP, custando $2 \text{ RTT}$ cada.

$$T_{\text{não-persistente, em série}} = 2 \text{ RTT} + 2n \text{ RTT} = 2(n + 1) \text{ RTT}$$

_(desprezando o tempo de transmissão de objetos pequenos)._

##### 3. Avaliação de Desempenho

- **Vantagens:** O servidor libera memórias e descritores de _sockets_ rapidamente assim que entrega o objeto, sendo mais simples e resiliente contra ataques de conexões presas.
- **Desvantagens:** Pior desempenho de latência. O cliente paga o custo de $1 \text{ RTT}$ de _handshake_ repetidamente para cada imagem pequena da página.

---

#### Modelo 2: HTTP Não Persistente Com Paralelismo

##### 1. Funcionamento

O navegador abre **múltiplas conexões TCP independentes e simultâneas** (geralmente até $k = 6$) para baixar os $n$ objetos em paralelo.

##### 2. Análise Matemática do Tempo Total

- O HTML base custa $2 \text{ RTT}$.
- Assumindo paralelismo perfeito (onde as conexões simultâneas baixam os objetos ao mesmo tempo), os RTTs dos $n$ objetos são sobrepostos.

$$T_{\text{não-persistente, paralelo}} = 2 \text{ RTT (HTML)} + 2 \text{ RTT (Objetos em paralelo)} = 4 \text{ RTT}$$

##### 3. Avaliação de Desempenho

- **Vantagens:** Redução drástica no tempo de carregamento perceptível.
- **Desvantagens:** Consumo massivo de recursos no servidor, que precisa processar múltiplos _handshakes_ e manter vários _sockets_ abertos simultaneamente para o mesmo cliente.

---

#### Modelo 3: HTTP Persistente Sem Paralelismo (HTTP/1.1 Padrão / _Pipelining_)

##### 1. Funcionamento

O servidor **deixa a conexão TCP aberta** após enviar a resposta do HTML. Os $n$ objetos subsequentes são solicitados através da **mesma conexão TCP** já estabelecida.

##### 2. Análise Matemática do Tempo Total

- O HTML base custa $2 \text{ RTT}$ (1 RTT TCP + 1 RTT HTTP).
- Como o TCP já está aberto, cada um dos $n$ objetos subsequentes custa apenas **1 RTT** (apenas o pedido/resposta HTTP).

$$T_{\text{persistente, em série}} = 2 \text{ RTT} + n \text{ RTT} = (n + 2) \text{ RTT}$$

##### 3. Avaliação de Desempenho

- **Vantagens:** Economiza $1 \text{ RTT}$ de _handshake_ por objeto e poupa CPU e memória do servidor ao evitar a criação/destruição contínua de _sockets_.
- **Desvantagens:** O servidor precisa gerenciar _timeouts_ de conexões ociosas. Continua sujeito ao **bloqueio de cabeça de fila (_Head-of-Line Blocking_)**.

---

#### Modelo 4: HTTP Persistente Com Paralelismo (Web Moderna)

##### 1. Funcionamento

O cliente **reaproveita a conexão TCP persistente existente** para enviar requisições sequenciais, mas **abre uma nova conexão TCP em paralelo** para acelerar objetos adicionais simultaneamente.

##### 2. Análise Matemática do Tempo Total

- O HTML base e o objeto reusado na conexão 1 custam $2 \text{ RTT} + 1 \text{ RTT}$.
- A nova conexão paralela aberta para o objeto 2 custa $2 \text{ RTT}$.
- O tempo total da fase de objetos é o máximo entre as vias paralelas:

$$T_{\text{persistente, paralelo}} = 2 \text{ RTT (HTML)} + \max(1 \text{ RTT}, 2 \text{ RTT}) = 4 \text{ RTT}$$

---

#### Tabela Resumo dos Modelos de Conexão HTTP (UFRJ)

| Modelo de Conexão                   | Conexões TCP Abertas               | Fórmula do Tempo Total (para $n$ objetos) | Vantagem Principal                            | Desvantagem Principal                         |
| :---------------------------------- | :--------------------------------- | :------------------------------------------ | :-------------------------------------------- | :-------------------------------------------- |
| **Não Persistente Sem Paralelismo** | $n + 1$ conexões (1 por vez)     | $2(n + 1) \text{ RTT}$                    | Liberação rápida de recursos no servidor.     | Altíssima latência (paga RTT TCP para tudo).  |
| **Não Persistente Com Paralelismo** | $n + 1$ conexões (várias juntas) | $4 \text{ RTT}$                           | Carregamento muito rápido.                    | Sobrecarga severa de CPU/sockets no servidor. |
| **Persistente Sem Paralelismo**     | 1 única conexão TCP                | $(n + 2) \text{ RTT}$                     | Economiza RTTs de TCP e recursos no servidor. | Sofre com Head-of-Line (HOL) Blocking.        |
| **Persistente Com Paralelismo**     | Múltiplas conexões mantidas        | $4 \text{ RTT}$                           | Equilíbrio entre paralelismo e reuso de TCP.  | Alto número de conexões mantidas ociosas.     |

---

### 4. O Bloqueio de Cabeça de Fila (HOL Blocking) e a Evolução do HTTP (HTTP/1.1 $\to$ HTTP/2 $\to$ HTTP/3)

#### Fenômeno de Rede

No HTTP/1.1 com conexão persistente única, as requisições são atendidas na ordem de chegada (FCFS: _First-Come, First-Served_). Se o cliente solicitar um arquivo gigante (ex: um vídeo) seguido por três imagens pequenas, o que acontece?

---

#### Modelo Matemático: O Custo do Bloqueio HOL (UFRJ / Kurose)

##### 1. Aplicação do Cálculo

Suponha que um objeto grande $O_1$ leve **10 unidades de tempo** para ser transmitido e três objetos pequenos ($O_2, O_3, O_4$) levem **1 unidade de tempo** cada.

- **Cenário A: Atendimento FCFS (Objeto Grande Primeiro - HTTP/1.1)**
    
    - Instante de conclusão de $O_1$: $t = 10$.
    - Instante de conclusão de $O_2$: $t = 10 + 1 = 11$.
    - Instante de conclusão de $O_3$: $t = 11 + 1 = 12$.
    - Instante de conclusão de $O_4$: $t = 12 + 1 = 13$.
    - **Tempo Médio de Conclusão Percebido:** $$\bar{T}_{\text{HOL}} = \frac{10 + 11 + 12 + 13}{4} = \frac{46}{4} = 11{,}5 \text{ unidades}$$
- **Cenário B: Atendimento Reordenado/Intercalado (Objetos Pequenos Primeiro)**
    
    - Instante de conclusão de $O_2$: $t = 1$.
    - Instante de conclusão de $O_3$: $t = 2$.
    - Instante de conclusão de $O_4$: $t = 3$.
    - Instante de conclusão de $O_1$: $t = 3 + 10 = 13$.
    - **Tempo Médio de Conclusão Percebido:** $$\bar{T}_{\text{otimizado}} = \frac{1 + 2 + 3 + 13}{4} = \frac{19}{4} = 4{,}75 \text{ unidades}$$

##### 2. Interpretação em Termos de Redes

O arquivo grande termina no exato mesmo instante ($t = 13$) em ambos os cenários. No entanto, reordenar/intercalar a transmissão reduz o tempo médio de espera do usuário de **11,5 para 4,75 (uma redução de mais de 58%)** sem adicionar 1 bps de largura de banda à rede!

---

#### Solução Tecnológica nas Versões do HTTP

1. **HTTP/2 (Padronizado em 2015):**
    
    - **Intercalação de Quadros (_Frame Interleaving_):** Divide os objetos em quadros pequenos e intercala sua transmissão na mesma conexão TCP. O vídeo grande não bloqueia mais as imagens pequenas.
    - **Problema Residual:** Como o HTTP/2 ainda roda sobre uma **única conexão TCP**, se um único pacote for perdido na rede, o TCP paralisa a entrega de **todos os quadros** até retransmitir o segmento perdido (Bloqueio HOL no nível de Transporte).
2. **HTTP/3 (Padronizado via QUIC):**
    
    - Substitui o TCP subjacente pelo protocolo **QUIC (que opera sobre UDP)**.
    - O QUIC implementa fluxos de dados independentes e criptografados. Se um pacote de uma imagem for perdido, apenas aquele fluxo sofre retransmissão; todos os outros fluxos continuam fluindo sem nenhum bloqueio!

---

### 5. Caches Web (_Proxy Servers_) e o GET Condicional

#### Fenômeno de Rede

Como reduzir a latência percebida pelo usuário e evitar o estrangulamento de um enlace de acesso saturado sem precisar gastar fortunas aumentando a largura de banda física?

#### Conceito

Um **Cache Web (Servidor Proxy)** é um nó de rede instalado na LAN local que atende a requisições HTTP em nome do servidor de origem.

- **Dualidade Papel:** O cache age simultaneamente como **servidor** (para os navegadores locais) e como **cliente** (em relação aos servidores de origem na Internet).

---

#### Unificação Matemática: O Impacto do Cache no Atraso Médio (Notas UFRJ)

##### 1. Aplicação do Cálculo

Considere uma rede institucional onde a taxa de acerto do cache (_Hit Rate_) é $p_{\text{hit}} = 0{,}40$ (40% das requisições são servidas localmente em $T_{\text{cache}} = 10\text{ ms}$). As 60% restantes ($p_{\text{miss}} = 0{,}60$) precisam atravessar a Internet e sofrem um atraso total de $T_{\text{Internet}} = 2{,}01\text{ s}$.

O **Atraso Médio Total de Resposta** é a média ponderada:

$$T_{\text{médio}} = p_{\text{hit}} \cdot T_{\text{cache}} + (1 - p_{\text{hit}}) \cdot T_{\text{Internet}}$$

$$T_{\text{médio}} = 0{,}40 \cdot (0{,}010\text{ s}) + 0{,}60 \cdot (2{,}010\text{ s}) = 0{,}004 + 1{,}206 = 1{,}21\text{ segundo}$$

##### 2. Interpretação em Termos de Redes

Além de cortar a latência média de mais de 2 segundos para 1,21 segundo, o cache reduz a carga no enlace de acesso em 40% ($a_{\text{efetiva}} = 0{,}60 \cdot a$). Isso retira a intensidade de tráfego $I$ da zona de saturação (onde $I \to 1$) e estabiliza as filas do roteador.

---

#### O Mecanismo do GET Condicional (`304 Not Modified`)

Para evitar que o cache entregue uma cópia local desatualizada de um arquivo que sofreu alterações no servidor de origem, o HTTP utiliza o **GET Condicional**:

```
[ Cliente ]  ---> (GET /fig.png) ---> [ Cache Web ]  ---(GET com If-Modified-Since)---> [ Servidor Origem ]
                                      [ Local ]  <--- (304 Not Modified) ------- [ Servidor Origem ]
[ Cliente ]  <--- (200 OK + Dados) -- [ Cache Web ]
```

1. Quando o cache armazena um objeto, ele salva a data enviada no cabeçalho `Last-Modified:` do servidor.
2. Quando outro cliente pede o mesmo objeto, o cache envia uma requisição de validação contendo o cabeçalho: `If-Modified-Since: <Data da Cópia Local>`
3. **Se o objeto NÃO foi modificado:** O servidor responde com o código de status **`304 Not Modified`** com um **corpo de mensagem completamente vazio**.
4. **Resultado:** Economiza-se 100% da largura de banda do arquivo e o cache entrega imediatamente a sua cópia local.

---

## 2.3 Correio Eletrônico na Internet: SMTP, POP3, IMAP e Webmail

### 2.3.1 Arquitetura do Sistema de E-mail

#### Fenômeno de Rede

Ao contrário da navegação Web, onde a comunicação ocorre em tempo real entre o navegador do usuário e o servidor Web, o correio eletrônico é um sistema de **comunicação assíncrona**. O remetente envia a mensagem mesmo que o destinatário esteja _offline_.

#### Conceito

A arquitetura de e-mail é composta por três elementos fundamentais:

```
[ Agente de Usuário A ]                    [ Agente de Usuário B ]
    (User Agent)                               (User Agent)
         |                                          ^
   (SMTP / Push)                              (POP3/IMAP / Pull)
         v                                          |
[ Servidor de E-mail ]  ===(SMTP / Push)===>  [ Servidor de E-mail ]
     (Remetente)                                (Destinatário)
```

1. **Agentes de Usuário (_User Agents - UA_):** Softwares que permitem ao usuário ler, responder, criar e organizar mensagens (ex: Outlook, Thunderbird ou a interface do Gmail).
2. **Servidores de Correio (_Mail Servers_):** O coração da infraestrutura. Cada usuário possui uma **caixa de correio (_mailbox_)** localizada em seu servidor de e-mail.
    - **Fila de Mensagens (_Message Queue_):** Se o servidor do remetente não conseguir entregar uma mensagem imediatamente ao servidor do destinatário, a mensagem é mantida em uma fila para retentativas periódicas (ex: a cada 30 minutos). Se após alguns dias a entrega falhar, ela é devolvida com mensagem de erro (_bounce_).
3. **Protocolo SMTP (_Simple Mail Transfer Protocol_):** O protocolo padrão da camada de aplicação para transferência de e-mails entre servidores de correio.

---

### 2.3.2 O Protocolo SMTP vs. HTTP

#### Funcionamento do SMTP

- Opera sobre a camada de transporte usando **TCP na porta 25**.
- É um protocolo orientado a texto simples (comandos ASCII e códigos de resposta de 3 dígitos).
- A transferência de uma mensagem ocorre em três fases: **Handshake**, **Transferência de Dados** e **Encerramento**.
- O fim do corpo da mensagem é sinalizado por uma linha contendo estritamente um **ponto único (`.`)**.

---

#### Análise Comparativa: SMTP vs. HTTP (Tema Recorrente de Prova)

| Critério                     | **HTTP**                                                                                      | **SMTP**                                                                                                         |
| :--------------------------- | :-------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Mecanismo de Comunicação** | **Protocolo _Pull_ (Puxar):** O cliente puxa/solicita dados hospedados no servidor.           | **Protocolo _Push_ (Empurrar):** O servidor do remetente empurra/envia os dados para o servidor do destinatário. |
| **Estrutura de Dados**       | Cada objeto (texto, imagem, vídeo) é empacotado em sua **própria mensagem de resposta HTTP**. | Todos os componentes do e-mail são codificados e combinados em uma **única mensagem composta**.                  |
| **Formato das Mensagens**    | Suporta nativamente dados binários e qualquer tipo de mídia no corpo.                         | Restrito historicamente ao formato ASCII de 7 bits (exigindo extensões MIME para anexos binários).               |
| **Porta Padrão TCP**         | Porta `80` (HTTP) / `443` (HTTPS).                                                            | Porta `25`.                                                                                                      |

---

### 2.3.3 Protocolos de Acesso ao Correio (_Mail Access Protocols_)

#### Fenômeno de Rede

Por que o destinatário não usa o SMTP para baixar os e-mails do seu próprio servidor de correio para o seu computador?

#### Conceito

O SMTP é um protocolo **exclusivamente _Push_** (utilizado para empurrar mensagens do remetente até o servidor do destino). Para puxar (_Pull_) os e-mails armazenados na sua caixa de correio no servidor para o seu dispositivo local, utilizam-se **Protocolos de Acesso ao Correio**:

1. **POP3 (_Post Office Protocol - Version 3_):**
    
    - Protocolo extremamente simples (porta TCP 110).
    - **Modo "Baixar e Apagar" (_Download-and-Delete_):** O agente de usuário baixa as mensagens para a máquina local e o servidor as apaga.
    - **Modo "Baixar e Manter" (_Download-and-Keep_):** O usuário baixa as mensagens, mas mantém cópias no servidor.
    - **Limitação:** É um protocolo **sem estado (_stateless_)** entre sessões. Se o usuário criar pastas ou marcar e-mails como lidos em uma máquina, essas alterações não se refletem em outros dispositivos.
2. **IMAP (_Internet Message Access Protocol_):**
    
    - Protocolo muito mais complexo e robusto (porta TCP 143).
    - **Mantém o Estado (_Stateful_):** Associa cada mensagem a uma pasta e mantém a árvore de diretórios centralizada no servidor.
    - Permite que o usuário crie pastas, busque mensagens por palavra-chave no servidor e baixe apenas partes da mensagem (ex: ler o cabeçalho sem baixar um anexo de 50 MB). Ideal para acesso por múltiplos dispositivos (_smartphone_, notebook, tablet).
3. **Correio Baseado na Web (Webmail):**
    
    - O usuário utiliza um navegador Web comum (HTTP/HTTPS) para se comunicar com o servidor de e-mail.
    - A comunicação entre o navegador e o servidor do provedor ocorre via **HTTP**.
    - A comunicação entre os servidores de e-mail na Internet continua ocorrendo estritamente via **SMTP**.

---

## 2.4 DNS: O Serviço de Diretório da Internet (_Domain Name System_)

---

### 2.4.1 O que é o DNS e Por que Roda na Borda da Rede?

#### Fenômeno de Rede

Os seres humanos preferem identificar recursos na rede usando nomes mnemônicos e alfanuméricos fáceis de memorizar (como `www.ufrj.br`). No entanto, os roteadores no núcleo da rede processam pacotes examinando endereços IP numéricos de tamanho fixo (como `146.164.220.1`).

#### Conceito

O **DNS (_Domain Name System_)** é um banco de dados distribuído e hierárquico que provê a **tradução de nomes de domínio em endereços IP** (e vice-versa).

##### A Filosofia da Arquitetura do DNS

O DNS é um protocolo da **Camada de Aplicação**. Por que a função essencial de traduzir endereços de rede foi projetada na camada de aplicação e não dentro do núcleo da rede (na camada IP)?

- **Princípio de Projeto da Internet (_End-to-End Principle_):** Manter o núcleo da rede (_routers_) o mais simples, rápido e enxuto possível, deixando a complexidade do banco de dados de nomes para os sistemas finais na borda (_edge_).

---

### 2.4.2 Arquitetura Hierárquica e Distribuída do DNS

Se o DNS fosse implementado como um **único servidor centralizado** no mundo, o sistema sofreria com:

1. **Ponto Único de Falha:** Se o servidor caísse, toda a Internet global parava.
2. **Volume Insuportável de Tráfego:** Bilhões de requisições por segundo congestionariam o enlace desse servidor.
3. **Distância Geográfica:** Consultas vindas do outro lado do mundo sofreriam com altíssimos atrasos de propagação.

Por isso, o DNS é estruturado como uma **árvore hierárquica distribuída**:

```
                              [ Servidores Raiz (Root DNS) ]
                                            |
                 +--------------------------+--------------------------+
                 |                                                     |
    [ Servidores TLD (.br) ]                               [ Servidores TLD (.com) ]
                 |                                                     |
[ Servidor Autoritativo (ufrj.br) ]                   [ Servidor Autoritativo (google.com) ]
```

1. **Servidores Raiz (_Root DNS Servers_):** Existem 13 endereços IP lógicos de servidores raiz no mundo (replicados geograficamente por centenas de servidores físicos usando _Anycast_). Eles fornecem os endereços IP dos servidores TLD.
2. **Servidores de Domínio de Nível Superior (_Top-Level Domain - TLD_):** Responsáveis por domínios genéricos (`.com`, `.org`, `.edu`) e domínios de código de país (`.br`, `.uk`, `.fr`).
3. **Servidores Autoritativos (_Authoritative DNS Servers_):** Mantidos por organizações ou provedores. Contêm os registros DNS oficiais que mapeiam os nomes de hospedeiros daquela organização para seus IPs.
4. **Servidor DNS Local (_Local Name Server / Resolver_):** Não pertence estritamente à hierarquia, mas é fundamental. Cada ISP (ou rede universitária) possui um servidor DNS local. Quando um host faz uma consulta DNS, a requisição vai primeiramente para o seu DNS local, que atua como um intermediário/proxy resolvendo a cadeia.

---

### 2.4.3 Resolução de Nomes e Análise de RTTs: Iterativa vs. Recursiva (Kurose + UFRJ)

#### Fenômeno de Rede

Quando seu computador quer acessar `www.ufrj.br`, como o Servidor DNS Local descobre o IP final caso não o tenha em memória?

Exemplo com 4 RTTs em Resolução Iterativa.

```
[ Host ] ---> (1. Consulta) ---> [ DNS Local ] ---> (2. Consulta) ---> [ Raiz ]
                                 [ DNS Local ] <--- (3. Ref: TLD) <--- [ Raiz ]
                                 [ DNS Local ] ---> (4. Consulta) ---> [ TLD .br ]
                                 [ DNS Local ] <--- (5. Ref: Auth) <-- [ TLD .br ]
                                 [ DNS Local ] ---> (6. Consulta) ---> [ Autoritativo ufrj.br ]
                                 [ DNS Local ] <--- (7. Resposta) <--- [ Autoritativo ufrj.br ]
[ Host ] <--- (8. IP Final) ---- [ DNS Local ]
```

---

#### Unificação Matemática: Modelo de Latência por RTTs na Resolução DNS

##### 1. Resolução Iterativa (Padrão da Internet)

Na consulta **iterativa**, o servidor consultado responde com o endereço do próximo servidor da hierarquia que deve ser consultado (_"Eu não sei o IP, mas pergunte ao servidor X"_).

- **Análise de RTTs:**
    - Host $\to$ DNS Local: **1 RTT** (geralmente na rede local).
    - DNS Local $\to$ Servidor Raiz: **1 RTT**.
    - DNS Local $\to$ Servidor TLD (`.br`): **1 RTT**.
    - DNS Local $\to$ Servidor Autoritativo (`ufrj.br`): **1 RTT**.
- **Atraso Total sem Cache:** $$T_{\text{iterativo}} = \text{RTT}_{\text{local}} + \text{RTT}_{\text{raiz}} + \text{RTT}_{\text{TLD}} + \text{RTT}_{\text{auth}} \approx 4 \text{ RTTs}$$

##### 2. Resolução Recursiva

Na consulta **recursiva**, o nó consultado assume a responsabilidade de contatar o nó seguinte e só devolve a resposta quando obtiver o IP final.

- **Carga:** Sobrecarrega os servidores dos níveis superiores da hierarquia (especialmente os servidores Raiz), e por isso é **desabilitada por padrão** nos servidores raiz e TLDs por questões de segurança e desempenho.

---

### 2.4.4 Registros de Recursos (_Resource Records - RRs_)

O banco de dados do DNS armazena suas informações em registros de quatro campos no formato:

$$(\text{Name}, \text{Value}, \text{Type}, \text{TTL})$$

O campo **Type** define o significado dos campos `Name` e `Value`:

1. **Tipo A (_Address_):** Mapeia um nome de host para um endereço IPv4.
    - `(aulas.ufrj.br, 146.164.220.1, A, 86400)`
2. **Tipo NS (_Name Server_):** Especifica o nome do servidor DNS autoritativo responsável pelo domínio.
    - `(ufrj.br, dns.ufrj.br, NS, 86400)`
3. **Tipo CNAME (_Canonical Name_):** Mapeia um alias/apelido para seu nome canônico (verdadeiro).
    - `(server1.ufrj.br, webserver-prod-01.ufrj.br, CNAME, 86400)`
4. **Tipo MX (_Mail Exchange_):** Mapeia o domínio para o nome do servidor de correio responsável por receber e-mails daquele domínio.
    - `(ufrj.br, mail.ufrj.br, MX, 86400)`

---

### 2.4.5 Caching DNS e a Escolha do Transporte: UDP vs. TCP (UFRJ)

#### Caching DNS

Para reduzir drasticamente o tempo de resposta e o tráfego nos servidores Raiz/TLD, os servidores DNS locais armazenam em **cache** os mapeamentos aprendidos.

- O campo **TTL (_Time to Live_)** especifica após quantos segundos a entrada expira e deve ser descartada do cache para garantir a consistência de dados alterados.

---

#### Unificação Matemática: Por que o DNS usa UDP por padrão e TCP como Exceção? (Tema Chave de Prova)

##### 1. Uso do UDP (Porta 53) — Consultas Padrão

- **Fenômeno:** Uma consulta DNS típica (pergunta por um IP) exige uma mensagem pequena de requisição e uma resposta enxuta.
- **Análise de Latência:**
    - Se o DNS utilizasse **TCP**, cada tradução de nome exigiria o _handshake_ de 3 vias do TCP (1 RTT) antes mesmo de enviar a pergunta DNS. A resolução DNS sem cache custaria no mínimo **$2 \times 4 = 8 \text{ RTTs}$**!
    - Com **UDP**, o cliente envia o datagrama direto. A consulta custa apenas **1 RTT por salto**, tornando a navegação Web instantânea.
- **Economia de Recursos:** Servidores DNS recebem bilhões de requisições. Usar UDP evita manter blocos de controle de conexão TCP (_Sockets_) em memória no servidor.

##### 2. Uso do TCP (Porta 53) — Exceção / Transferência de Zona

- **Fenômeno:** Quando a resposta DNS excede o tamanho máximo de um datagrama UDP padrão (**512 bytes**) ou quando dois servidores autoritativos sincronizam todo o seu banco de dados (**Transferência de Zona / _Zone Transfer_**).
- **Por que mudar para TCP?** Transferir bancos de dados inteiros exige a garantia de entrega confiável, sem perdas, sem corrupção e com ordenação correta, justificando o uso do TCP.
Vamos concluir o **Capítulo 2: Camada de Aplicação**, cobrindo as Seções **2.5 (Distribuição P2P)**, **2.6 (Streaming de Vídeo DASH e CDNs)** e **2.7 (Programação com Sockets)**.

Sempre que a modelagem matemática e os exercícios de prova da UFRJ aprofundarem o texto do Kurose & Ross, unificaremos o conteúdo através da nossa cadeia analítica (**fenômeno de rede → conceito → modelo → matemática → cálculo → interpretação**).

---
## 2.5 Distribuição de Arquivos P2P e o Protocolo BitTorrent

---

### 1. O Fenômeno da Distribuição Massiva de Arquivos

#### Fenômeno de Rede

Quando uma empresa lança uma atualização de sistema operacional ou um vídeo em alta definição de **$F$ bits** e **$N$ usuários** tentam baixá-lo ao mesmo tempo, como a infraestrutura de rede responde?

#### Conceito: Arquitetura Cliente-Servidor vs. P2P

- **Na Arquitetura Cliente-Servidor:** O servidor é a única fonte geradora de bits. Conforme o número de clientes $N$ cresce, a taxa de upload do servidor ($u_s$) torna-se um gargalo severo.
- **Na Arquitetura Peer-to-Peer (P2P):** Os sistemas finais (**pares** ou _peers_) atuam simultaneamente como clientes (consumindo bits) e servidores (redistribuindo bits que já baixaram). O sistema possui **autoescalabilidade (_self-scalability_)**: cada novo par traz uma nova carga de consumo, mas também adiciona capacidade de upload ao sistema.

---

### 2. Unificação Matemática: Modelo do Tempo Mínimo de Distribuição (Kurose + UFRJ)

Para comparar quantitativamente o tempo necessário para distribuir um arquivo de tamanho $F$ para $N$ clientes entre as duas arquiteturas, define-se o modelo sob as seguintes variáveis:

- $F$: Tamanho do arquivo a ser distribuído (em **bits**).
- $N$: Número de clientes/pares que desejam obter a cópia do arquivo.
- $u_s$: Taxa de upload do servidor de origem (em **bits/s**).
- $u_i$: Taxa de upload do $i$-ésimo par (em **bits/s**).
- $d_i$: Taxa de download do $i$-ésimo par (em **bits/s**).
- $d_{\text{min}} = \min{d_1, d_2, \dots, d_N}$: Taxa de download do par mais lento da rede.

---

#### Modelo Matemático 1: Tempo de Distribuição na Arquitetura Cliente-Servidor ($D_{\text{CS}}$)

##### 1. Dedução dos Limites Inferiores

Nenhum par ajuda a redistribuir o arquivo. O tempo total é limitado por dois gargalos físicos:

1. **Gargalo no Servidor:** O servidor precisa enviar $N$ cópias completas de $F$ bits, enviando um total de $N \cdot F$ bits pela sua interface de upload $u_s$. O tempo não pode ser menor que $\frac{N \cdot F}{u_s}$.
2. **Gargalo no Cliente Mais Lento:** O cliente com a menor taxa de download ($d_{\text{min}}$) leva no mínimo $\frac{F}{d_{\text{min}}}$ para receber seus próprios $F$ bits.

##### 2. Aplicação da Fórmula

$$D_{\text{CS}} = \max\left\{ \frac{N \cdot F}{u_s},\; \frac{F}{d_{\text{min}}} \right\}$$

##### 3. Interpretação em Termos de Redes

Para valores grandes de $N$, o tempo de distribuição é dominado pelo termo $\frac{N \cdot F}{u_s}$. **O tempo cresce de forma estritamente linear com o número de usuários $N$**. Se o número de clientes aumentar 1000 vezes, o tempo para distribuir o arquivo também aumentará 1000 vezes!

---

#### Modelo Matemático 2: Tempo de Distribuição na Arquitetura P2P ($D_{\text{P2P}}$)

##### 1. Dedução dos Limites Inferiores

No P2P, os pares redistribuem pedaços do arquivo entre si. O tempo total é limitado por três restrições físicas:

1. **Envio Inicial do Servidor:** Para que o arquivo entre na comunidade, o servidor precisa injetar cada um dos $F$ bits pelo menos uma vez no enlace. Tempo mínimo: $\frac{F}{u_s}$.
2. **Gargalo de Download no Cliente Lento:** O cliente mais lento ainda precisa baixar seus $F$ bits. Tempo mínimo: $\frac{F}{d_{\text{min}}}$.
3. **Capacidade Agregada de Upload do Sistema:** A rede como um todo precisa entregar um total de $N \cdot F$ bits para os $N$ clientes. A taxa máxima de upload combinada de todo o sistema é a soma do upload do servidor com o upload de todos os $N$ pares ($u_{\text{total}} = u_s + \sum_{i=1}^N u_i$). Tempo mínimo: $\frac{N \cdot F}{u_s + \sum_{i=1}^N u_i}$.

##### 2. Aplicação da Fórmula

$$D_{\text{P2P}} = \max\left\{
\frac{F}{u_s},\;
\frac{F}{d_{\text{min}}},\;
\frac{N \cdot F}{u_s + \sum_{i=1}^{N} u_i}
\right\}$$

##### 3. Interpretação em Termos de Redes (Análise com Uploads Iguais $u_i = u$)

Se todos os pares tiverem a mesma taxa de upload $u_i = u$, a capacidade total de upload torna-se $u_s + N \cdot u$. O terceiro termo passa a ser:

$$\frac{N \cdot F}{u_s + N \cdot u}$$

Quando $N \to \infty$, dividindo o numerador e o denominador por $N$:

$$\lim_{N \to \infty} \frac{N \cdot F}{u_s + N \cdot u} = \frac{F}{u}$$

O tempo de distribuição P2P **não cresce indefinidamente com $N$**; ele atinge uma assíntota e fica limitado superiormente! O gráfico de $D_{\text{P2P}}$ vs. $N$ curva-se e estabiliza, demonstrando a **autoescalabilidade do P2P**.

---

### 3. O Protocolo BitTorrent: Mecanismos Práticos de Funcionamento

O BitTorrent é o protocolo P2P de distribuição de arquivos mais popular do mundo.

- **Torrent e Chunks:** A coleção de todos os pares compartilhando um arquivo é chamada de **torrent**. O arquivo é dividido em blocos idênticos chamados **chunks** (tipicamente de **256 KB**).
- **Rastreador (_Tracker_):** Nó central de infraestrutura que mantém o registro de quais pares estão ativos no torrent. Quando um novo par (Alice) entra na rede, ela se registra no _tracker_ e recebe uma lista com o endereço IP de um subconjunto de pares (seus "vizinhos").
- **Seleção de Chunks — O Mais Raro Primeiro (_Rarest First_):** Para decidir qual bloco pedir aos seus vizinhos, Alice determina quais blocos possuem o menor número de cópias disponíveis entre eles e **solicita os blocos mais raros primeiro**. Isso equaliza o número de cópias de cada bloco na rede e evita que um bloco desapareça se a fonte original sair.
- **Algoritmo de Incentivo — _Tit-for-Tat_ (Olho por Olho):** Como evitar que usuários "caronas" (_freeriders_) apenas baixem arquivos sem enviar nada em troca?
    1. Alice mede continuamente a taxa na qual recebe dados de cada vizinho.
    2. Ela seleciona os **4 pares que lhe fornecem dados na maior taxa** e retribui enviando blocos para eles. Esses 4 pares são chamados de **desbloqueados (_unchoked_)**. A lista é recalculada a cada 10 segundos.
    3. **Desbloqueio Otimista (_Optimistically Unchoked_):** A cada 30 segundos, Alice escolhe aleatoriamente **1 par adicional** (Bob) e envia blocos para ele. Se Bob retribuir com uma taxa alta, ele pode entrar na lista dos "Top 4" de Alice no ciclo seguinte. Isso permite que novos pares sem blocos consigam suas primeiras peças e que pares com altas capacidades de upload se encontrem.

---

## 2.6 Streaming de Vídeo e Redes de Distribuição de Conteúdo (CDNs)

---

### 2.6.1 O Desafio do Streaming de Vídeo e o Protocolo DASH

#### Fenômeno de Rede

O tráfego de vídeo (YouTube, Netflix, Prime Video) representa cerca de **80% de todo o tráfego da Internet**. Um vídeo pré-gravado é uma sequência de imagens exibidas a uma taxa fixa (ex: 24 ou 60 quadros/s). Como entregar vídeo contínuo para usuários com conexões oscilantes (ex: 4G/5G em movimento)?

#### Conceito: DASH (_Dynamic Adaptive Streaming over HTTP_)

No streaming tradicional por HTTP, o vídeo era baixado como um arquivo único. No **DASH**, o vídeo é codificado em **múltiplas versões de qualidade/bitrate** e dividido em trechos (_chunks_) de alguns segundos de duração (ex: 2 a 10 segundos).

##### O Arquivo de Manifesto (_Manifest File_)

O servidor HTTP fornece um **arquivo de manifesto** que lista as URLs e as taxas de bits de cada versão de qualidade do vídeo.

1. O cliente baixa primeiramente o arquivo de manifesto.
2. Em seguida, a aplicação cliente requisita um trecho de vídeo por vez via requisições `HTTP GET` especificando o intervalo de bytes.
3. **Seleção Adaptativa de Taxa:** Conforme baixa os trechos, a aplicação cliente mede a largura de banda de recepção atual e monitora o nível de preenchimento do seu _buffer_ local. Se a rede acelerar, ela pede o próximo trecho em alta definição (4K); se o _buffer_ esvaziar ou a rede oscilar, ela alterna dinamicamente para uma versão de menor taxa de bits (720p/480p), evitando travamentos na exibição.

---

### 2.6.1.1 Dimensionamento do _Playout Buffer_ (Tema de Prova — "Nem Muito Grande, Nem Muito Pequeno")

#### Fenômeno de Rede

A rede não entrega dados a uma taxa perfeitamente constante — ela sofre variações de atraso (_jitter_). Se o player exibisse cada quadro assim que ele chegasse, qualquer oscilação momentânea na rede causaria uma pausa visível na reprodução. Por isso, o cliente mantém um **_playout buffer_**: ele acumula alguns segundos de vídeo antes de começar a exibição, criando uma "almofada" contra as variações de atraso.

#### Interpretação: os dois extremos

- **_Buffer_ muito pequeno:** o player fica exposto a qualquer oscilação de rede. Se a chegada de dados atrasar momentaneamente, o _buffer_ esvazia (_underflow_) e a reprodução trava (_rebuffering_) — a experiência do usuário é interrompida.
- **_Buffer_ muito grande:** o cliente precisa esperar mais tempo antes de começar a exibir (maior **atraso de início**, ruim para interatividade/live streaming), consome mais memória, e se o usuário pular para outro ponto do vídeo, todo o trabalho de download armazenado é desperdiçado.

O tamanho do _buffer_ é, portanto, um compromisso entre **robustez contra variações de rede** e **baixo atraso de início/uso de recursos** — o mesmo tipo de raciocínio de "nem muito grande, nem muito pequeno" reaparece no dimensionamento de temporizadores (_timeouts_) de protocolos confiáveis, que veremos adiante.

---

### 2.6.2 Redes de Distribuição de Conteúdo (_Content Distribution Networks - CDNs_)

#### Fenômeno de Rede

Se uma empresa de streaming mantiver um único _datacenter_ gigante com todos os seus vídeos, clientes distantes sofrerão com altos atrasos de propagação, travamentos em enlaces gargalo e o _datacenter_ será um ponto único de falha.

#### Conceito

Uma **CDN** é uma rede geograficamente distribuída de servidores _proxy_ que armazena cópias de vídeos e conteúdos em locais próximos aos usuários finais.

##### Filosofias de Posicionamento de Servidores de CDN

1. **Entrar Fundo (_Enter Deep_):** Instala pequenos _clusters_ de servidores profundamente **dentro das redes de acesso dos ISPs residenciais**.
    - _Vantagem:_ Minimiza a latência e contorna os gargalos da Internet pública.
    - _Desvantagem:_ Alta complexidade de manutenção e gerenciamento de milhares de _clusters_ espalhados.
2. **Trazer para Perto (_Bring Home_):** Instala _clusters_ maiores em grandes **Pontos de Troca de Tráfego (IXPs)** interconectando ISPs de Nível 1/2.
    - _Vantagem:_ Menor número de _clusters_ para manter.
    - _Desvantagem:_ Resulta em latências ligeiramente maiores do que o modelo _Enter Deep_.

##### Estratégias de Atualização de Conteúdo

- **Caches sob Demanda (_Pull-Caching_):** Se um cliente pede um vídeo que não está no _cluster_ local da CDN, o servidor busca o vídeo no repositório central, armazena uma cópia e o entrega ao cliente (usado pelo Google/YouTube).
- **Armazenamento Agendado (_Push-Caching_):** Conteúdos e filmes populares são enviados ativamente para os servidores da CDN em horários agendados fora do horário de pico (estratégia utilizada pela Netflix).

---

## 2.7 Programação com Sockets em Python: UDP vs. TCP

Para encerrar o Capítulo 2, analisaremos como as aplicações interagem com os protocolos de transporte através da **Socket API**.

---

### 2.7.1 Sockets UDP em Python (Sem Conexão)

#### Conceito

No UDP, **não há fase de estabelecimento de conexão** (_handshake_). O remetente anexa explicitamente o endereço IP e a porta de destino a cada datagrama enviado.

##### O Servidor UDP e o Número de Sockets (Questão de Prova)

Um servidor UDP precisa de **apenas 1 único socket** para atender a qualquer número de clientes simultâneos! Como o UDP não mantém estado de conexão, todas as mensagens de todos os clientes entram pela mesma "porta" do socket do servidor, e o servidor identifica quem enviou examinando a tupla `(IP_cliente, Porta_cliente)` retornada pela primitiva de recepção.

##### Código Prático UDP em Python

```python
# --- SERVIDIOR UDP (UDPServer.py) ---
from socket import *

serverPort = 12000
# Cria o socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))  # Associa o socket à porta 12000
print("Servidor UDP pronto para receber...")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # Recebe dados e endereço do cliente
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)  # Responde ao cliente

# --- CLIENTE UDP (UDPClient.py) ---
from socket import *

serverName = '127.0.0.1'  # IP do Servidor
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # Cria socket UDP do cliente

message = "mensagem de teste"
clientSocket.sendto(message.encode(), (serverName, serverPort))  # Envia datagrama
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # Recebe resposta
print("Resposta do Servidor:", modifiedMessage.decode())
clientSocket.close()
```

---

### 2.7.2 Sockets TCP em Python (Orientado à Conexão)

#### Conceito

No TCP, antes de trocar dados, cliente e servidor executam o _handshake_ de 3 vias. Uma vez estabelecida, a comunicação ocorre como um **fluxo contínuo de bytes (_byte-stream_)**.

##### Por que o Servidor TCP precisa de 2 Tipos de Sockets? (Questão Chave de Prova)

Diferente do UDP, um servidor TCP utiliza **dois tipos de sockets**:

1. **Socket de Boas-Vindas (_Welcome Socket / Listening Socket_):** Fica associado à porta bem conhecida (ex: porta `12000`) escutando requisições de conexão de novos clientes (`listen()`).
2. **Socket de Conexão (_Connection Socket_):** Quando um cliente inicia um _handshake_, a chamada `accept()` do servidor cria um **novo socket dedicado exclusivamente** para conversar com aquele cliente específico.

- **Interpretação e Cálculo:** Se um servidor TCP estiver atendendo a **$N$ clientes simultâneos**, ele manterá abertos exatamente **$N + 1$ sockets** em memória (1 socket de boas-vindas escutando a porta principal + $N$ sockets de conexão dedicados aos clientes ativos).

##### Código Prático TCP em Python

```python
# --- SERVIDOR TCP (TCPServer.py) ---
from socket import *

serverPort = 12000
# 1. Cria o Socket de Boas-Vindas (AF_INET = IPv4, SOCK_STREAM = TCP)
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(('', serverPort))
welcomeSocket.listen(1)  # Começa a escutar requisições TCP
print("Servidor TCP escutando na porta 12000...")

while True:
    # 2. accept() bloqueia até chegar um cliente e CRIA o Socket de Conexão dedicado
    connectionSocket, addr = welcomeSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()  # Fecha o socket de conexão do cliente atual

# --- CLIENTE TCP (TCPClient.py) ---
from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# Inicia o Three-Way Handshake TCP com o servidor
clientSocket.connect((serverName, serverPort))

sentence = "mensagem de teste tcp"
clientSocket.send(sentence.encode())  # Envia fluxo de bytes
modifiedSentence = clientSocket.recv(1024).decode()
print("Resposta do Servidor:", modifiedSentence)
clientSocket.close()
```

---

#### Tabela Resumo: Programação com Sockets UDP vs. TCP

| Propriedade                                   | **Sockets UDP**                                                                 | **Sockets TCP**                                                                     |
| :-------------------------------------------- | :------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------- |
| **Tipo de Socket Python**                     | `SOCK_DGRAM`                                                                    | `SOCK_STREAM`                                                                       |
| **Estabelecimento de Conexão**                | Não há (`connect` opcional).                                                    | Obrigatório via `connect()` e `accept()`.                                           |
| **Primitivas de E/S**                         | `sendto()` e `recvfrom()` (com endereçamento explícito).                        | `send()` e `recv()` (pelo canal já estabelecido).                                   |
| **Abstração de Dados**                        | **Datagramas discretos** (preserva limites de mensagem).                        | **Fluxo contínuo de bytes** (_Byte-Stream_).                                        |
| **Sockets no Servidor (para $N$ clientes)** | **1 socket único** para todos os clientes.                                      | **$N + 1$ sockets** (1 de boas-vindas + $N$ de conexão).                        |
| **Ordem de Execução dos Programas**           | O cliente pode enviar mensagens antes do servidor rodar (dados serão perdidos). | O programa servidor **precisa rodar antes** para abrir o socket e escutar na porta. |


---
# Capítulo 3 (Resumo Essencial para a P1): Transmissão Confiável de Dados

> **Nota de revisão:** esta seção não estava no resumo original, que ia até o Capítulo 2. Ela foi adicionada porque **todas as seis provas antigas anexadas contêm uma questão inteira (2 a 4 pontos) sobre este tema** — stop-and-wait, ACKs/NAKs, números de sequência, Go-Back-N, Selective Repeat, checksum/paridade e dimensionamento de timeout. É provavelmente o assunto matemático mais cobrado depois de filas M/M/1.

## 3.1 Por que a Transmissão Confiável é Difícil?

### Fenômeno de Rede

A camada de rede (IP) só promete um "melhor esforço" (_best-effort_): pacotes podem ser **corrompidos** (bits invertidos por ruído no canal), **perdidos** (descartados por _buffer_ cheio) ou **atrasados/reordenados**. Se uma aplicação (ou o TCP) precisa garantir que todos os dados cheguem corretos e na ordem certa, ela precisa construir esses mecanismos de confiabilidade **por cima** de um canal não confiável.

### Conceito: os três ingredientes básicos

1. **Checksum:** um pequeno conjunto de bits, calculado a partir dos dados, que permite ao receptor detectar corrupção (mas não corrigir sozinho).
2. **ACK / NAK (_Acknowledgment_ / _Negative Acknowledgment_):** mensagens de controle que o receptor devolve ao emissor para confirmar ("recebi certo") ou negar ("recebi errado, reenvie") a chegada de um pacote.
3. **Números de sequência:** identificadores anexados a cada pacote para que o receptor consiga distinguir um pacote novo de uma retransmissão de um pacote antigo.
4. **Temporizador (_timer_):** se o emissor não recebe confirmação dentro de um tempo esperado, ele assume que algo deu errado (perda) e retransmite.

---

## 3.2 Checksum e Bit de Paridade

### Conceito

O **bit de paridade** é o checksum mais simples: dado um conjunto de bits de dados, acrescenta-se 1 bit extra de forma que o **número total de 1's** (dados + paridade) seja sempre par (paridade par) ou sempre ímpar (paridade ímpar).

### Interpretação — o que a prova cobra

- **1 bit de paridade detecta qualquer corrupção de exatamente 1 bit**, não importa o tamanho da mensagem original, e **mesmo que a corrupção ocorra no próprio bit de paridade** — porque, em qualquer um dos casos, a contagem total de 1's muda de par para ímpar (ou vice-versa), e essa mudança é o que é detectado.
- **Limitação:** 1 bit de paridade **não detecta corrupção de 2 bits simultâneos** (a paridade volta a "fechar" corretamente por coincidência).
- **Checksum sozinho não basta** para transmissão confiável: ele só resolve o problema de **corrupção**. Ainda é preciso números de sequência (para não confundir pacotes) e temporizadores (para lidar com **perda**, que o checksum não consegue detectar — um pacote perdido simplesmente não chega, não há nada para checar).

**Exemplo (baseado em prova):** mensagem original de 4 bits `0001`; com paridade par, acrescenta-se um bit para que a contagem de 1's seja par: `0001_1` (5 bits, dois 1's → par). Se o canal corromper esse pacote para `0001_0`, a contagem de 1's passa a ser ímpar — o erro é detectado, mesmo tendo ocorrido no próprio bit de paridade.

---

## 3.3 Stop-and-Wait: o Protocolo Mais Simples

### Conceito

No protocolo **Stop-and-Wait** (a base do RDT 3.0 do Kurose), o emissor transmite **um único pacote** e então **para e espera** (_stop and wait_) por um ACK do receptor antes de enviar o próximo. Se o ACK não chegar dentro do tempo de *timeout*, o emissor retransmite o mesmo pacote.

### Por que precisamos de números de sequência mesmo em Stop-and-Wait?

Esta é uma das perguntas mais recorrentes nas provas. A resposta depende de **quais mensagens de controle existem**:

- **Com ACKs e NAKs, sem perdas (só corrupção):** os **pacotes de dados precisam de número de sequência** (para o receptor distinguir "isto é um pacote novo" de "isto é uma retransmissão do pacote anterior", caso o ACK/NAK anterior tenha se corrompido). Já os **próprios ACKs/NAKs não precisam identificar qual pacote confirmam** — como só existe um pacote pendente por vez, o próximo ACK/NAK sempre se refere ao último pacote enviado. Basta **1 bit** de número de sequência nos pacotes (alternando entre 0 e 1) — essa é a origem do nome "protocolo *alternating bit*".
- **Usando apenas ACKs, sem NAKs (o receptor sempre manda ACK do último pacote recebido com sucesso):** agora o **ACK precisa conter o número de sequência do pacote que está confirmando**. Sem essa informação, o emissor não conseguiria distinguir um ACK do pacote atual (que pode estar corrompido, exigindo reenvio) de um ACK duplicado do pacote anterior.

### Modelo matemático — Probabilidade de sucesso por tentativa

Seja $p$ a probabilidade de uma tentativa de envio ser bem-sucedida (pacote **e** ACK chegam corretamente).

- **Variável de uma única tentativa:** $X = 1$ se sucesso, $X=0$ se falha. $X \sim \text{Bernoulli}(p)$, logo $E[X] = p$.
- **Número de tentativas até o primeiro sucesso ($Y$):** como o emissor retransmite até acertar, $Y$ conta quantas tentativas são necessárias. $Y \sim \text{Geométrica}(p)$:
$$P(Y = y) = (1-p)^{y-1} \cdot p, \quad y = 1, 2, 3, \dots \qquad E[Y] = \frac{1}{p}$$
  - **Interpretação:** a probabilidade de acertar *exatamente* na 3ª tentativa é $P(Y=3) = (1-p)^2 \cdot p$ (as duas primeiras falham, a terceira dá certo).
- **Enviando $n$ pacotes independentes — número enviado sem precisar de retransmissão ($Z$):** cada um dos $n$ pacotes é bem-sucedido de primeira com probabilidade $p$, de forma independente. $Z \sim \text{Binomial}(n, p)$, com $E[Z] = np$.

> **Ponte com o Capítulo 1:** repare que essa é exatamente a mesma família de distribuições (Bernoulli → Geométrica → Binomial) usada para modelar usuários ativos e bloqueio em multiplexação estatística — só que agora aplicada a *tentativas de transmissão* em vez de *usuários simultâneos*.

### Modelo matemático — Utilização e vazão do Stop-and-Wait

#### Sem perdas

O ciclo de Stop-and-Wait é: transmitir o pacote ($L/R$) + esperar o RTT de ida e volta. A **utilização** $U$ é a fração desse ciclo em que o enlace está de fato ocupado enviando dados úteis:

$$U_{\text{sem perdas}} = \frac{L/R}{\text{RTT} + L/R}$$

- **Hipóteses:** $L$ = tamanho do pacote (bits), $R$ = taxa de transmissão (bits/s), RTT = tempo de propagação de ida e volta (sem contar o tempo de transmissão do ACK, considerado desprezível).
- **Interpretação:** se RTT $\gg L/R$ (enlace rápido, mas distância grande — ex.: satélite), $U \to 0$: o emissor passa a maior parte do tempo **ocioso**, esperando o ACK voltar, desperdiçando a capacidade do enlace. Essa ineficiência é justamente o problema que motiva o *pipelining* (Seção 3.4).
- **Vazão:** $\text{vazão} = U \cdot R$, ou equivalentemente $L / (\text{RTT} + L/R)$.

#### Com perdas (probabilidade de sucesso $p$ por tentativa)

Como cada pacote precisa, em média, de $E[Y] = 1/p$ tentativas até ter sucesso, o tempo efetivo do ciclo aumenta por esse fator:

$$U_{\text{com perdas}} \approx \frac{L/R}{\text{RTT}/p}$$

- **Interpretação:** quanto **menor** $p$ (canal mais sujeito a erros), **menor** a utilização — faz sentido, pois mais tempo é gasto retransmitindo. Quando $p=1$ (sem perdas), a fórmula se reduz ao caso anterior (aproximando $L/R$ como desprezível frente ao RTT).
- **Como aumentar utilização/vazão:** diminuir o RTT, aumentar $R$ (menos tempo de transmissão relativo) ou — mais importante — **abandonar o Stop-and-Wait em favor de um protocolo com pipelining** (próxima seção).

---

## 3.4 Pipelining: Go-Back-N (GBN) e Selective Repeat (SR)

### Fenômeno de Rede

Como acabamos de ver, Stop-and-Wait desperdiça o enlace sempre que RTT for grande em relação ao tempo de transmissão. A solução é permitir que o emissor mande **vários pacotes antes de receber a confirmação do primeiro** — isso é chamado de *pipelining*, e o número de pacotes não confirmados permitidos por vez é a **janela** de tamanho $J$.

### Conceito — as duas estratégias de recuperação de erro

1. **Go-Back-N (GBN):** o receptor é "burro" — ele só aceita pacotes **em ordem** e descarta silenciosamente qualquer pacote fora de ordem (mesmo que não esteja corrompido). O ACK é **cumulativo**: confirma "recebi corretamente até o pacote de número $k$". Se der timeout, o emissor **retransmite todos** os pacotes da janela a partir do primeiro não confirmado (daí o nome: "volta N posições").
2. **Selective Repeat (SR):** o receptor **bufferiza** pacotes fora de ordem em vez de descartá-los, e confirma **cada pacote individualmente**. Se der timeout (ou vier um NAK) apenas para um pacote específico, **só aquele pacote** é retransmitido — muito mais eficiente em canais com erros, ao custo de um receptor mais complexo (precisa de buffer e lógica de reordenação).

### Modelo matemático — quantos números de sequência são necessários?

Esta é a pergunta mais recorrente e mais traiçoeira das provas. Seja $J$ o tamanho da janela do emissor e $S+1$ o tamanho do espaço de números de sequência (números de $0$ a $S$, aritmética módulo $S+1$).

- **Em GBN:** como o receptor **descarta** qualquer pacote fora de ordem, ele nunca precisa distinguir um pacote "velho" atrasado de um "novo" — ele só aceita o único número que está esperando. A única ambiguidade possível é no **emissor**, que precisa distinguir um ACK novo de um ACK antigo duplicado. Basta, portanto, que a janela caiba dentro do espaço de sequência:
$$S + 1 \geq J + 1 \quad \Longleftrightarrow \quad S \geq J$$
- **Em SR:** como o receptor **aceita e armazena** pacotes fora de ordem (ele também usa uma janela de tamanho $J$), é possível que, simultaneamente, estejam "em trânsito" pacotes/ACKs cobrindo até $2J$ números de sequência distintos (a janela nova do emissor e a janela antiga ainda sendo confirmada pelo receptor podem se sobrepor). É necessário:
$$S + 1 \geq 2J$$
  - **Consequência clássica de prova:** em SR, usar um espaço de sequência igual a $2J$ exatamente é a condição **mínima**; usar menos que isso gera ambiguidade entre um pacote novo e uma retransmissão antiga, mesmo sem haver perdas ou corrupção.

### Modelo matemático — utilização com pipelining

Com uma janela de $J$ pacotes, o emissor consegue manter até $J$ pacotes "no ar" simultaneamente. A utilização passa a ser:

$$U_{\text{pipeline}} = \min\left(1,\; J \cdot \frac{L/R}{\text{RTT} + L/R}\right)$$

- **Interpretação:** para $J=1$, essa fórmula se reduz exatamente à utilização do Stop-and-Wait — o que confirma que Stop-and-Wait **é** um caso particular de GBN/SR com janela igual a 1 (é exatamente esse raciocínio que aparece na prova de 2025/2, item (a): com $J=1$, o emissor só pode ter um pacote pendente de ACK por vez).
- Aumentar $J$ aumenta a utilização até o ponto em que $U=1$ (enlace 100% ocupado) — depois disso, aumentar $J$ ainda mais não ajuda a vazão, só aumenta o número de pacotes que precisam ser retransmitidos em caso de erro (em GBN).

---

## 3.5 Dimensionamento do Timeout: "Nem Muito Grande, Nem Muito Pequeno"

### Conceito

O valor do *timeout* (tempo que o emissor espera antes de assumir perda e retransmitir) precisa ser cuidadosamente escolhido:

- **Timeout muito curto:** o emissor retransmite pacotes que na verdade **ainda estão a caminho** (não foram perdidos, só demoraram um pouco mais que o normal). Isso gera **retransmissões desnecessárias**, desperdiçando banda e podendo até piorar o congestionamento que causou o atraso em primeiro lugar.
- **Timeout muito longo:** quando um pacote é **de fato** perdido, o emissor demora muito para perceber e retransmitir, aumentando o atraso percebido pela aplicação e reduzindo a vazão efetiva.
- **Regra geral:** o timeout deve ser **maior que o RTT esperado**, mas não muito maior — daí a necessidade de estimar o RTT dinamicamente, e não usar um valor fixo.

### Interpretação — regra de ouro

Quanto **maior** o RTT (rede mais lenta ou mais distante), **maior** deve ser o timeout — nunca o contrário. Isso é uma pegadinha de prova recorrente: a afirmação "quanto menor o RTT, maior deve ser o timeout" está **errada**; a relação é diretamente proporcional, não inversa.

O TCP resolve esse problema estimando um **RTT suavizado** (média móvel ponderada de amostras de RTT reais) e somando uma margem de segurança proporcional à variabilidade observada, em vez de usar um valor fixo.

---

## 3.6 Produto Atraso × Banda e o Tamanho Ótimo da Janela

### Conceito

O **produto atraso-banda** (_delay-bandwidth product_) é a quantidade de bits que podem estar "em trânsito" dentro da rede em um dado instante — pense na rede como um cano, e nesse produto como o volume desse cano:

$$\text{Produto Atraso-Banda} = \text{RTT} \times R \quad [\text{bits}]$$

### Interpretação — por que ele determina a janela ideal de GBN/SR e do TCP

Para manter o enlace **sempre ocupado** (utilização máxima), o emissor precisa ter, em voo, uma quantidade de dados não confirmados **pelo menos igual** ao produto atraso-banda — ou seja, o tamanho da janela (em bits) precisa satisfazer $J \cdot L \geq \text{RTT} \times R$.

- **Janela muito pequena** (menor que o produto atraso-banda): o emissor esgota os pacotes permitidos e fica ocioso esperando ACKs antes que o enlace seja totalmente utilizado — subutilização, o mesmo problema do Stop-and-Wait.
- **Janela muito grande:** não ajuda mais a vazão (o enlace já está 100% ocupado), mas aumenta o risco de sobrecarregar buffers de roteadores no caminho (mais pacotes em fila) e o custo de uma eventual retransmissão em GBN (mais pacotes para reenviar).

Esse é o mesmo princípio "nem muito grande, nem muito pequeno" da Seção 2.6.1.1 (buffer de streaming) e da Seção 3.5 (timeout) — um padrão que se repete várias vezes na disciplina.

---

## 3.7 TCP: Confiabilidade + Controle de Congestionamento (Visão Essencial)

### Conceito

O TCP combina ideias de GBN e SR (é *cumulativo* como GBN, mas pode reconhecer segmentos individuais fora de ordem com ACKs duplicados/opções SACK, como SR) e adiciona **controle de congestionamento**: o emissor ajusta dinamicamente sua janela de congestionamento ($\text{cwnd}$) com base em sinais de perda.

### Modelo matemático — AIMD (_Additive Increase, Multiplicative Decrease_)

- **Aumento aditivo:** enquanto não há perda, $\text{cwnd}$ cresce **linearmente** (tipicamente +1 MSS por RTT) — o TCP testa a rede cautelosamente, sondando por mais capacidade disponível aos poucos.
- **Diminuição multiplicativa:** ao detectar perda (timeout ou 3 ACKs duplicados), o TCP interpreta isso como sinal de congestionamento e **corta a janela pela metade** — uma reação agressiva e imediata.
- **Interpretação da prova:** quando a janela do TCP diminui, isso indica que o TCP **detectou** (ou presumiu) perda de pacote — mas atenção: nem toda perda de pacote é causada por estouro de fila (buffer overflow); ela pode ter outras causas (corrupção em enlace sem fio, por exemplo). Por isso a afirmação "toda queda de janela implica necessariamente estouro de fila" deve ser tratada com cautela em questões de V ou F.
- **Controle de fluxo vs. controle de congestionamento (cuidado com pegadinha clássica):** são dois mecanismos **diferentes**, ambos implementados via o tamanho de janela do TCP, mas com propósitos opostos aos que a intuição sugere à primeira vista:
    - **Controle de fluxo:** evita que o **emissor** sobrecarregue o **buffer de recepção do receptor** (não tem relação com "gargalos no emissor").
    - **Controle de congestionamento:** evita que o emissor sobrecarregue a **rede** (roteadores no meio do caminho), não especificamente o receptor.
    - Nenhum dos dois "é" comutação por circuito ou por pacote — essa associação não faz sentido; ambos são mecanismos de camada de transporte que operam sobre uma rede de comutação por pacotes.

---

## Checklist da Seção 3 (Transmissão Confiável)

- [ ] Sei explicar por que checksum sozinho não garante confiabilidade (só detecta corrupção, não perda).
- [ ] Sei explicar por que 1 bit de paridade detecta erro de 1 bit mesmo se o erro for no próprio bit de paridade.
- [ ] Sei explicar quando os ACKs precisam (ou não) de número de sequência, dependendo de existirem NAKs.
- [ ] Sei calcular $E[X]$, $E[Y]$ (geométrica) e $E[Z]$ (binomial) num cenário de retransmissões.
- [ ] Sei calcular utilização do Stop-and-Wait com e sem perdas, e explicar por que RTT grande prejudica a utilização.
- [ ] Sei explicar a diferença entre GBN e SR (o que o receptor faz com pacotes fora de ordem) e deduzir $S \geq J$ (GBN) e $S+1 \geq 2J$ (SR).
- [ ] Sei explicar por que o timeout deve crescer com o RTT, nunca diminuir.
- [ ] Sei explicar o papel do produto atraso-banda no dimensionamento da janela.
- [ ] Sei diferenciar controle de fluxo (protege o receptor) de controle de congestionamento (protege a rede).
