### 1. Visão física da Internet ("nuts-and-bolts")

- **Hosts (end systems):** geram/consomem dados
- **Enlaces de comunicação:** cabos, fibra, rádio — cada um com taxa de transmissão **R** (bits/s)
- **Comutadores de pacotes:** roteadores (núcleo) e switches de enlace (borda) — redirecionam dados pelo caminho
- **Rota/caminho:** sequência de enlaces + comutadores entre origem e destino
#### 1.1 Visão de Serviços
Sob a perspectiva do que ela oferece às aplicações, a Internet é uma **infraestrutura que provê serviços para aplicações distribuídas**

#### 1.2 O que é um Protocolo?

Toda a comunicação entre dispositivos na Internet é governada por **protocolos**[20].
##### Definição de Protocolo:

Um **protocolo** define o **formato** (sintaxe) e a **ordem** das mensagens trocadas entre duas ou mais entidades comunicantes, além das **ações** (semântica) tomadas no envio ou no recebimento de uma mensagem.


### 2. Por que dividir dados em pacotes

- Evita que um único usuário monopolize um enlace inteiro → **multiplexação estatística**
### 3. Store-and-forward

- Roteador só retransmite um pacote **depois** de recebê-lo por completo
- $d_{trans} = L/R$; para P pacotes back-to-back em N enlaces: $(N+P-1)\cdot(L/R)$
- **Cut-through switching:** retransmite assim que lê o cabeçalho — atraso deixa de se multiplicar por N
### 4. Redes de acesso e meios físicos

- **Acesso residencial:** DSL, cabo (compartilhado), FTTH, móvel | **Institucional:** Ethernet, Wi-Fi
- **Meios guiados:** par trançado, coaxial, fibra | **Não guiados:** rádio, satélite
- **Arquiteturas de aplicação:** cliente-servidor vs. P2P

### 5. Comutação de pacotes

- Multiplexação estatística evita monopolização de enlace
- **Store-and-forward:** $d_{trans}=L/R$; P pacotes/N enlaces: $(N+P-1)L/R$
- **Cut-through:** não espera pacote inteiro
### 6. Comutação de circuitos vs. pacotes

| Circuitos      | Pacotes                           |                            |
| -------------- | --------------------------------- | -------------------------- |
| Recursos       | Reservados/dedicados              | Compartilhados sob demanda |
| Taxa garantida | Sim                               | Não                        |
| Ociosidade     | Desperdiça recurso                | Aproveitada por outros     |
| Técnicas       | FDM / TDM                         | —                          |
| Melhor para    | Tráfego constante, sessões longas | Tráfego variável/rajado    |

|Circuitos|Pacotes|
|---|---|---|
|Recursos|Reservados (FDM/TDM)|Compartilhados|
|Melhor para|Tráfego constante|Tráfego variável|

### 7. Os quatro atrasos nodais

$$d_{nodal} = d_{proc} + d_{fila} + d_{trans} + d_{prop}$$

- **d_proc:** fixo, exame do cabeçalho
- **d_fila:** único que varia com o tráfego
- **d_trans = L/R:** fixo (pacote + enlace)
- **d_prop = m/s:** fixo (distância física + velocidade do sinal, independe de L)
- **d_empacotamento** (visto no P7/VoIP): tempo para acumular bits suficientes pra formar um pacote

### 8. Atrasos, perda e vazão

- $d_{nodal}=d_{proc}+d_{fila}+d_{trans}+d_{prop}$ (+ $d_{empacot}$ em VoIP)
- **Único variável:** $d_{fila}$, via $I=La/R$
- **Teoria de filas:** $N=I/(1-I)$ (M/M/1, via Little ou Markov); M/D/1: $N=\frac{I(2-I)}{2(1-I)}$
- $d_{total}=\frac{L/R}{1-I}=\frac{1}{\mu-a}$
- **Vazão:** $\min(R_1,...,R_N)$ | **Packet pair:** revela taxa do gargalo
- Fim-a-fim geral: $\sum_{i=1}^N(d_{proc}^{(i)}+d_{trans}^{(i)}+d_{prop}^{(i)}+d_{queue}^{(i)})$
- **Perda:** $(1-p)^N$ sucesso em N enlaces; retransmissões médias $=1/(1-p)^N$ (geométrica)
### 9. Intensidade de tráfego (I = La/R) e atraso de fila

