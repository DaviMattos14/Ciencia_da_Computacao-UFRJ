# Resumo Unificado — Livro (Kurose 8ed) + Notas de Aula
## Capítulos 1 e 2, com a linha de raciocínio explícita entre teoria estrutural e análise matemática

---

## Como usar este documento

Cada tópico é tratado em quatro partes, escritas por extenso:

1. **O que é** — a explicação conceitual, como o livro apresenta
2. **Existe disputa por recurso?** — o filtro que decide se a matemática entra ou não
3. **Se sim, qual o recurso e quem disputa ele** — a "tradução" do conceito de rede para uma linguagem de "vários agentes competindo por uma capacidade finita"
4. **A ferramenta matemática e por que ela se aplica** — a fórmula, de onde ela vem, e o que ela responde fisicamente

Quando a resposta da parte 2 for "não", as partes 3 e 4 são omitidas — esses são tópicos puramente estruturais, e é importante você não tentar forçar uma conexão matemática onde ela não existe.

---

# CAPÍTULO 1 — Introdução

## 1. Visão da Internet (Aula 1)

**O que é.** O livro descreve a Internet de duas formas complementares. A visão física a define como um conjunto de hosts (sistemas finais), enlaces de comunicação e comutadores de pacotes (roteadores e switches) interligados. A visão de serviço a descreve como uma infraestrutura que oferece serviços de comunicação a aplicações distribuídas, através de APIs e protocolos, sem que a aplicação precise conhecer os detalhes internos.

**Existe disputa por recurso?** Não, neste nível. Esta seção é puramente definicional — está estabelecendo o vocabulário (host, enlace, comutador de pacotes) que será usado no resto do livro. Nenhuma fórmula é necessária aqui.

---

## 2. Borda da rede e redes de acesso (Aula 2)

**O que é.** A borda da rede é onde ficam os hosts. A rede de acesso é o "primeiro salto" que conecta um host à rede do provedor — pode ser DSL (par de cobre, dedicado), HFC/cabo (fibra + coaxial, compartilhado entre vizinhos), FTTH (fibra até a casa) ou acesso sem fio (Wi-Fi via ponto de acesso, ou celular via estação-base).

**Existe disputa por recurso?** Parcialmente, e é importante notar isso: no caso do **HFC**, as notas de aula mencionam explicitamente que "usuários vizinhos podem compartilhar capacidade" — isso já é, embrionariamente, o mesmo tipo de disputa que será formalizada matematicamente mais adiante (Aula 4). Mas nesse ponto do curso, o livro ainda trata isso apenas de forma qualitativa, sem fórmula. A comparação DSL (dedicado) vs. HFC (compartilhado) é conceitual — prepara terreno para a distinção circuitos vs. pacotes que vem a seguir, mas ainda não exige cálculo.

---

## 3. Núcleo da rede: comutação de circuitos vs. pacotes, store-and-forward (Aula 3)

**O que é.** Na comutação de circuitos, os recursos de um enlace são reservados antes da transmissão (via FDM, TDM ou CDMA), garantindo taxa constante mas desperdiçando capacidade durante períodos ociosos. Na comutação de pacotes, os dados são divididos em pacotes que compartilham enlaces e buffers sob demanda — sem reserva fixa, aproveitando melhor a capacidade agregada, mas sujeitos a fila, atraso e perda. O store-and-forward é a regra segundo a qual um roteador só começa a retransmitir um pacote depois de tê-lo recebido por completo.

**Existe disputa por recurso?** Sim, e esta é a primeira aparição explícita do conceito central deste curso: múltiplos usuários competindo por um enlace de capacidade finita. Mas nesse ponto o livro ainda trata o tema qualitativamente (a tabela comparativa "recursos reservados vs. compartilhados") — a formalização matemática dessa disputa (quantos usuários ativos ao mesmo tempo o enlace suporta) só vem na Aula 4.

**O recurso e quem disputa.** O recurso é a capacidade de transmissão R de um enlace. Quem disputa são os usuários (ou os pacotes que eles geram) que precisam desse enlace para transmitir seus dados.

**A ferramenta matemática (nesta seção, ainda limitada).** Aqui a matemática se resume ao atraso de transmissão de um único pacote, d_trans = L/R, e sua generalização para N enlaces em pipeline, (N+P-1)L/R para P pacotes. Isso não é ainda "teoria de disputa" — é uma contagem determinística de tempo, sem aleatoriedade envolvida. A disputa probabilística só aparece na próxima seção.

---

## 4. Multiplexação estatística e as quatro distribuições (Aula 4 e Aula 7 — Parte A das notas)

