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