- **I → 0:** fila quase inexistente | **I = 1:** rajadas causam fila → atraso médio tende ao infinito | **I > 1:** fila cresce sem limite → **perda de pacotes**
- **Lei de Little / teoria de filas (M/M/1):** $N = I/(1-I)$ — número médio de pacotes no sistema, derivável tanto via Lei de Little quanto via cadeia de Markov (nascimento-morte), com resultado idêntico

### 10. Vazão (throughput)

- Vazão média = F/T; limitada pelo **enlace gargalo**: $\min(R_1,...,R_N)$
- **Packet pair:** intervalo de chegada de 2 pacotes back-to-back no destino revela a taxa do enlace gargalo (L/Rs)

### 11. Camadas de protocolo (5 camadas do modelo Internet)

1. **Aplicação** (HTTP, SMTP, DNS...)
2. **Transporte** (TCP, UDP) — entre processos
3. **Rede** (IP) — roteamento, datagramas
4. **Enlace** (Ethernet, Wi-Fi) — nó a nó adjacente
5. **Física** — bits → sinais físicos

- **Vantagem:** modularidade (mudar uma camada sem afetar as outras)
- **Desvantagens:** (1) redundância de funcionalidade entre camadas, (2) ocultação de informação entre camadas
- **Encapsulamento:** cada camada adiciona seu cabeçalho aos dados de cima (mensagem → segmento → datagrama → quadro); desencapsulamento no destino faz o processo inverso
- **Dispositivos e camadas:** hosts implementam as 5; roteadores implementam física+enlace+rede; switches implementam só física+enlace
### 12. Segurança (visão geral)

- Malware (vírus, worms) | DoS/DDoS (vulnerabilidade, banda, conexões) | Packet sniffing | IP spoofing

### 13. Histórico

- 1961-72: ARPANET | 1972-80: TCP/IP | 1980-90: DNS, NSFNET | 1990-2000: Web (HTTP/HTML) | 2000-hoje: banda larga, mobile, cloud

Aqui está o resumo do **Capítulo 1 (Redes de Computadores e a Internet)**, reunindo as explicações teóricas do livro do Kurose, as notas de aula e os modelos matemáticos desenvolvidos pelo seu professor.

---

### **1. Resumo Integrado do Capítulo 1**

#### **1.1. O que é a Internet e o que são Protocolos?**

- **Visão Física (Componentes):** A Internet é uma rede global composta por **sistemas finais** (_hosts_) nas bordas, conectados por **enlaces de comunicação** (fibras, cabos, rádio) e **comutadores de pacotes** (roteadores e _switches_). Os sistemas finais conectam-se através de uma estrutura hierárquica de Provedores de Serviços de Internet (ISPs).
- **Visão de Serviço:** É uma infraestrutura que provê serviços e interfaces de programação (APIs / _sockets_) para que **aplicações distribuídas** (Web, streaming, e-mail) troquem dados sem precisar conhecer a mecânica interna do núcleo da rede.
- **Conceito de Protocolo:** Regras que governam a comunicação entre entidades. É composto por:
    - **Sintaxe:** Formato e estrutura dos campos da mensagem.
    - **Semântica:** Significado de cada campo e ações a serem tomadas no envio/recebimento.
    - **Ação/Ordem:** Sequência temporal na qual as mensagens devem ser trocadas.

#### **1.2. A Borda da Rede e Redes de Acesso**

