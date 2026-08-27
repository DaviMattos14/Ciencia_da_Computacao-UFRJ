### 1. Visão física da Internet ("nuts-and-bolts")

- **Hosts (end systems):** geram/consomem dados
- **Enlaces de comunicação:** cabos, fibra, rádio — cada um com taxa de transmissão **R** (bits/s)
- **Comutadores de pacotes:** roteadores (núcleo) e switches de enlace (borda) — redirecionam dados pelo caminho
- **Rota/caminho:** sequência de enlaces + comutadores entre origem e destino

### 2. Por que dividir dados em pacotes

- Evita que um único usuário monopolize um enlace inteiro → **multiplexação estatística**

### 3. Store-and-forward

- Roteador só retransmite um pacote **depois** de recebê-lo por completo
- $d_{trans} = L/R$; para P pacotes back-to-back em N enlaces: $(N+P-1)\cdot(L/R)$
- **Cut-through switching:** retransmite assim que lê o cabeçalho — atraso deixa de se multiplicar por N

### 4. Comutação de circuitos vs. pacotes

||Circuitos|Pacotes|
|---|---|---|
|Recursos|Reservados/dedicados|Compartilhados sob demanda|
|Taxa garantida|Sim|Não|
|Ociosidade|Desperdiça recurso|Aproveitada por outros|
|Técnicas|FDM / TDM|—|
|Melhor para|Tráfego constante, sessões longas|Tráfego variável/rajado|

### 5. Os quatro atrasos nodais

$$d_{nodal} = d_{proc} + d_{fila} + d_{trans} + d_{prop}$$

- **d_proc:** fixo, exame do cabeçalho
- **d_fila:** único que varia com o tráfego
- **d_trans = L/R:** fixo (pacote + enlace)
- **d_prop = m/s:** fixo (distância física + velocidade do sinal, independe de L)
- **d_empacotamento** (visto no P7/VoIP): tempo para acumular bits suficientes pra formar um pacote

### 6. Intensidade de tráfego (I = La/R) e atraso de fila

- **I → 0:** fila quase inexistente | **I = 1:** rajadas causam fila → atraso médio tende ao infinito | **I > 1:** fila cresce sem limite → **perda de pacotes**
- **Lei de Little / teoria de filas (M/M/1):** $N = I/(1-I)$ — número médio de pacotes no sistema, derivável tanto via Lei de Little quanto via cadeia de Markov (nascimento-morte), com resultado idêntico

### 7. Vazão (throughput)

- Vazão média = F/T; limitada pelo **enlace gargalo**: $\min(R_1,...,R_N)$
- **Packet pair:** intervalo de chegada de 2 pacotes back-to-back no destino revela a taxa do enlace gargalo (L/Rs)

### 8. Camadas de protocolo (5 camadas do modelo Internet)

1. **Aplicação** (HTTP, SMTP, DNS...)
2. **Transporte** (TCP, UDP) — entre processos
3. **Rede** (IP) — roteamento, datagramas
4. **Enlace** (Ethernet, Wi-Fi) — nó a nó adjacente
5. **Física** — bits → sinais físicos

- **Vantagem:** modularidade (mudar uma camada sem afetar as outras)
- **Desvantagens:** (1) redundância de funcionalidade entre camadas, (2) ocultação de informação entre camadas
- **Encapsulamento:** cada camada adiciona seu cabeçalho aos dados de cima (mensagem → segmento → datagrama → quadro); desencapsulamento no destino faz o processo inverso
- **Dispositivos e camadas:** hosts implementam as 5; roteadores implementam física+enlace+rede; switches implementam só física+enlace
