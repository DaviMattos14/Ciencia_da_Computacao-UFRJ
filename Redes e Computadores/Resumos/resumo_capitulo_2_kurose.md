# Resumo — Capítulo 2: Camada de Aplicação (Kurose & Ross, 8ª ed.)

## Sumário
1. Princípios de aplicações de rede
2. A Web e o HTTP
3. Correio eletrônico
4. DNS
5. Aplicações P2P
6. Streaming de vídeo e CDNs
7. Programação de sockets
8. Glossário completo
9. Exercícios resolvidos (referência)

---

## 1. Princípios de aplicações de rede

**Princípio fim-a-fim (end-to-end principle):** toda a "inteligência" de uma aplicação de rede mora nos **hosts** (bordas da rede). Roteadores e switches não entendem nada de HTTP, e-mail, etc. — só encaminham pacotes. Por isso, criar uma nova aplicação não exige modificar o núcleo da rede.

**Processos, não hosts, se comunicam.** Um host pode rodar vários processos simultaneamente (navegador, e-mail, WhatsApp), todos usando o mesmo endereço IP. Para identificar o processo certo, é preciso **endereço IP + número de porta**.

**Socket:** a interface entre o processo (aplicação) e a camada de transporte — a "porta de entrada/saída" por onde a aplicação escreve e lê dados da rede.

**Portas padronizadas:**
| Porta | Protocolo |
|---|---|
| 80 | HTTP |
| 443 | HTTPS |
| 25 | SMTP |
| 53 | DNS |

**Exigências de serviço da camada de transporte (4 dimensões):**
1. Confiabilidade de dados (perda é tolerável?)
2. Vazão (precisa de taxa mínima garantida?)
3. Temporização (é sensível a atraso?)
4. Segurança (precisa de criptografia/autenticação?)

**TCP vs. UDP:**
| | TCP | UDP |
|---|---|---|
| Confiabilidade | Garantida (retransmite) | "Melhor esforço" |
| Ordem | Garante ordem | Não garante |
| Controle de congestionamento | Sim | Não |
| Orientado a conexão | Sim (handshake) | Não |
| Atraso | Maior (pelas garantias) | Menor, mais previsível |
| Uso típico | HTTP, e-mail, arquivos | VoIP, videochamada, jogos, streaming ao vivo |

**Exemplo simples:** baixar um PDF tolera atraso mas não tolera perda (TCP); uma videochamada tolera pequenas perdas mas não tolera atraso (UDP).

---

## 2. A Web e o HTTP

**URL:** nome do host + caminho do objeto dentro daquele host.

**HTTP é stateless** (sem estado) — cada requisição é independente. O "estado" (ex: carrinho de compras) é simulado via **cookies**.

**Como funcionam os cookies (4 componentes):**
1. Cabeçalho `Set-Cookie:` na resposta (servidor "planta" o cookie)
2. Cabeçalho `Cookie:` na requisição seguinte (navegador devolve automaticamente)
3. Arquivo de cookie no navegador
4. Banco de dados no backend do site

**Cookies de terceiros:** permitem que anunciantes rastreiem o usuário através de múltiplos sites — motivo de preocupação com privacidade.

**Cache Web (proxy):** servidor intermediário perto dos usuários que guarda cópias de objetos já requisitados.

**Conexão com teoria de filas:** se $p_{hit}$ é a fração de acertos de cache, a taxa efetiva que atravessa o enlace de acesso (gargalo) cai para $\lambda_{efetivo} = \lambda \cdot p_{miss}$, reduzindo a intensidade de tráfego $I = \lambda_{efetivo}/\mu$ — e, pela não-linearidade de $N=I/(1-I)$, uma pequena redução em I gera queda desproporcional no atraso de fila.

**GET condicional:** evita reenviar objetos não modificados.
1. Cache guarda a data de `Last-Modified:`
2. Próxima requisição: `GET ... If-modified-since: <data>`
3. Se não mudou → servidor responde `304 Not Modified` (sem corpo, $d_{trans}$ mínimo)
4. Se mudou → `200 OK` com o objeto novo completo

**Modelos de conexão HTTP (persistência × paralelismo):**
| | Sem Paralelismo | Com Paralelismo |
|---|---|---|
| **Não Persistente** | $2(n+1)$ RTT | $\approx 4$ RTT |
| **Persistente** | $(n+2)$ RTT | $2\text{RTT}+\max(\ldots)$ |

(n = número de objetos adicionais além do HTML; cada handshake TCP custa 1 RTT)