- **Sistemas Finais (_Hosts_):** Ficam nas extremidades da rede e são divididos em **clientes** (solicitam serviços) e **servidores** (armazenam e entregam dados em _datacenters_).
- **Redes de Acesso Residencial:**
    - **DSL (Digital Subscriber Line):** Utiliza a linha telefônica de par trançado dedicada até o multiplexador DSLAM na central telefônica. Usa **FDM** para separar voz (0–4 kHz), upload (4–50 kHz) e download (50 kHz–1 MHz).
    - **Cabo / HFC (Híbrido Fibra-Coaxial):** Combina fibra até os nós de bairro e cabo coaxial até as casas. Conecta-se ao CMTS na operadora. É um **meio compartilhado**: usa FDM para divisão de frequência e TDMA para coordenar as transmissões de envio.
    - **FTTH (Fiber to the Home):** Leva fibra óptica direto à residência. Na arquitetura PON (Rede Óptica Passiva), cada casa tem uma ONT ligada por um distribuidor óptico (_splitter_) a uma OLT na central.
- **Redes Corporativas e Móveis:**
    - **Ethernet (LAN):** Conexão cabeada com _switches_, com velocidades de 100 Mbps a dezenas de Gbps.
    - **Wi-Fi (IEEE 802.11) e Redes Celulares (3G/4G/5G):** Transmissão sem fio via Pontos de Acesso (AP) ou Estações-Base (BS).
- **Meios Físicos:** Dividem-se em **guiados** (par trançado UTP, cabo coaxial, fibra óptica) e **não guiados** (ondas de rádio terrestres e satélites LEO/Geostacionários).

#### **1.3. O Núcleo da Rede (_Network Core_)**

- **Comutação de Pacotes:** Mensagens da aplicação são fragmentadas em pacotes de \(L\) bits.
    - **Armazena-e-Reenvia (_Store-and-Forward_):** O roteador deve receber o pacote **inteiro** em seu _buffer_ antes de começar a transmitir o primeiro bit no enlace seguinte.
    - **_Cut-Through_:** O comutador lê apenas o cabeçalho e já começa a repassar os bits antes de receber o pacote completo, reduzindo a latência (comportamento em _pipeline_).
- **Comutação de Circuitos:** Recursos do caminho são **reservados previamente** para a sessão. A capacidade é fatiada via **FDM** (divisão de frequência) ou **TDM** (divisão de tempo em _slots_).
- **Multiplexação Estatística vs. Reserva Estática:** A comutação de pacotes compartilha os enlaces sob demanda. É mais eficiente para tráfego em rajadas, suportando mais usuários ativos simultâneos.
- **Hierarquia de ISPs:** A Internet conecta ISPs de Acesso a ISPs Regionais e ISPs Globais de Nível 1 (_Tier-1_), interconectando-se via Pontos de Troca de Tráfego (IXPs) e redes privadas de conteúdo (como a da Google).

#### **1.4. Desempenho: Atraso, Perda e Vazão**

- **As 4 Fontes de Atraso Nodal:**
    1. \($d_{proc}$\) (Processamento): Checagem de erros de bit e consulta à tabela de repasse.
    2. $d_{fila}$ ou \(W\) (Fila): Espera no _buffer_ de saída até que o enlace fique livre.
    3. \($d_{trans}$\) ou \(S\) (Transmissão): Tempo para empurrar todos os bits do pacote para o meio.
    4. \($d_{prop}$\) (Propagação): Tempo necessário para que um bit viaje fisicamente pelo cabo/ar.
- **Intensidade de Tráfego (\(I\) ou \($\rho$\)):** Razão entre a taxa de chegada de bits e a capacidade de transmissão do enlace. Se \(I > 1\), a fila cresce indefinidamente ou ocorrem perdas por estouro de _buffer_.
- **Teoria de Filas e Lei de Little:** Estabelece que o número médio de pacotes em um sistema em equilíbrio é o produto da taxa de chegada pelo tempo médio no sistema (\($N = \lambda \cdot T$\)).
- **Vazão Fim a Fim (_Throughput_):** Determinada pela capacidade do **enlace gargalo** (o nó mais lento ao longo do caminho).