**O que é.** Esta é a seção em que o professor introduz formalmente a matemática que vai sustentar todo o resto do curso. O ponto de partida é o problema de dimensionamento: m usuários compartilham um enlace com capacidade para atender r simultaneamente; cada usuário está ativo com probabilidade p. Quer-se saber a probabilidade de a demanda ultrapassar a capacidade.

**Existe disputa por recurso?** Sim — esta é a formalização matemática exata da disputa que foi apenas mencionada qualitativamente na Aula 3. Agora ela ganha números.

**O recurso e quem disputa.** O recurso é a capacidade r do enlace (quantos usuários ele consegue atender simultaneamente). Quem disputa são os m usuários, cada um contribuindo com uma variável de Bernoulli Z_i (ativo ou não).

**A ferramenta matemática.** A soma dessas m variáveis de Bernoulli é uma variável Binomial, A ~ Bin(m,p), com Pr(A=a) = C(m,a) p^a (1-p)^(m-a). Quando m é grande e p é pequeno, com o produto λ=mp mantido moderado, a Binomial converge para uma Poisson, Pr(W=w) = e^(-λ) λ^w/w!. Uma quarta distribuição, a Geométrica, responde a uma pergunta relacionada mas distinta: não "quantos estão ativos agora", mas "quantos slots de tempo até o sistema voltar a ficar descongestionado" — Pr(S=s) = (1-q)^(s-1) q. A Binomial modela uma fotografia instantânea do sistema; a Geométrica modela uma dinâmica temporal de recuperação.

---

## 5. Atraso, perda e vazão — os quatro componentes do atraso nodal (Aula 3 e continuação em Aula 5)

**O que é.** Todo pacote que atravessa um roteador sofre quatro tipos de atraso: processamento (exame do cabeçalho), fila (espera no buffer de saída), transmissão (L/R) e propagação (distância dividida pela velocidade do sinal).

**Existe disputa por recurso?** Depende do componente específico, e essa distinção é o cerne do que separa "estrutural" de "matemático" dentro desta mesma seção. Processamento, transmissão e propagação são fixos — não dependem de quantos outros pacotes estão competindo pelo mesmo enlace naquele momento, então não precisam de nenhuma ferramenta probabilística. A fila é o único componente que varia com o tráfego, porque é exatamente onde a disputa por recurso acontece de fato.

**O recurso e quem disputa (apenas para o atraso de fila).** O recurso é o buffer de saída do roteador (e, por trás dele, a capacidade de transmissão do enlace). Quem disputa são os pacotes de múltiplos fluxos que chegam a esse roteador e precisam esperar sua vez de ser transmitidos.

**A ferramenta matemática.** A intensidade de tráfego I = La/R (ou λL/R, dependendo da notação) quantifica essa disputa como uma fração da capacidade sendo demandada. Quando I se aproxima de 1, o atraso médio de fila cresce sem limite — esse comportamento não-linear é o que a teoria de filas, desenvolvida a partir da Aula 5 em diante, formaliza precisamente.

---

## 6. Teoria de filas — Lei de Little e o modelo M/M/1 (Aulas 5, 6 e 8)

**O que é.** Um roteador com um enlace de saída pode ser modelado como um sistema de fila com um único servidor: pacotes chegam a uma taxa λ, esperam em uma fila se o servidor (o enlace) estiver ocupado, e são atendidos (transmitidos) a uma taxa μ = R/L.

**Existe disputa por recurso?** Sim, de forma central e explícita — esta é a formalização completa e rigorosa da disputa que vínhamos descrevendo qualitativamente desde a Aula 3.

**O recurso e quem disputa.** O recurso é o único servidor (o enlace de saída, com capacidade de transmitir μ pacotes por segundo). Quem disputa são os pacotes que chegam a uma taxa média λ, potencialmente vindos de múltiplos fluxos diferentes sendo multiplexados estatisticamente no mesmo enlace.

**A ferramenta matemática.** A Lei de Little, N = λT (e suas versões para cada "compartimento": N_q = λW para a fila, N_s = λS para o servidor), é uma relação de conservação válida para qualquer fila, independente da distribuição das chegadas ou do serviço — ela não calcula W ou T sozinha, apenas garante consistência entre número médio de pacotes, taxa de chegada e tempo médio no sistema. Para obter fórmulas fechadas, é necessário assumir hipóteses adicionais: no modelo M/M/1 (chegadas Poisson, serviço exponencial), chega-se a W = I/(μ-λ), T = 1/(μ-λ) e N = I/(1-I). A condição de estabilidade I<1 é necessária sempre que existe aleatoriedade (a exceção sendo o caso D/D/1, perfeitamente determinístico, que pode ter I=1 estável).

