##### P4 -- HTTP GET - parsing humano   
  
##### P7 -- web browser  
  
##### P8 -- web browser   
  
##### P9 -- caching -- interessante!   
  
##### P10 -- HTTP persistente x não persistente   
  
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