#### **1.5. Camadas de Protocolos e Encapsulamento**

- **Pilha de 5 Camadas da Internet:**
    1. **Aplicação:** Troca de mensagens entre processos (HTTP, SMTP, DNS).
    2. **Transporte:** Entrega de dados entre processos em _hosts_ distintos (TCP, UDP). PDU: **Segmento**.
    3. **Rede:** Roteamento e repasse de pacotes entre _hosts_ (IP). PDU: **Datagrama**.
    4. **Enlace:** Transferência de dados entre nós vizinhos (Ethernet, Wi-Fi). PDU: **Quadro** (_Frame_).
    5. **Física:** Transmissão dos bits individuais pelo meio físico.
- **Encapsulamento:** Ao descer na pilha, cada camada adiciona seu próprio **cabeçalho** (_header_) aos dados da camada superior, tratando a mensagem recebida como carga útil (_payload_).

#### **1.6. Segurança em Redes**

- **Tríade AIC:** Preservar **A**utenticidade/Confidencialidade, **I**ntegridade e **C**ompatibilidade/Disponibilidade.
- **Ameaças:** _Malware_ e _Botnets_, ataques de Recusa de Serviço (DoS/DDoS) por inundação de banda ou conexão, _Packet Sniffing_ (interceptação passiva) e _IP Spoofing_ (falsificação do IP de origem).

---

### **2. Interpretação Detalhada de Todas as Fórmulas do Capítulo 1**

#### **1. Atraso de Transmissão (\($d_{trans}$\) ou \($S$\))**

$$d_{trans} = \frac{L}{R}$$

- **O que representa:** O tempo exato que uma placa de rede leva para converter e empurrar todos os bits de um pacote para o meio físico.
- **Significado dos termos:**
    - \(L\) = Tamanho do pacote em **bits**.
    - \(R\) = Taxa de transmissão (largura de banda) do enlace em **bits por segundo (bit/s)**.
- **Interpretação:** É a "largura da porta". Quanto maior o pacote (\(L\)), mais tempo demora para sair; quanto mais rápida a rede (\(R\)), mais rápido ele é serializado. **Não depende da distância geográfica**.

---

#### **2. Atraso de Propagação (\($d_{prop}$\))**

$$d_{prop} = \frac{d}{s}$$

- **O que representa:** O tempo que um único bit leva para viajar fisicamente pelo meio de transmissão da origem até o destino.
- **Significado dos termos:**
    - \(d\) = Distância física entre o emissor e o receptor em **metros**.
    - \(s\) = Velocidade de propagação do sinal no meio físico (aprox. \($2 \times 10^8$\) a \($3 \times 10^8 \text{ m/s}$\)).
- **Interpretação:** É o tempo de viagem na estrada. **Não depende do tamanho do pacote nem da largura de banda (\(R\))**.

---

#### **3. Atraso Nodal Total (\(d_{nodal}\))**

$$d_{nodal} = d_{proc} + d_{fila} + d_{trans} + d_{prop}$$

- **O que representa:** O tempo total gasto por um pacote ao passar por um único nó (roteador).
- **Significado dos termos:**
    - \($d_{proc}$\) = Atraso de processamento do cabeçalho.
    - \($d_{fila}$\) (ou \($W$\)) = Tempo de espera na fila de saída do roteador.
    - \($d_{trans}$\) = Atraso de transmissão.
    - \($d_{prop}$\) = Atraso de propagação no enlace de saída.

---

#### **4. Atraso Fim a Fim em _Store-and-Forward_ (\($d_{\text{fim a fim}}$\))**