**Evolução do HTTP:**
- **HTTP/1:** respostas inteiras, FIFO — sofre de **Head-of-Line Blocking** (objeto grande trava os pequenos atrás dele)
- **HTTP/2:** ainda sobre TCP, mas com **interleaving** — quebra objetos em partes intercaladas na mesma conexão
- **HTTP/3:** abandona TCP, roda sobre UDP com o protocolo **QUIC** — reimplementa confiabilidade e criptografia por conta própria, mas com **streams independentes**, resolvendo o head-of-line blocking de forma definitiva (perda em um stream não trava os outros)

---

## 3. Correio eletrônico

**Três componentes:** agentes de usuário, servidores de correio, e o protocolo **SMTP**.

**SMTP é um protocolo de "empurrar" (push):** o servidor de origem inicia ativamente a conexão para empurrar a mensagem.

**Fluxo completo do e-mail:**
$$\underbrace{\text{Você} \to \text{Seu servidor}}_{\text{SMTP (push)}} \to \underbrace{\text{Seu servidor} \to \text{Servidor destinatário}}_{\text{SMTP (push)}} \to \underbrace{\text{Servidor} \to \text{Destinatário}}_{\text{IMAP/POP3 (pull)}}$$

**Leitura de e-mail é "puxar" (pull):** o cliente do destinatário precisa **consultar** o servidor ("tem mensagem nova?"), usando um protocolo diferente:
- **POP3:** mais simples, geralmente baixa e remove do servidor, não sincroniza bem entre dispositivos
- **IMAP:** mais moderno, mantém mensagens organizadas em pastas no servidor, sincroniza entre múltiplos dispositivos

---

## 4. DNS (Domain Name System)

**Por que existe:** tradução nome de domínio ↔ endereço IP. Duas vantagens de separar nome de IP:
1. **Mnemônico:** nomes são mais fáceis de lembrar que números
2. **Indireção/flexibilidade:** um site pode trocar de servidor sem que ninguém precise saber; um nome pode apontar para vários servidores (balanceamento, CDN); vários nomes podem apontar para o mesmo servidor

**Por que não um servidor DNS único e centralizado (4 problemas):**
1. Ponto único de falha — se cair, toda a Internet para
2. Volume de tráfego — bilhões de consultas globais
3. Distância física — atraso de propagação para usuários longe
4. Manutenção — gerenciar todos os domínios do mundo seria inviável

**Hierarquia de servidores DNS (3 níveis):**
1. **Servidores raiz** — topo da hierarquia
2. **Servidores TLD** — um para cada terminação (.com, .org, .br)
3. **Servidores autoritativos** — donos do mapeamento final de um domínio específico

**Consulta recursiva vs. iterativa:**
- **Recursiva** (host → servidor DNS local): o servidor local assume toda a responsabilidade e devolve a resposta pronta — porque o host tem recursos limitados
- **Iterativa** (servidor local → hierarquia raiz/TLD/autoritativo): cada servidor só responde "pergunta a este outro" — distribui a carga de trabalho entre os servidores da hierarquia

**Registros de recursos (RR):** formato (nome, valor, tipo, TTL)
| Tipo | Função |
|---|---|
| **A** | Nome de host → endereço IP |
| **NS** | Domínio → servidor de nomes autoritativo |
| **CNAME** | Apelido → nome canônico real (esconde detalhes internos de infraestrutura) |
| **MX** | Domínio → servidor de e-mail |

**Cache DNS:** servidores locais guardam mapeamentos já resolvidos por um tempo definido pelo **TTL**, reduzindo carga na hierarquia superior.

---

## 5. Aplicações P2P

**Distribuição de arquivo (F bits, N peers) — Cliente-Servidor:**

$$t_{cliente-servidor} \geq \max\left(\frac{NF}{u_s}, \frac{F}{d_{min}}\right)$$

- $NF/u_s$: gargalo é o servidor tendo que enviar N cópias
- $F/d_{min}$: gargalo é o peer mais lento para baixar

**Distribuição de arquivo — P2P:**

$$t_{P2P} \geq \max\left(\frac{F}{u_s}, \frac{NF}{u_s+\sum_{i=1}^{N}u_i}\right)$$

- $F/u_s$: servidor precisa injetar ao menos 1 cópia completa na rede
- $NF/(u_s+\sum u_i)$: capacidade agregada do sistema (servidor + todos os peers)

**Autoescalabilidade (self-scalability):** no cliente-servidor, $NF/u_s$ cresce linearmente com N (mais usuários = mais lento). No P2P, cada novo peer traz sua própria capacidade $u_i$, então o denominador cresce junto com o numerador — o sistema escala muito melhor.

---

## 6. Streaming de vídeo e CDNs

**DASH (Dynamic Adaptive Streaming over HTTP):** vídeo dividido em chunks pequenos, cada um codificado em múltiplas taxas de bits. O cliente escolhe, chunk a chunk, a melhor qualidade que a banda disponível permite — priorizando **continuidade** sobre qualidade máxima constante (evitar travamentos).

