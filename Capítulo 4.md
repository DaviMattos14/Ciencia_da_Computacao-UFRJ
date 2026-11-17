> **Nome**: Davi dos Santos Mattos            **DRE**: 119133049

#### P4
No mínimo 2 time slots. 
**Time Slot 1:**
    - Fila 1 envia **X** $\rightarrow$ Saída X
    - Fila 2 envia **Y** $\rightarrow$ Saída Y
    - Fila 3 envia **Z** $\rightarrow$ Saída Z
  **Time Slot 2:**
     - Fila 1: vazia
     - Fila 2 envia **X** $\rightarrow$ Saída X
     - Fila 3 envia **Y** $\rightarrow$ Saída Y

No máximo 3 time slot.
**Time Slot 1:**
    - Fila 1 envia **X** $\rightarrow$ Saída X \[BLOQUEADO\]
    - Fila 2 envia **X** $\rightarrow$ Saída X 
    - Fila 3 envia **Z** $\rightarrow$ Saída Z
  **Time Slot 2:**
     - Fila 1:envia **X** $\rightarrow$ Saída X
     - Fila 2 envia **Y** $\rightarrow$ Saída Y 
     - Fila 3 envia **Y** $\rightarrow$ Saída Y \[BLOQUEADO\]
**Time Slot 3:**
     - Fila 1: vazia
     - Fila 2: vazia
     - Fila 3 envia **Y** $\rightarrow$ Saída Y 

#### P8
a)

| Prefixo                   | Interface |
| ------------------------- | --------- |
| `11100000 00` (/10)       | 0         |
| `11100000 01000000` (/16) | 1         |
| `11100000` (/8)           | 2         |
| `11100001 0` (/9)         | 2         |
| *                         | 3         |
b) 

| Endereço                            | Interface |
| ----------------------------------- | --------- |
| 11001000 10010001 01010001 01010101 | 3         |
| 11100001 01000000 11000011 00111100 | 2         |
| 11100001 10000000 00010001 01110111 | 3         |

#### P19

a)
1. Capture todos os pacotes que saem do NAT e anote o identificador de cada um.
2. Separe-os em **cadeias de números consecutivos** (cada pacote que vem depois do `n` com `n+1` pertence à mesma cadeia).
3. O número de cadeias independentes é o número de hosts.

Ela funciona porque cada host tem **seu próprio contador**, e o NAT não altera o campo de identificação. Uma ressalva: como o ponto de partida é aleatório, existe uma chance pequena (não nula) de dois hosts começarem em números muito próximos e as cadeias se confundirem.

b) Não funciona. Com identificadores aleatórios não há correlação entre pacotes consecutivos do mesmo host, então não há como agrupar os pacotes por origem e contar os hosts.

#### P20
- **Conexão direta Arnold → Bernard:** impossível, porque o NAT de Bernard descarta o SYN sem entrada na tabela.
- **Conexão invertida Bernard → Arnold:** impossível, pelo mesmo motivo (Arnold também está atrás de NAT).
- **Solução:** usar um peer público (Cláudio) como **relay**. Ambos iniciam conexões para ele, e ele repassa os dados.
#### P21
Ingress Port = 1 ; IP Src = 10.3.*\.\* ; IP Dst = 10.2.\*.\* → Forward(2)
Ingress Port = 2 ; IP Src = 10.1.\*.\* ; IP Dst = 10.3.\*.\* → Forward(1)
Ingress Port = {1,2} ; IP Src = \*. ; IP Dst = 10.2.0.3 → Forward(3)
Ingress Port = {1,2} ; IP Src = \*. ; IP Dst = 10.2.0.4 → Forward(4)
Ingress Port = 3 ; IP Src = 10.2.0.3 ; IP Dst = 10.2.0.4 → Forward(4)  
Ingress Port = 4 ; IP Src = 10.2.0.4 ; IP Dst = 10.2.0.3 → Forward(3)
#### P22
Ingress Port = 3 ; IP Src = 10.2.0.3 ; IP Dst = {10.3.*\.\*, 10.1.*\.\*} → Forward(2)  
Ingress Port = 4 ; IP Src = 10.2.0.4 ; IP Dst = {10.3.*\.\*, 10.1.*\.\*} → Forward(1)
#### P23

- S1
IP Src = 10.2.\*.\* ; IP Dst = 10.1.0.1 → Forward(2)  
IP Src = 10.2.\*.\*; IP Dst = 10.1.0.2 → Forward(3)
IP Src = 10.2.\*.\*; IP Dst = 10.3.\*.\* → Forward(1)

- S3
IP Src = 10.2.\*.\* ; IP Dst = 10.1.\*.\* → Forward(3)  
IP Src = 10.2.\*.\*; IP IP Dst = 10.3.0.6 → Forward(1)
IP Src = 10.2.\*.\*; IP Dst = 10.3.0.5 → Forward(2)

## Capítulo 5
#### P3

| **Passo** | **N′**      | **D(t),p(t)** | **D(u),p(u)** | **D(v),p(v)** | **D(w),p(w)** | **D(y),p(y)** | **D(z),p(z)** |
| --------- | ----------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| **0**     | $x$         | $\infty$      | $\infty$      | **$3, x$**    | $6, x$        | $6, x$        | $8, x$        |
| **1**     | $\{xv\}$    | $7, v$        | **$6, v$**    | —             | $6, x$        | $6, x$        | $8, x$        |
| **2**     | {$xvu$}     | $7, v$        | —             | —             | **$6, x$**    | $6, x$        | $8, x$        |
| **3**     | {$xvuw$}    | $7, v$        | —             | —             | —             | **$6, x$**    | $8, x$        |
| **4**     | {$xvuwy$}   | **$7, v$**    | —             | —             | —             | —             | $8, x$        |
| **5**     | {$xvuwyt$}  | —             | —             | —             | —             | —             | **$8, x$**    |
| **6**     | {$xvuwytz$} | —             | —             | —             | —             | —             | —             |