$$d_{\text{fim a fim}} = N \cdot \frac{L}{R}$$ _(Assumindo \(N\) enlaces idênticos com taxa \(R\), sem atraso de fila/processamento/propagação)_.

- **O que representa:** O tempo total para enviar 1 pacote da origem ao destino atravessando \(N\) enlaces.
- **Significado dos termos:**
    - \(N\) = Número de enlaces percorridos (\(N-1\) roteadores intermediários).
    - \(L/R\) = Atraso de transmissão de um pacote em um enlace.
- **Interpretação:** Como cada roteador opera em _Store-and-Forward_, ele precisa armazenar o pacote \(L/R\) segundos antes de retransmitir. O atraso de transmissão é pago em **todos** os \(N\) enlaces em série.

---

#### **5. Transmissão em _Pipeline_ de \(N\) Pacotes em \(H\) Enlaces**

$$T_{tx} = \frac{(H + N - 1)(L + h)}{R}$$

- **O que representa:** O tempo total de transmissão para levar uma mensagem dividida em \(N\) pacotes ao longo de \(H\) enlaces em série.
- **Significado dos termos:**
    - \(H\) = Número de enlaces.
    - \(N\) = Número de pacotes em que a mensagem foi fragmentada.
    - \(L\) (ou \($\ell$\)) = Tamanho útil dos dados no pacote.
    - \(h\) = Tamanho do cabeçalho (_header_) adicionado a cada pacote.
    - \(R\) = Taxa do enlace.
- **Interpretação:** O primeiro pacote leva \(H\) saltos para encher o _pipeline_. A partir daí, cada um dos \(N-1\) pacotes restantes chega com um espaçamento de apenas \(1\) tempo de transmissão.

---

#### __6. Tamanho Útil Ótimo do Pacote (\($\ell$\))_*

