##### P4 -- HTTP GET - parsing humano   

- **a) Qual é o URL do documento requisitado pelo navegador?**
    - **Resposta:** `[http://gaia.cs.umass.edu/cs453/index.html](http://gaia.cs.umass.edu/cs453/index.html)`.
        
- **b) Qual versão do HTTP o navegador está rodando?**
    - **Resposta:** `HTTP/1.1`.
        
- **c) O navegador requisita uma conexão não persistente ou persistente?**
    - O cabeçalho `Connection: keep-alive` indica reutilização do socket.
    - **Resposta:** Persistente (`keep-alive`).
        
- **d) Qual é o endereço IP do hospedeiro no qual o navegador está rodando?**
    - **Resposta:** **Não é possível determinar**. O endereço IP do cliente pertence aos cabeçalhos do protocolo IP (camada de rede), não estando presente no payload da mensagem HTTP (camada de aplicação).
        
- **e) Qual tipo de navegador inicia essa mensagem? Por que o tipo de navegador é necessário?**
    - **Resposta:** É o `Mozilla/5.0` (Netscape 7.2 no Windows NT 5.1). O servidor usa essa informação para negociar conteúdo e enviar versões formatadas especificamente para aquele navegador.

##### P7 -- web browser  
  1. **Etapa DNS:** Para traduzir o nome de domínio para endereço IP visitando $n$ servidores DNS, o tempo decorrido é a soma das latências individuais: $\sum_{i=1}^{n} RTT_i$.    
2. **Etapa TCP Handshake:** Aberta a conexão, consome-se $1 \cdot RTT_0$ para sincronizar os pacotes SYN e SYN/ACK.
3. **Etapa HTTP Request/Response:** O envio da requisição GET e a recepção do texto HTML consomem mais $1 \cdot RTT_0$ (desprezando o tempo de transmissão físico por ser muito pequeno).
$$\text{Tempo Total} = \left( \sum_{i=1}^{n} RTT_i \right) + 2 \cdot RTT_0$$
##### P8 -- web browser   
##### a) HTTP Não Persistente sem Conexões TCP Paralelas
- Cada objeto exige $1\text{ RTT}_0$ para abrir o TCP e $1\text{ RTT}_0$ para buscar o arquivo.
- Para o arquivo base + $8$ objetos ($9$ objetos no total):
    $$T = RTT_{\text{DNS}} + 2 \cdot RTT_0 + 8 \times (2 \cdot RTT_0) = RTT_{\text{DNS}} + 18 \cdot RTT_0$$
##### b) HTTP Não Persistente com 6 Conexões Paralelas
- **HTML Base:** $RTT_{\text{DNS}} + 2 \cdot RTT_0$.
- **8 Objetos em paralelo (Limite de 6 por vez):**
	- _Lote 1_ (6 objetos em paralelo): $2 \cdot RTT_0$.        
	- _Lote 2_ (2 objetos restantes em paralelo): $2 \cdot RTT_0$.
$$T = RTT_{\text{DNS}} + 2 \cdot RTT_0 + 2 \cdot RTT_0 + 2 \cdot RTT_0 = RTT_{\text{DNS}} + 6 \cdot RTT_0$$
##### c) HTTP Persistente (com Pipelining)
- Conexão aberta no HTML base ($2 \cdot RTT_0$).
- Os $8$ objetos são pedidos juntos numa única rajada e respondidos consecutivamente ($1 \cdot RTT_0$).
$$T = RTT_{\text{DNS}} + 2 \cdot RTT_0 + 1 \cdot RTT_0 = RTT_{\text{DNS}} + 3 \cdot RTT_0$$
##### P9 -- caching -- interessante!   
##### a) Sem Cache Instalação
1. **Taxa de Chegada de Tráfego ($\beta$):**
    $$\beta = 16\text{ req/s} \times 1\text{ Mbit} = 16\text{ Mbps}$$
2. **Utilização do Enlace ($I$):**
    $$I = \frac{16\text{ Mbps}}{15\text{ Mbps}} = 1{,}067$$
3. **Análise:** Como $I > 1$, a fila cresce de forma ilimitada, o atraso de acesso $d_{\text{acesso}} \to \infty$, tornando o **tempo de resposta total infinito** (falha na rede).
##### b) Com Cache Instalado na LAN ($h = 0{,}4$)
1. **Novo tráfego no enlace de acesso:** Apenas a fração não satisfeita localmente ($1 - h = 0{,}6$) passa pelo enlace.
       $$\beta_{\text{novo}} = (1 - 0{,}4) \times 16\text{ Mbps} = 9{,}6\text{ Mbps}$$
2. **Nova Intensidade de Tráfego ($I_{\text{novo}}$):**
$$I_{\text{novo}} = \frac{9{,}6\text{ Mbps}}{15\text{ Mbps}} = 0{,}64$$
3. **Calculando $\Delta$:**    $$\Delta = \frac{1\text{ Mbit}}{15\text{ Mbps}} = 0{,}0667\text{ s}$$
4. **Calculando $d_{\text{acesso}}$:**
    $$d_{\text{acesso}} = \frac{0{,}0667}{1 - 0{,}64} = \frac{0{,}0667}{0{,}36} \approx 0{,}185\text{ s}$$
5. **Calculando o Tempo Médio de Resposta Total ($T_{\text{médio}}$):** (Considerando $d_{\text{LAN}} \approx 0\text{ s}$)   $$T_{\text{médio}} = 0{,}4 \cdot (0) + 0{,}6 \cdot (0{,}185 + 3) = 0{,}6 \cdot (3{,}185) \approx 1{,}911\text{ segundos}$$
##### P10 -- HTTP persistente x não persistente   

