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

-  q : Probabilidade de um _slot_ estar descongestionado (sucesso, ou seja,  P(A \le r) ).
-  1 - q : Probabilidade de o _slot_ estar congestionado ( P(A > r) ).
-  S : Número de _slots_ futuros até observar o primeiro _slot_ descongestionado ( S \in {1, 2, 3, \dots} ).

##### 4. Hipóteses

- Os estados da rede em _slots_ consecutivos são temporalmente **independentes**.

##### 5. Aplicação das Fórmulas

Como estamos contando o número de tentativas até obter o primeiro sucesso (slot descongestionado),  S  segue uma **Distribuição Geométrica**:

$$S \sim \text{Geom}(q)$$ $$P(S = s) = (1 - q)^{s-1} \cdot q, \quad s = 1, 2, 3, \dots$$

O **Tempo Médio de Recuperação (Esperança de  S )** é:

$$E[S] = \frac{1}{q}$$

##### 6. Interpretação em Termos de Redes

Se a probabilidade de um slot estar normal for  q = 0{,}50 , o tempo médio de descongestionamento é  E[S] = \frac{1}{0{,}50} = 2\text{ slots} . Se a rede estiver extremamente sobrecarregada com  q = 0{,}20 , levará em média  E[S] = \frac{1}{0{,}20} = 5\text{ slots}  para se recuperar.

---

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