---

## 7. Tempo residual de serviço e a comparação M/M/1 vs. M/D/1 (Aula 8)

**O que é.** Quando um pacote chega e encontra o servidor ocupado, ele não espera o tempo de serviço completo do pacote em transmissão — espera apenas o que resta dele, o chamado tempo residual S_R.

**Existe disputa por recurso?** Sim — esta é uma extensão mais fina da mesma disputa do item anterior, agora examinando com precisão o que acontece com o pacote que já está sendo atendido no momento da chegada de um novo pacote.

**O recurso e quem disputa.** O mesmo de antes (o servidor único), mas agora o foco está especificamente na fração de trabalho já realizada versus a fração que ainda falta, no pacote que está em atendimento.

**A ferramenta matemática.** A fórmula geral S_R = E[S²]/(2E[S]) mostra que o tempo residual depende do segundo momento do tempo de serviço, não apenas da média — por isso, dois sistemas com a mesma intensidade de tráfego I podem ter atrasos médios diferentes, dependendo da variabilidade do tempo de serviço. Para serviço exponencial (M/M/1), a propriedade de falta de memória faz S_R = S; para serviço determinístico (M/D/1), o paradoxo da inspeção faz S_R = S/2, resultando em W_(M/D/1) = (1/2) W_(M/M/1).

---

## 8. Perda de pacotes e vazão (retomado ao longo das aulas, formalizado nos exercícios)

**O que é.** Perda ocorre quando o buffer de um roteador está cheio e um pacote chega — ele é descartado. Vazão é a taxa efetiva de transferência de dados, limitada pelo enlace mais lento do caminho (o gargalo).

**Existe disputa por recurso?** Para perda, sim — é a consequência extrema da mesma disputa por buffer já discutida (quando I ultrapassa 1 de forma sustentada, ou quando rajadas de tráfego excedem a capacidade do buffer finito). Para vazão/gargalo, a lógica é diferente: não é bem uma "disputa", é uma restrição estrutural — o caminho todo não pode ir mais rápido que seu elo mais fraco.

**A ferramenta matemática.** Para perda em um caminho com N enlaces com probabilidade de perda independente p em cada um, a probabilidade de sucesso é (1-p)^N, e o número médio de retransmissões necessárias segue uma distribuição Geométrica, com média 1/(1-p)^N. Para vazão, a fórmula é simplesmente o mínimo das taxas dos enlaces do caminho, min(R1,...,RN) — sem necessidade de ferramentas probabilísticas.

---

## 9. Camadas de protocolo e encapsulamento (Aulas 7-8)

**O que é.** A pilha da Internet tem cinco camadas — física, enlace, rede, transporte, aplicação — cada uma provendo serviço à camada acima usando os serviços da camada abaixo. Cada camada adiciona seu próprio cabeçalho aos dados vindos de cima (encapsulamento).

**Existe disputa por recurso?** Não. Esta é uma seção inteiramente estrutural/organizacional, sobre como o software de rede é dividido em módulos independentes. Não há competição por capacidade aqui — é sobre modularidade de design, com suas vantagens (facilidade de manutenção) e desvantagens (redundância de funcionalidade entre camadas, ocultação de informação entre camadas). Nenhuma fórmula matemática se aplica a este tópico.

---

# CAPÍTULO 2 — Camada de Aplicação

## 10. Princípios de aplicações de rede (início do Capítulo 2, ainda não coberto nas notas de aula até a Aula 10)

**O que é.** O princípio fim-a-fim estabelece que toda a inteligência de uma aplicação reside nos hosts, não no núcleo da rede. Processos (não hosts) se comunicam, identificados pela combinação endereço IP + porta, através de uma interface chamada socket.

**Existe disputa por recurso?** Não, para a parte de endereçamento (IP+porta, sockets) — isso é puramente sobre identificação e roteamento correto de dados até o processo certo. Para a escolha entre TCP e UDP, existe uma disputa implícita entre confiabilidade e velocidade, mas isso é tratado qualitativamente aqui (a formalização rigorosa de custo de retransmissão viria no Capítulo 3, controle de congestionamento do TCP, que ainda não estudamos).

---

## 11. Web e HTTP — cookies, GET condicional, modelos de conexão (Aula 9, e Seção 2.2 do livro)

**O que é.** HTTP é stateless; cookies simulam estado através de um mecanismo de quatro componentes (cabeçalhos Set-Cookie/Cookie, arquivo local, banco de dados no servidor). O GET condicional evita reenviar objetos não modificados. Os modelos de conexão HTTP combinam persistência (conexão TCP reaproveitada ou não) com paralelismo (uma ou várias conexões simultâneas).