#### P5

| Rodada | u        | v   | x   | y        | z   |
| ------ | -------- | --- | --- | -------- | --- |
| 0      | $\infty$ | 6 z | 2 z | $\infty$ | 0   |
| 1      | 7 v      | 5 x | 2 z | 5 x      | 0   |
| 2      | 6 v      | 5 x | 2 z | 5 x      | 0   |

#### P10

Base da Indução ($t = 0 \to t = 1$):

- No instante inicial ($t = 0$), cada nó conhece apenas os custos diretos para seus vizinhos imediatos $v \in N(x)$, definindo:
    $$D_x^{(0)}(y) = \begin{cases} 0, & \text{se } y = x \\ c(x, y), & \text{se } y \in N(x) \\ \infty, & \text{caso contrário} \end{cases}$$
    
- Na iteração $t = 1$, após receber os vetores de distâncias iniciais de seus vizinhos, o nó $x$ atualiza seu vetor pela equação de Bellman-Ford:
    $$D_x^{(1)}(y) = \min_{v \in N(x)} \left\{ c(x, v) + D_v^{(0)}(y) \right\}$$
    
- Como cada vizinho $v$ possui $D_v^{(0)}(v) = 0$, o termo correspondente ao próprio destino $y$ (quando $y \in N(x)$) na operação de mínimo é $c(x, y) + D_y^{(0)}(y) = c(x, y) + 0 = c(x, y) = D_x^{(0)}(y)$
- Portanto, o mínimo tomado sobre todos os vizinhos nunca pode exceder o valor inicial (e para $y \notin N(x)$, qualquer valor finito é estritamente menor que $\infty$):
    $$D_x^{(1)}(y) \le D_x^{(0)}(y) \quad \forall x, y$$

Passo Indutivo ($t \to t + 1$):

- **Hipótese de Indução:** Suponha que, até a iteração $t$, nenhuma estimativa de distância em nenhum nó da rede tenha aumentado, isto é:
    
      
    
    $$D_v^{(t)}(y) \le D_v^{(t-1)}(y) \quad \forall v, y$$
    
- Na iteração $t + 1$, o nó $x$ recalcula sua distância até $y$:
    
      
    
    $$D_x^{(t+1)}(y) = \min_{v \in N(x)} \left\{ c(x, v) + D_v^{(t)}(y) \right\}$$
    
- Como os custos de enlace $c(x, v)$ são constantes e, pela hipótese de indução, $D_v^{(t)}(y) \le D_v^{(t-1)}(y)$ para todo vizinho $v$, cada termo da soma satisfaz:
    
      
    
    $$c(x, v) + D_v^{(t)}(y) \le c(x, v) + D_v^{(t-1)}(y)$$
    
- Logo, o mínimo sobre todos os vizinhos também satisfaz:
    
      
    
    $$\min_{v \in N(x)} \left\{ c(x, v) + D_v^{(t)}(y) \right\} \le \min_{v \in N(x)} \left\{ c(x, v) + D_v^{(t-1)}(y) \right\}$$
    
    $$D_x^{(t+1)}(y) \le D_x^{(t)}(y)$$
    


Estabilização em um Número Finito de Etapas

Para concluir que o algoritmo converge e para em um número finito de passos:

1. **Limitante Inferior (Cota Mínima):**
     - Todos os custos de enlace $c(u, v)$ na rede são estritamente positivos ($c(u, v) > 0$).

    - Qualquer caminho simples entre dois nós distintos $x$ e $y$ em um grafo finito com $N$ nós possui no máximo $N - 1$ enlaces e um custo estritamente positivo. Assim, cada entrada $D_x^{(t)}(y)$ é limitada inferiormente pelo custo real do caminho mínimo $d^*(x, y) > 0$ (e certamente por $0$).

2. **Discretude / Conjunto Finito de Caminhos Possíveis:**

    - Como a rede possui um número finito $N$ de nós, existe apenas um **número finito de caminhos sem laços** possíveis entre $x$ e $y$ (e, consequentemente, um conjunto finito de valores de custo possíveis que $D_x^{(t)}(y)$ pode assumir).

    - Além disso, na versão síncrona, a cada iteração $t$ em que ocorre alguma mudança na rede, o algoritmo incorpora caminhos com pelo menos $t$ saltos. Como nenhum caminho de custo mínimo em um grafo com custos positivos possui laços, ele tem no máximo $N - 1$ enlaces.

3. **Conclusão:**

    - Uma sequência monotonicamente não crescente ($D_x^{(0)}(y) \ge D_x^{(1)}(y) \ge D_x^{(2)}(y) \ge \dots$) que assume valores dentro de um conjunto finito de custos e é limitada inferiormente por $d^*(x, y) > 0$ **não pode decrescer indefinidamente**.

    - Portanto, após um número finito de etapas (no máximo $N - 1$ iterações após o início), nenhum vetor de distâncias sofre mais alterações, o envio de mensagens cessa e o algoritmo atinge um estado estacionário estável.

#### P11
#### Exercício 1
#### Exercício 2