##### **Cenário:**

- Enlace de $10\text{ metros}$ com taxa $150\text{ bits/s}$ em ambas as direções.
- Pacote de dados = $100.000\text{ bits}$ ($100\text{ Kbits}$).
- Pacote de controle (ACK/Handshake) = $200\text{ bits}$.
- Página inicial contém $10$ objetos referenciados de $100\text{ Kbits}$.
##### **Análise para Instâncias Paralelas Não Persistentes:**

- **Dividindo a Banda:** Com $N$ conexões paralelas, cada conexão recebe uma fatia igual $\frac{150}{N}\text{ bits/s}$.
- **Conclusão:** Abrir $N$ conexões não persistentes **não traz benefícios reais de tempo de transmissão**, pois a largura de banda total do enlace é fixa ($150\text{ bits/s}$). Na verdade, piora a eficiência total devido ao _overhead_ repetido de pacotes de controle de $200\text{ bits}$ multiplicados por cada handshake.
##### **Análise para HTTP Persistente:**

- **Desempenho:** O HTTP persistente evita $10$ handshakes TCP e economiza pacotes de controle extras no enlace de baixa largura de banda.
- **Ganhos:** **Sim, os ganhos são significativos**, eliminando a latência de controle e a divisão desnecessária de banda em conexões paralelas concorrentes.

##### P13 -- calcule também o tempo médio para a transmissão de objetos em cada caso -- qual o tempo médio de transmissão de objetos no item a)? qual o tempo médio de transmissão de objetos no item b)? explique porque o tempo médio depende da ordem de serviço

- **Vídeo:** 2.000 quadros
- **5 imagens:** 3 quadros cada = 15 quadros no total
- **Total de quadros a enviar:** 2.000 + 15 = **2.015**

a) Sem interleaving (vídeo inteiro primeiro)

O vídeo ocupa os 2.000 primeiros "tempos de quadro"; só depois disso as 5 imagens são enviadas, uma após a outra:

$$2.000 + (5 \times 3) = 2.000 + 15 = \boxed{2.015 \text{ tempos de quadro}}$$

(Esse é o tempo até a **última** imagem terminar.)

b) Com interleaving

Com HTTP/2, os quadros do vídeo e das 5 imagens são intercalados — o servidor envia 1 quadro de cada "stream" por vez, em rodízio (round-robin): vídeo, img1, img2, img3, img4, img5, vídeo, img1, ...

Cada **rodada** consome 6 tempos de quadro (1 de cada stream). Como cada imagem só precisa de **3 quadros**, ela termina após **3 rodadas**:

$$3 \text{ rodadas} \times 6 \text{ streams} = \boxed{18 \text{ tempos de quadro}}$$

(A última imagem — a 5ª — recebe seu quadro final exatamente no tempo de quadro 18.)

 c) Tempo médio de transmissão de objetos — item a) (sem interleaving)

Calculando o instante em que **cada um dos 6 objetos** (vídeo + 5 imagens) termina de ser recebido:

| Objeto   | Termina em (tempo de quadro) |
| -------- | ---------------------------- |
| Vídeo    | 2.000                        |
| Imagem 1 | 2.003                        |
| Imagem 2 | 2.006                        |
| Imagem 3 | 2.009                        |
| Imagem 4 | 2.012                        |
| Imagem 5 | 2.015                        |

$$\text{Tempo médio} = \frac{2000+2003+2006+2009+2012+2015}{6} = \frac{12045}{6} = \boxed{2.007{,}5 \text{ tempos de quadro}}$$

 d) Tempo médio de transmissão de objetos — item b) (com interleaving)

| Objeto   | Termina em (tempo de quadro) |
| -------- | ---------------------------- |
| Imagem 1 | 14                           |
| Imagem 2 | 15                           |
| Imagem 3 | 16                           |
| Imagem 4 | 17                           |
| Imagem 5 | 18                           |
| Vídeo    | 2.015                        |

$$\text{Tempo médio} = \frac{14+15+16+17+18+2015}{6} = \frac{2095}{6} \approx \boxed{349{,}17 \text{ tempos de quadro}}$$

### e) Por que o tempo médio depende da ordem de serviço

O **makespan** (tempo até _tudo_ terminar) é **idêntico** nos dois casos — 2.015 tempos de quadro, já que o total de trabalho (quadros) enviado é o mesmo, não importa a ordem. Mas o **tempo médio de transmissão dos objetos individuais** despenca de ~2.007 para ~349 com o interleaving.

Isso acontece porque, sem interleaving, **todas as 5 imagens pequenas ficam "presas" atrás do vídeo gigante** , mesmo sendo objetos pequenos e rápidos de enviar, elas só começam depois que os 2.000 quadros do vídeo terminam. Com interleaving, as imagens **"furam a fila"** e terminam quase imediatamente (por volta do quadro 14-18), enquanto só o vídeo (que é grande e o usuário já espera demorar) fica para o final.

Isso é exatamente o mesmo princípio de **escalonamento "menor trabalho primeiro" (Shortest Job First)** que minimiza o **tempo médio de espera** em filas — mesmo que o tempo total do sistema não mude, atender primeiro os itens pequenos reduz drasticamente a **média**, porque poucos itens (o vídeo) "puxam" a média pra cima quando são atendidos por último, ao invés de "travarem" todos os outros itens atrás deles.

##### P23 -- esse é muito importante -- fala sobre escalonamento p2p   
  
##### P24 -- também interessante sobre p2p  
  
Site que usa cookies:  
  
Escolha um site que você goste e tente descobrir como que ele usa cookies -- para isso, estude o HTML do site. Indique também quais outros sites são acessados, sem você saber, quando você acessa o site em questão