**Existe disputa por recurso?** Para cookies e GET condicional, não — são mecanismos de estado e eficiência, sem disputa por capacidade compartilhada. Para os modelos de conexão HTTP, sim, mas de uma forma específica: o recurso disputado não é banda em si, é RTTs (tempo de ida e volta) — cada handshake TCP consome um RTT, e a pergunta é quantos desses "slots de tempo" são necessários no total.

**O recurso e quem disputa.** No caso dos modelos de conexão, o "recurso" conceitual é o tempo total até a página carregar, e os "competidores" são os múltiplos objetos (HTML, imagens) que precisam, cada um, de uma requisição/resposta.

**A ferramenta matemática.** Aqui não é teoria de filas probabilística — é contagem determinística de RTTs: 2(n+1) RTT para não-persistente sem paralelismo, (n+2) RTT para persistente sem paralelismo, aproximadamente 4 RTT para os modelos com paralelismo. É uma matemática mais simples (aritmética/combinatória), mas segue a mesma lógica de "quantificar o custo de compartilhar/disputar um recurso limitado no tempo".

---

## 12. Cache Web (Seção 2.2 do livro) — o ponto de reencontro mais direto com a teoria de filas do Capítulo 1

**O que é.** Um cache Web é um servidor intermediário que guarda cópias de objetos já requisitados, evitando que toda requisição precise atravessar até o servidor de origem.

**Existe disputa por recurso?** Sim, e este é um dos exemplos mais claros de como um conceito do Capítulo 2 (cache) se conecta diretamente com a matemática construída no Capítulo 1 (teoria de filas). O recurso disputado é o enlace de acesso entre a rede local (por exemplo, a universidade) e a Internet.

**O recurso e quem disputa.** O enlace de acesso, com capacidade μ, é disputado pelas requisições de todos os usuários da rede local. Sem cache, todas as requisições, na taxa λ, disputam esse enlace. Com cache, apenas a fração p_miss das requisições precisa atravessá-lo.

**A ferramenta matemática.** A taxa efetiva que atravessa o enlace cai para λ_efetivo = λ · p_miss, reduzindo a intensidade de tráfego para I_efetivo = λ_efetivo/μ. Como o atraso de fila cresce de forma não-linear conforme I se aproxima de 1 (lembrando de N=I/(1-I)), mesmo uma redução moderada em I, especialmente se o sistema estava próximo da saturação, gera uma queda desproporcionalmente grande no atraso — o que explica por que instalar um cache costuma ser mais custo-efetivo do que simplesmente ampliar a capacidade do enlace.

---

## 13. HTTP/2, interleaving e o problema do exercício P13 (Seção 2.2 do livro)

**O que é.** HTTP/1 sofre de head-of-line blocking: um objeto grande, enviado inteiro antes dos demais, atrasa a entrega de objetos pequenos atrás dele. HTTP/2 resolve isso quebrando objetos em partes intercaladas (interleaving) dentro da mesma conexão.

**Existe disputa por recurso?** Sim — o recurso disputado é a própria conexão TCP (mais especificamente, sua capacidade de transmissão), e quem disputa são os diferentes objetos (vídeo, imagens) que precisam ser enviados através dela.

**O recurso e quem disputa.** A conexão TCP única é o recurso; os objetos de tamanhos diferentes (um vídeo grande, várias imagens pequenas) são os competidores por essa capacidade.

**A ferramenta matemática.** Embora não seja teoria de filas probabilística, o princípio matemático subjacente é o mesmo espírito de "ordem de atendimento importa": o makespan total (tempo até tudo terminar) é idêntico independentemente da ordem, mas o tempo médio de conclusão dos objetos individuais muda drasticamente conforme a ordem de serviço — exatamente o mesmo princípio de escalonamento "menor trabalho primeiro" que minimiza tempo médio de espera em sistemas de fila.

---

## 14. Correio eletrônico — SMTP, IMAP/POP3 (Seção 2.3 do livro)

**O que é.** SMTP é um protocolo de "empurrar" (push) usado tanto para o envio inicial quanto para a retransmissão entre servidores de correio. A leitura de e-mail usa protocolos de "puxar" (pull) — IMAP ou POP3 — porque o cliente precisa consultar ativamente o servidor.

**Existe disputa por recurso?** Não. Esta seção é inteiramente sobre a direção da iniciativa de comunicação (quem inicia a conexão) e a arquitetura de protocolos separados para funções diferentes — não há competição por capacidade compartilhada sendo modelada aqui.

