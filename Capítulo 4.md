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
#### **2. Tabela de Execução do Algoritmo de Dijkstra (Origem: $x$)**

| **Passo** | **N′**    | **D(t),p(t)** | **D(u),p(u)** | **D(v),p(v)** | **D(w),p(w)** | **D(y),p(y)** | **D(z),p(z)** |
| --------- | --------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| **0**     | $x$       | $\infty$      | $\infty$      | **$3, x$**    | $6, x$        | $6, x$        | $8, x$        |
| **1**     | $xv$      | $7, v$        | **$6, v$**    | —             | $6, x$        | $6, x$        | $8, x$        |
| **2**     | $xvu$     | $7, v$        | —             | —             | **$6, x$**    | $6, x$        | $8, x$        |
| **3**     | $xvuw$    | $7, v$        | —             | —             | —             | **$6, x$**    | $8, x$        |
| **4**     | $xvuwy$   | **$7, v$**    | —             | —             | —             | —             | $8, x$        |
| **5**     | $xvuwyt$  | —             | —             | —             | —             | —             | **$8, x$**    |
| **6**     | $xvuwytz$ | —             | —             | —             | —             | —             | —             |

(Nota: Nos passos 1, 2 e 3, houve empate de custo mínimo igual a $6$ entre os nós $u$, $w$ e $y$, sendo
#### P5
#### P10
#### P11
#### Exercício 1
#### Exercício 2