**CDN (Content Delivery Network):** replica conteúdo em servidores espalhados geograficamente, atendendo cada usuário pelo servidor mais próximo.

**Cache Web vs. CDN:**
- Cache Web: **reativo** — só armazena depois de uma primeira requisição (sofre cache miss na primeira vez)
- CDN: **proativo/planejado** — a empresa de conteúdo pré-posiciona o conteúdo antes de qualquer requisição local

**Duas estratégias de CDN:**
- **Enter Deep:** muitos servidores, entrando fundo nas redes de acesso locais
- **Bring Home:** poucos clusters grandes, em pontos de troca de tráfego (IXPs)

**Como a CDN direciona o usuário:** via DNS — a resolução do domínio da CDN devolve o IP do servidor mais apropriado para aquele usuário específico.

---

## 7. Programação de sockets

**UDP (sem conexão):**
- Não há `connect()` prévio
- Cada `sendto()` precisa informar o endereço de destino (IP+porta) — como cartas avulsas pelo correio, sem "sessão" contínua
- Um mesmo socket pode enviar para destinatários diferentes

**TCP (orientado a conexão):**
- Cliente usa `connect()` uma única vez, antes de qualquer troca de dados
- Depois do `connect()`, `send()`/`recv()` não precisam mais de endereço — já embutido na conexão
- **Servidor usa DOIS sockets:**
  - `serverSocket` (welcoming socket): fica sempre "escutando" novas conexões via `accept()` — como uma recepcionista fixa
  - `connectionSocket`: criado a cada `accept()`, dedicado a um cliente específico — como um atendente designado

**Por que dois sockets no servidor TCP:** se fosse um único socket, o servidor não conseguiria simultaneamente "conversar" com um cliente já conectado E "escutar" novas conexões chegando.

| | UDP | TCP |
|---|---|---|
| Conexão prévia | Não | Sim (`connect()`) |
| Endereço em cada envio | Sim | Não |
| Sockets no servidor | 1 | 2 (escuta + 1 por cliente) |

---

## 8. Glossário completo

| Termo | Significado |
|---|---|
| Socket | Interface entre processo e camada de transporte |
| Porta | Número que identifica um processo específico dentro de um host |
| Cookie | Mecanismo para simular estado sobre HTTP (stateless) |
| Cache Web / Proxy | Servidor intermediário que guarda cópias de objetos já requisitados |
| GET condicional | Requisição HTTP que evita reenviar objetos não modificados |
| RTT | Round-Trip Time — tempo de ida e volta de uma mensagem |
| Head-of-Line Blocking | Objeto grande "trava" a entrega de objetos pequenos atrás dele |
| Interleaving | Técnica do HTTP/2 de intercalar partes de objetos diferentes numa mesma conexão |
| QUIC | Protocolo sobre UDP usado pelo HTTP/3, com streams independentes |
| SMTP | Protocolo de "empurrar" e-mail entre servidores |
| IMAP/POP3 | Protocolos de "puxar" e-mail do servidor para o cliente |
| DNS | Sistema distribuído de tradução nome ↔ IP |
| Registro de recursos (RR) | Entrada no banco de dados DNS: (nome, valor, tipo, TTL) |
| CNAME | Registro DNS de apelido → nome canônico |
| P2P | Arquitetura onde peers compartilham arquivos entre si, sem depender só de um servidor |
| Autoescalabilidade | Propriedade do P2P onde novos usuários também trazem capacidade extra |
| DASH | Streaming adaptativo que ajusta qualidade do vídeo conforme banda disponível |
| CDN | Rede de servidores que replica conteúdo geograficamente |
| Welcoming socket | Socket TCP do servidor dedicado a aceitar novas conexões |

---

## 9. Exercícios resolvidos (referência)

- **P4:** parsing de mensagem HTTP GET capturada
- **P7/P8:** cálculo de tempo total (RTTs de DNS + HTTP) para diferentes modelos de conexão
- **P9:** cache Web e cálculo de atraso médio de resposta (com e sem cache)
- **P10:** comparação numérica entre HTTP persistente e não persistente
- **P13:** HTTP/2 — interleaving reduz o tempo médio de transmissão de objetos (mesmo makespan, menor tempo médio) — princípio análogo a "menor trabalho primeiro" em escalonamento
- **P23:** distribuição de arquivo — arquitetura cliente-servidor
- **P24:** distribuição de arquivo — arquitetura P2P (autoescalabilidade)

---

*Resumo elaborado a partir do Capítulo 2 de Kurose & Ross, "Computer Networking: A Top-Down Approach", 8ª edição americana.*