---

## 15. DNS (Seção 2.4 do livro)

**O que é.** O DNS é um banco de dados distribuído, organizado em hierarquia (raiz, TLD, autoritativo), que traduz nomes de domínio em endereços IP através de registros de recursos (A, NS, CNAME, MX), usando consultas recursivas (do host ao servidor local) e iterativas (do servidor local pela hierarquia).

**Existe disputa por recurso?** Não diretamente na operação do DNS em si, mas os motivos para não usar um servidor único e centralizado reaproveitam, implicitamente, conceitos já vistos no Capítulo 1: o problema de "volume de tráfego" é o mesmo que motivou a multiplexação estatística (muitos usuários, um recurso limitado), e o problema de "distância física" é exatamente o atraso de propagação (d_prop) que já formalizamos. O CNAME e o cache DNS são mecanismos estruturais, sem matemática associada.

---

## 16. Aplicações P2P (Seção 2.5 do livro)

**O que é.** Na distribuição de um arquivo de F bits para N peers, a arquitetura cliente-servidor depende inteiramente da capacidade de upload do servidor, enquanto a arquitetura P2P aproveita também a capacidade de upload de cada peer que já recebeu partes do arquivo.

**Existe disputa por recurso?** Sim, de forma muito clara — o recurso é a capacidade de upload (do servidor, e no caso P2P, também dos peers), disputada pela necessidade de entregar o arquivo completo a todos os N usuários.

**O recurso e quem disputa.** Na arquitetura cliente-servidor, apenas o servidor (capacidade u_s) precisa suprir todos os N peers. Na arquitetura P2P, o total de capacidade disponível é u_s mais a soma das capacidades de upload de todos os peers.

**A ferramenta matemática.** Embora não seja teoria de filas no sentido estrito, a lógica matemática é a mesma "trabalho total dividido por capacidade total" que sustenta toda a teoria de filas: para cliente-servidor, o tempo mínimo é max(NF/u_s, F/d_min); para P2P, é max(F/u_s, NF/(u_s+soma dos u_i)). A diferença estrutural entre os dois — o denominador do segundo termo crescer junto com N no caso P2P — é o que explica matematicamente a propriedade de autoescalabilidade.

---

## 17. Streaming de vídeo e CDN (Seção 2.6 do livro)

**O que é.** DASH divide o vídeo em pequenos pedaços codificados em múltiplas taxas de bits, permitindo ao cliente adaptar a qualidade conforme a banda disponível. CDNs replicam conteúdo em servidores geograficamente distribuídos.

**Existe disputa por recurso?** Sim, implicitamente, em ambos os casos, mas nenhum dos dois é formalizado matematicamente no curso até este ponto — o princípio subjacente ao DASH é adaptar-se dinamicamente à intensidade de tráfego disponível (o mesmo espírito de "medir I e reagir"), e o princípio da CDN é o mesmo do cache Web, apenas de forma proativa em vez de reativa: reduzir quem disputa cada enlace, posicionando o conteúdo mais perto do consumidor.

---

## 18. Programação de sockets (Seção 2.7 do livro)

**O que é.** Sockets UDP não requerem conexão prévia (cada envio especifica o destinatário); sockets TCP requerem um connect() prévio, e o servidor TCP usa dois sockets distintos — um welcoming socket, sempre disponível para aceitar novas conexões, e um connection socket dedicado a cada cliente já conectado.

**Existe disputa por recurso?** Não. Esta seção é sobre a API de programação e a estrutura de comunicação entre processos — é implementação, não modelagem de desempenho sob disputa.

---

# Síntese final

O padrão que percorre os dois capítulos inteiros pode ser resumido assim: o livro descreve, capítulo após capítulo, uma sucessão de mecanismos de rede — alguns puramente estruturais (camadas, sockets, formato de mensagens, DNS, e-mail), outros que envolvem explicitamente múltiplos agentes competindo por um recurso finito (o núcleo da rede, os buffers de roteadores, o enlace de acesso disputado por usuários de um cache, a conexão TCP disputada por objetos HTTP/2, a capacidade de upload disputada em P2P). As notas de aula do professor concentram a construção da ferramenta matemática (distribuições, Lei de Little, modelo M/M/1, tempo residual) logo no início do curso, precisamente para que essa ferramenta já esteja disponível quando, mais adiante, o livro voltar a encontrar situações de disputa por recurso — o que acontece repetidamente, em contextos aparentemente muito diferentes entre si (redes de acesso, cache Web, HTTP/2, P2P), mas que compartilham exatamente a mesma estrutura matemática subjacente.