$$\ell^* = \sqrt{\frac{L' \cdot h}{H - 1}}$$

- **O que representa:** O tamanho ideal de dados em cada pacote que minimiza o tempo total de transmissão de uma mensagem grande.
- **Significado dos termos:**
    - \(L'\) = Tamanho total da mensagem original sem cabeçalhos.
    - \(h\) = Tamanho do cabeçalho por pacote.
    - \(H\) = Número de enlaces no caminho.
- **Interpretação:** Equilibra dois problemas: pacotes muito grandes demoram para encher o _pipeline_; pacotes muito pequenos adicionam excesso de cabeçalhos (\(h\)), desperdiçando banda.

---

#### **7. Intensidade de Tráfego (\(I\) ou \($\rho$\))**

$$I = \frac{a \cdot L}{R} = \frac{\lambda \cdot L}{R} = \frac{\lambda}{\mu}$$

- **O que representa:** O nível de ocupação do enlace de saída.
- **Significado dos termos:**
    - \(a\) (ou \($\lambda$\)) = Taxa média de chegada de pacotes (pacotes/segundo).
    - \(L\) = Tamanho médio do pacote em bits.
    - \(R\) = Taxa do enlace em bits/segundo.
    - \($a \cdot L$\) = Taxa média com que os bits chegam à fila.
    - \($\mu = R/L$\) = Taxa média de serviço do servidor (pacotes/segundo).
- **Interpretação:**
    - Se \($I \approx 0$\): Fila quase vazia.
    - Se \(I \to 1\): Fila e atraso crescem exponencialmente.
    - Se \(I > 1\): O sistema é instável, a fila cresce infinitamente e ocorrem perdas.

---

#### **8. A Lei de Little**

$$N = \lambda \cdot T \quad \text{ou} \quad N = a \cdot T$$

- **O que representa:** Relação fundamental válida para qualquer sistema de filas em equilíbrio.
- **Significado dos termos:**
    - \(N\) = Número médio de pacotes dentro do sistema.
    - \(\lambda\) (ou \(a\)) = Taxa média de chegada de pacotes.
    - \(T\) = Tempo médio que um pacote permanece no sistema.
- **Aplicações Específicas:**
    - Na fila de espera: \($N_q = a \cdot W$\) (número médio na fila = taxa \($\times$\) tempo de espera na fila).
    - No servidor: \($N_s = a \cdot S = I$\) (número médio no servidor = utilização do canal).

---

#### **9. Tempo Médio na Fila no Modelo \($M/M/1$\) (\($W_{M/M/1}$\))**

$$W_{M/M/1} = \frac{I}{\mu(1 - I)} = \frac{I \cdot (L/R)}{1 - I}$$

- **O que representa:** O tempo médio de espera na fila assumindo chegadas aleatórias de Poisson e tamanhos de pacote com distribuição exponencial (variáveis).
- **Significado dos termos:**
    - \(I\) = Intensidade de tráfego (\($\lambda / \mu$\)).
    - \($\mu$\) = Taxa de serviço do enlace (\(R/L\)).
- **Interpretação:** Mostra que conforme \(I\) se aproxima de 1, o termo \((1 - I)\) no denominador vai a zero, fazendo a espera tender ao infinito.

---

#### **10. Tempo Médio na Fila no Modelo $(M/D/1) ((W_{M/D/1}))$**

$$W_{M/D/1} = \frac{I}{2\mu(1 - I)} = \frac{1}{2} W_{M/M/1}$$

- **O que representa:** O tempo médio de espera na fila para pacotes de **tamanho fixo** (determinístico).
- **Interpretação:** Ao eliminar a variação do tamanho do pacote, a esperança do tempo residual cai pela metade, cortando o atraso de fila médio exatamente ao meio em relação ao modelo \(M/M/1\).

---

#### **11. Técnica do _Packet Pair_ (\($\Delta_{out}$\))**

$$\Delta_{out} = \frac{L}{R_{gargalo}} \implies \hat{R}_{gargalo} = \frac{L}{\Delta_{out}}$$

- **O que representa:** A estimativa da capacidade do enlace gargalo da rede através do intervalo de tempo (\(\Delta_{out}\)) medido entre a chegada de dois pacotes consecutivos transmitidos juntamente.

---

#### **12. Vazão Fim a Fim (_Throughput_)**

$$\text{Vazão} = \min(R_1, R_2, \dots, R_N)$$

- **O que representa:** A taxa efetiva de transferência de dados do cliente ao servidor.
- **Interpretação:** Funciona como o fluxo de água em um encanamento: a vazão total é limitada pelo cano mais fino (o **enlace gargalo**).

---

### **3. Glossário Detalhado**

- **API (_Application Programming Interface_):** Conjunto de regras oferecido pela camada de transporte/sistema operacional para que o programa de aplicação solicite serviços de rede. _Exemplo:_ A interface do aplicativo de entregas que permite pedir comida sem conhecer o caminho do entregador.
- **Atraso Nodal:** Soma dos quatro atrasos sofridos por um pacote ao passar por um roteador $(d_{proc} + d_{fila} + d_{trans} + d_{prop}$).
- **Bit:** A menor unidade de informação em computação (valor 0 ou 1).
- **CMTS (_Cable Modem Termination System_):** Equipamento na central da operadora de cabo que converte sinais analógicos vindos das casas em dados digitais para a Internet.
- **Comutação de Circuitos (_Circuit Switching_):** Abordagem de rede que reserva recursos dedicados ao longo de um caminho antes de transmitir dados. _Exemplo:_ Reserva de mesa em restaurante sofisticado.
- **Comutação de Pacotes (_Packet Switching_):** Abordagem da Internet que divide mensagens em pacotes e compartilha enlaces sob demanda sem reserva prévia. _Exemplo:_ Restaurante por ordem de chegada sem reservas.
- **_Cut-Through_:** Técnica de repasse em comutadores onde a transmissão começa assim que o cabeçalho do pacote é lido, sem esperar o pacote inteiro chegar.
- **Datagrama:** O pacote de dados característico da camada de rede (IP).
- **DSLAM (_Digital Subscriber Line Access Multiplexer_):** Equipamento na central telefônica que separa os sinais de voz dos dados de Internet transmitidos via DSL.
- **Encapsulamento:** Processo de empacotamento no qual cada camada da pilha adiciona seu próprio cabeçalho (_header_) ao redor da PDU da camada superior. _Exemplo:_ Colocar uma carta dentro de um envelope e depois dentro de uma caixa de despacho.
- **Enlace Gargalo (_Bottleneck Link_):** O enlace com a menor taxa de transmissão ao longo de uma rota fim a fim, determinando a velocidade máxima da conexão.
- **FDM (_Frequency-Division Multiplexing_):** Divisão da capacidade de um meio em faixas de frequência contínuas e paralelas. _Exemplo:_ Estações de rádio FM transmitindo simultaneamente em frequências diferentes.
- **_Host_ (Sistema Final):** Dispositivo conectado nas extremidades da rede que executa aplicações (clientes e servidores).
- **IXP (_Internet Exchange Point_):** Ponto físico de troca de tráfego onde múltiplos ISPs se conectam para trocar dados diretamente sem pagar trânsito.
- **Lei de Little:** Teorema da teoria de filas que relaciona o número médio de pacotes no sistema (\(N\)), a taxa de chegada (\($\lambda$\)) e o tempo no sistema (\(T\)) por \($N = \lambda T$\).
- **Multiplexação Estatística:** Compartilhamento dinâmico e sob demanda de um enlace entre múltiplos usuários, aproveitando os momentos de silêncio de cada um.
- **PDU (_Protocol Data Unit_):** Nome genérico do pacote em cada camada (Mensagem na Aplicação, Segmento no Transporte, Datagrama na Rede, Quadro no Enlace).
- **Protocolo:** Conjunto de regras que define sintaxe, semântica e ação para a troca de mensagens entre entidades.
- **Quadro (_Frame_):** A PDU da camada de enlace que transporta o datagrama entre dois nós vizinhos.
- **Segmento:** A PDU da camada de transporte (TCP/UDP).
- **_Socket_:** A porta lógica/interface entre o processo de aplicação e a pilha de protocolos de transporte do sistema operacional. _Exemplo:_ A porta de entrada e saída de uma casa.
- **_Store-and-Forward_ (Armazena-e-Reenvia):** Regime em que o roteador deve receber o pacote completamente antes de iniciar a retransmissão no enlace de saída.
- **TDM (_Time-Division Multiplexing_):** Divisão do tempo de transmissão em quadros fatiados em _slots_ periódicos atribuídos a cada conexão. _Exemplo:_ Turnos organizados para falar em uma reunião.

---

### **4. Destaques e Exemplos Práticos para Fixação**

- **Diferença entre Transmissão e Propagação (Analogia do Pedágio):**
    - **Transmissão (\(L/R\)):** É a velocidade do atendente do pedágio ao processar a fila de carros.
    - **Propagação (\(d/s\)):** É o tempo que os carros levam para dirigir na rodovia entre um pedágio e outro.
- **Por que utilizar comutação de pacotes em vez de circuitos?**
    - Em uma rede de 1 Mbps com usuários de 100 kbps ativos 10% do tempo: a comutação de circuitos só aceita 10 usuários fixos. A comutação de pacotes aceita 35 usuários mantendo uma probabilidade de sobrecarga menor que \(0,04%\).
- **Pipeline e Fragmentação:**
    - Enviar um arquivo imenso como um único pacote atrasa a entrega porque o primeiro roteador segura tudo antes de retransmitir. Ao fatiar a mensagem em pacotes menores, o segundo roteador já começa a repassar o primeiro pacote enquanto o segundo ainda está sendo enviado pela origem, criando um fluxo em _pipeline_.
