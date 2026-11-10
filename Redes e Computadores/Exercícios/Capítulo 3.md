## P6

Suponha emissor em “esperar chamada 0” e receptor em “esperar 0”. O emissor envia o pacote 0, que chega intacto. O receptor entrega o dado, envia ACK e vai para “esperar 1”. O ACK é corrompido. O emissor, ao receber um ACK corrompido, retransmite o pacote 0. O receptor, em “esperar 1”, recebe um pacote intacto com SN 0 e, pela Fig. 3.60, responde NAK. O emissor recebe o NAK e retransmite o pacote 0, e o ciclo se repete indefinidamente. O emissor espera um ACK válido que nunca virá, e o receptor espera o pacote 1, que o emissor só enviará após receber esse ACK. Gerando um deadlock.

## P13
```plaintext
 Emissor                                            Receptor
│ D0(m1) ──► (ATRASADO na rede)
│ timeout → reenvia
│ D0(m1)' ───────────────────────────────────────►│ entrega m1; espera 1
│◄────────────────────────────────────────── A0   │
│ D1(m2) ────────────────────────────────────────►│ entrega m2; espera 0
│◄────────────────────────────────────────── A1   │
│ D0(m3) ──► (a caminho)
│             D0(m1) antigo chega ───────────────►│ espera 0 → ACEITA
│                                                  │ entrega m1 DE NOVO X
│                                                  │ passa a esperar 1
│◄────────────────────────────────────────── A0   │
│ recebe A0 → conclui "m3 entregue" X
│ D1(m4) ────────────────────────────────────────►│ (a ver abaixo)
│             D0(m3) chega ──────────────────────►│ espera 1 → "duplicata"
│                                                  │ DESCARTA m3 X;envia A0
```

o receptor recebe `D1(m4)`, espera 1, **entrega m4** e envia A1. O A0 que ele enviou ao descartar m3 chega ao emissor quando este já espera o ACK 1, então o emissor o **ignora** (acknum errado, regra do rdt3.0).

A aplicação receptora recebe **m1, m2, m1, m4**:
- **m1 chega duplicado.**
- **m3 foi perdido**, embora o emissor acredite que foi entregue.
Isso viola exatamente o que o RDT promete: sem duplicação, sem perda, em ordem.

## P15
- **$RTT$ (Round-Trip Time / Tempo de ida e volta):** $30\text{ ms} = 0{,}030\text{ s}$
- **$R$ (Taxa de transmissão do enlace):** $1\text{ Gbps} = 10^9\text{ bits/s}$
- **$L$ (Tamanho do pacote neste exercício):** $1.500\text{ bytes} = 1.500 \times 8\text{ bits} = 12.000\text{ bits}$
$$d_{trans} = \frac{L}{R} = \frac{12.000}{10^9} = 1{,}2 \times 10^{-5}\text{ s} = 0{,}012\text{ ms}$$
$$U_{sender} = \frac{d_{trans}}{RTT + d_{trans}} = \frac{0{,}012\text{ ms}}{30\text{ ms} + 0{,}012\text{ ms}} = \frac{0{,}012}{30{,}012} \approx 0{,}00039984 \approx 4 \times 14^{-4}$$

Queremos que $U_{sender} > 0{,}98$:
$$\frac{N \cdot d_{trans}}{RTT + d_{trans}} > 0{,}98$$
$$N > \frac{0{,}98 \cdot (RTT + d_{trans})}{d_{trans}} = \frac{0{,}98 \cdot 30{,}012}{0{,}012} = 0{,}98 \cdot 2.501 = 2.450{,}98$$

Como $N$ representa um número inteiro de pacotes:
$$N \ge 2.451\text{ pacotes}$$

## P23

**Variante 1**: GBN em que o receptor aceita/armazena pacotes fora de ordem

- **Lógica:** Se o receptor for modificado para aceitar e armazenar pacotes fora de ordem, a janela de recepção deixa de ser unitária ($N_{rcv} = 1$) e passa a ser de tamanho $N_{rcv} = N$.

- **Condição de não ambiguidade:** Para evitar que a nova janela do receptor se sobreponha a retransmissões da janela antiga do emissor (caso todos os ACKs se percam), a soma dos tamanhos das janelas do emissor e do receptor não pode exceder o espaço total $k$ ($N_{send} + N_{rcv} \le k$).

- **Resultado:** $N + N \le k \implies 2N \le k \implies \mathbf{N \le \lfloor k / 2 \rfloor}$.

**Variante 2**: GBN Padrão (Receptor só aceita pacotes rigorosamente em ordem)
- **Lógica:** O receptor possui janela unitária ($N_{rcv} = 1$), aceitando apenas o pacote de valor exato `expectedseqnum`.

- **Condição de não ambiguidade:** Se o emissor transmitir $N$ pacotes e todos os ACKs forem perdidos, o emissor retransmitirá o pacote $0$. O receptor, por sua vez, estará aguardando o pacote $N \bmod k$. Para que o receptor não confunda a retransmissão do pacote $0$ com um novo pacote esperado, precisamos que $N \bmod k \neq 0$.

- **Resultado:** $N_{send} + N_{rcv} \le k \implies N + 1 \le k \implies \mathbf{N \le k - 1}$.

**Variante 3**: Selective Repeat (SR)
- **Lógica:** Ambos os lados mantêm janelas de tamanho $N$ ($N_{send} = N$ e $N_{rcv} = N$).

- **Condição de não ambiguidade:** No pior cenário de perda total de ACKs, a janela do receptor avança $N$ posições enquanto a do emissor permanece parada. Para garantir que a faixa de números de sequência esperada pelo receptor não se sobreponha à faixa retransmitida pelo emissor, as duas janelas somadas devem ser menores ou iguais ao tamanho total do espaço $k$.

- **Resultado:** $N_{send} + N_{rcv} \le k \implies 2N \le k \implies \mathbf{N \le \lfloor k / 2 \rfloor}$.

## P40

a) 

- **Intervalos:** Rodadas **1 a 6** e rodadas **23 a 26**.
- **Justificativa:** Nesses intervalos, a janela de congestionamento (`cwnd`) apresenta crescimento exponencial, dobrando a cada RTT (1 $\to$ 2 $\to$ 4 $\to$ 8 $\to$ 16 $\to$ 32 na primeira fase; 1 $\to$ 2 $\to$ 4 $\to$ 8 após a rodada 22).

b) 

- **Intervalos:** Rodadas **6 a 16** e rodadas **17 a 22**.
- **Mapeamento detalhado na FSM da 8ª edição por RTT/Estado:**
    1. **Rodadas 1–5 (Estado: _Slow Start_):** O protocolo permanece em _Slow Start_ porque `cwnd < ssthresh`. A cada ACK recebido, `cwnd` é incrementado em 1 MSS, resultando na dobradinha a cada RTT.
    2. **Rodada 6 (Transição: _Slow Start_ $\to$ _Congestion Avoidance_):** Ao final da rodada 5, `cwnd` atinge 32 MSS, igualando-se ao limiar `ssthresh` (32). A FSM avalia o evento `cwnd >= ssthresh` e transiciona para o estado **_Congestion Avoidance_**.
    3. **Rodadas 6–16 (Estado: _Congestion Avoidance_):** O protocolo permanece em _Congestion Avoidance_, incrementando `cwnd` de forma linear (+1 MSS a cada RTT completo, variando de 32 até 42).
    4. **Após a Rodada 16 (Transição: _Congestion Avoidance_ $\to$ _Fast Recovery_ $\to$ _Congestion Avoidance_):** Ocorre o evento de 3 ACKs duplicados (`dupACKcount == 3`). A FSM executa:        $$\text{ssthresh} = \frac{\text{cwnd}}{2} = \frac{42}{2} = 21 \text{ MSS}$$$$\text{cwnd} = \text{ssthresh} + 3 = 24 \text{ MSS}$$
	O segmento é retransmitido rapidamente e o TCP Reno entra em **_Fast Recovery_**. Ao receber o ACK do segmento retransmitido, deflaciona a janela e retorna a **_Congestion Avoidance_** para a rodada 17.
    5. **Rodadas 17–22 (Estado: _Congestion Avoidance_):** A `cwnd` cresce linearmente a partir de 24 MSS até atingir 29 MSS na rodada 22 (+1 MSS por RTT).
    
    6. **Após a Rodada 22 (Transição: _Congestion Avoidance_ $\to$ _Slow Start_):** Ocorre um evento de _Timeout_ (esgotamento de temporização). A FSM executa:$$\text{ssthresh} = \lfloor 29 / 2 \rfloor = 14 \text{ MSS}$$$$\text{cwnd} = 1 \text{ MSS}, \quad \text{dupACKcount} = 0$$
	A FSM retorna imediatamente para o estado **_Slow Start_**.
    7. **Rodadas 23–26 (Estado: _Slow Start_):** Com `cwnd` reiniciada em 1 MSS e `ssthresh = 14`, a janela dobra a cada RTT até a rodada 26 (`cwnd = 8`), mantendo-se em _Slow Start_ pois $8 < 14$.

c) Detecção da perda após a 16ª rodada

- **Causa:** **3 ACKs duplicados (_Fast Retransmit_)**.
- **Justificativa:** A janela de congestionamento na rodada 17 reduz-se para 24 MSS (que corresponde a $\text{ssthresh} + 3 = 21 + 3$) em vez de descer para 1 MSS. Esse comportamento de corte pela metade é exclusivo da recepção de 3 ACKs duplicados no TCP Reno.

d) Detecção da perda após a 22ª rodada

- **Causa:** **Timeout (_Esgotamento de Temporização_)**. Na rodada 23, a `cwnd` despenca diretamente para 1 MSS, o que caracteriza a reação da FSM diante da expiração do temporizador de retransmissão.
- 
e) Valor de `ssthresh` na 1ª rodada
A fase de Partida Lenta termina na rodada 6 quando `cwnd` atinge 32 MSS e a curva passa de exponencial para linear. Como a transição de estado ocorre no instante em que $\text{cwnd} \ge \text{ssthresh}$, infere-se que o valor inicial de `ssthresh` era 32 MSS.

f) Valor de `ssthresh` na 18ª rodada

- **Valor:** **21 MSS**.

- **Justificativa:** A perda ocorrida após a 16ª rodada deu-se com `cwnd = 42`. A FSM atualiza o limiar para $\text{ssthresh} = 42 / 2 = 21 \text{ MSS}$. Na 18ª rodada, esse parâmetro permanece em 21 MSS 

g) Valor de `ssthresh` na 24ª rodada

- **Valor:** **14 MSS** (ou $14{,}5 \text{ MSS}$). O timeout pós-rodada 22 ocorreu quando `cwnd = 29`. O valor de `ssthresh` é recalculado como $\lfloor 29 / 2 \rfloor = 14 \text{ MSS}$.

h)
- **Resposta:** **7ª rodada**.
- **Justificativa:** Somando a quantidade acumulada de segmentos transmitidos por RTT:
	- Rodada 1: $1$ segmento (acumulado: $1$)
	- Rodada 2: $2$ segmentos (acumulado: $3$)
	- Rodada 3: $4$ segmentos (acumulado: $7$)
	- Rodada 4: $8$ segmentos (acumulado: $15$)
	- Rodada 5: $16$ segmentos (acumulado: $31$)
	- Rodada 6: $32$ segmentos (acumulado: $63$)
	- Rodada 7: $33$ segmentos (acumulado: $96$) Como até o fim da 6ª rodada haviam sido enviados 63 segmentos, os segmentos de número 64 a 96 — incluindo o 70º — são enviados durante a **7ª rodada**.
  
i) Valores de `cwnd` e `ssthresh` para perda por 3 ACKs duplicados após a 26ª rodada

- **Valores:** $\text{ssthresh} = \mathbf{4\text{ MSS}}$ e $\text{cwnd} = \mathbf{7\text{ MSS}}$ (ao entrar em _Fast Recovery_).
- **Justificativa:** Na 26ª rodada, $\text{cwnd} = 8 \text{ MSS}$. Com 3 ACKs duplicados, $\text{ssthresh} = 8 / 2 = 4 \text{ MSS}$, e o valor ajustado de `cwnd` no TCP Reno torna-se $\text{ssthresh} + 3 = 7 \text{ MSS}$.

j)
- **Valores na 19ª rodada:** $\text{ssthresh} = \mathbf{21\text{ MSS}}$ e $\text{cwnd} = \mathbf{4\text{ MSS}}$.
- **Comentário Histórico:** O **TCP Tahoe** (proposto por Van Jacobson em 1988) adotava uma postura rígida: qualquer indicação de perda (seja Timeout ou 3 ACKs duplicados) cortava `cwnd` incondicionalmente para 1 MSS e reiniciava a Partida Lenta.
- **Evolução em Tahoe:**  
    - Pós-16ª rodada ($\text{cwnd} = 42$): $\text{ssthresh} = 42 / 2 = 21 \text{ MSS}$.
	- Rodada 17: $\text{cwnd} = 1 \text{ MSS}$ (_Slow Start_)
	- Rodada 18: $\text{cwnd} = 2 \text{ MSS}$ (_Slow Start_)
	- Rodada 19: $\text{cwnd} = 4 \text{ MSS}$ (_Slow Start_)
    
k) 

|**Rodada (RTT)**|**cwnd (MSS)**|**ssthresh (MSS)**|**Estado na FSM do TCP**|**Evento / Observação**|
|---|---|---|---|---|
|**1**|1|32|_Slow Start_|Início da conexão|
|**2**|2|32|_Slow Start_|Crescimento exponencial|
|**3**|4|32|_Slow Start_|Crescimento exponencial|
|**4**|8|32|_Slow Start_|Crescimento exponencial|
|**5**|16|32|_Slow Start_|Crescimento exponencial|
|**6**|32|32|Transição para _Congestion Avoidance_|`cwnd` atinge `ssthresh`|
|**7**|33|32|_Congestion Avoidance_|Crescimento linear (+1); 70º seg enviado|
|**8**|34|32|_Congestion Avoidance_|Crescimento linear|
|**9**|35|32|_Congestion Avoidance_|Crescimento linear|
|**10**|36|32|_Congestion Avoidance_|Crescimento linear|
|**11**|37|32|_Congestion Avoidance_|Crescimento linear|
|**12**|38|32|_Congestion Avoidance_|Crescimento linear|
|**13**|39|32|_Congestion Avoidance_|Crescimento linear|
|**14**|40|32|_Congestion Avoidance_|Crescimento linear|
|**15**|41|32|_Congestion Avoidance_|Crescimento linear|
|**16**|42|32|_Congestion Avoidance_|Ocorrência de 3 ACKs duplicados no fim|
|**17**|24|21|_Fast Recovery_ / _Congestion Avoidance_|`ssthresh` = 21; `cwnd` = 21 + 3 = 24|
|**18**|25|21|_Congestion Avoidance_|Crescimento linear|
|**19**|26|21|_Congestion Avoidance_|Crescimento linear|
|**20**|27|21|_Congestion Avoidance_|Crescimento linear|
|**21**|28|21|_Congestion Avoidance_|Crescimento linear|
|**22**|29|21|_Congestion Avoidance_|Ocorrência de Timeout no fim|
|**23**|1|14|_Slow Start_|`ssthresh` = $\lfloor 29/2 \rfloor = 14$; `cwnd` reseta p/ 1|
|**24**|2|14|_Slow Start_|Crescimento exponencial|
|**25**|4|14|_Slow Start_|Crescimento exponencial|
|**26**|8|14|_Slow Start_|Crescimento exponencial|
## P45

##### 1. Condição Inicial em $t_3$

- No instante $t_3$, ocorre uma perda no limite antigo $W_{\max}$.
- Ambos os protocolos executam a redução multiplicativa e caem para **$0{,}5 W_{\max}$**.
- A partir de $t_3$, o novo limite máximo suportado pela rede cai para **$0{,}75 W_{\max}$** (sem o conhecimento prévio dos emissores).

##### 2. Rodada 1 (Após $t_3$)

**TCP CUBIC**

1. **Crescimento:** A partir de $0{,}5 W_{\max}$, o CUBIC acelera rapidamente seu crescimento seguindo sua função cúbica para se aproximar da taxa pré-perda antiga ($W_{\max}$).
2. **Nova Perda:** Devido a essa subida rápida, o CUBIC atinge a nova capacidade de **$0{,}75 W_{\max}$** **primeiro no tempo** (no instante $t_4^{\text{CUBIC}}$).
3. **Reação à Perda:**
    - O CUBIC registra o novo valor de pico $W_{\max}^{\text{novo}} = 0{,}75 W_{\max}$.
	- Sua taxa de envio é cortada pela metade em relação ao ponto de perda:
$$\frac{0{,}75 W_{\max}}{2} = \mathbf{0{,}375 W_{\max}}$$
**TCP Reno**

1. **Crescimento:** A partir de $0{,}5 W_{\max}$, o Reno cresce de forma aditiva/linear (+1 MSS por RTT).
2. **Nova Perda:** Por crescer de forma mais lenta e constante, o Reno leva mais tempo para alcançar $0{,}75 W_{\max}$, sofrendo a perda em um instante posterior $t_4^{\text{Reno}}$ (onde $t_4^{\text{Reno}} > t_4^{\text{CUBIC}}$).
3. **Reação à Perda:**
    - Sua taxa de envio é cortada pela metade em relação a $0{,}75 W_{\max}$:
$$\frac{0{,}75 W_{\max}}{2} = \mathbf{0{,}375 W_{\max}}$$

##### 3. Rodada 2 (Segunda Rodada de Perda)

#### **TCP CUBIC**

1. **Crescimento:** Parte de $0{,}375 W_{\max}$ e tenta se aproximar do seu novo valor de referência $W_{\max}^{\text{novo}} = 0{,}75 W_{\max}$.
2. **Nova Perda:** Ao se aproximar de $0{,}75 W_{\max}$, atinge o limite da rede novamente e sofre outra perda em $t_5^{\text{CUBIC}}$.
3. **Reação:** Recua novamente para a metade da taxa corrente: $\mathbf{0{,}375 W_{\max}}$.

**TCP Reno**

1. **Crescimento:** Parte de $0{,}375 W_{\max}$ e sobe linearmente.
2. **Nova Perda:** Atinge $0{,}75 W_{\max}$ em $t_5^{\text{Reno}}$ e sofre nova perda.
3. **Reação:** Recua para $\mathbf{0{,}375 W_{\max}}$.

| **Fase / Evento**                 | **TCP Reno**                                                  | **TCP CUBIC**                                                 |
| --------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| **Taxa em $t_3$ (pós-perda)**     | $0{,}5 W_{\max}$                                              | $0{,}5 W_{\max}$                                              |
| **Padrão de Crescimento**         | Linear / Aditivo                                              | Cúbico (rápido no início)                                     |
| **Momento da 1ª Perda pós-$t_3$** | Atinge $0{,}75 W_{\max}$ **mais tarde** ($t_4^{\text{Reno}}$) | Atinge $0{,}75 W_{\max}$ **mais cedo** ($t_4^{\text{CUBIC}}$) |
| **Taxa mínima após 1ª Perda**     | $0{,}375 W_{\max}$                                            | $0{,}375 W_{\max}$                                            |
| **Momento da 2ª Perda**           | Atinge $0{,}75 W_{\max}$ em $t_5^{\text{Reno}}$               | Atinge $0{,}75 W_{\max}$ em $t_5^{\text{CUBIC}}$              |
| **Taxa mínima após 2ª Perda**     | $0{,}375 W_{\max}$                                            | $0{,}375 W_{\max}$                                            |
As oscilações do TCP CUBIC se tornam mais frequentes no tempo do que as do TCP Reno quando a capacidade do enlace diminui, porque a agressividade do CUBIC no início da recuperação o faz colidir com o novo teto de congestionamento muito mais rápido.

## P46
#### 1. Estado Inicial em $t_3$

- No instante $t_3$, ocorre a perda no limite antigo $W_{\max}$.
- Ambos os protocolos aplicam a redução multiplicativa e caem para **$0{,}5 W_{\max}$**.
- O novo limite de perda passa a ser **$1{,}5 W_{\max}$**.

#### 2. Evolução da Rodada 1 (Pós-$t_3$)

 **TCP Reno**

1. **Crescimento:** Parte de $0{,}5 W_{\max}$ e cresce de forma estritamente **linear** (+1 MSS a cada RTT).
    
2. **Nova Perda:** Para ir de $0{,}5 W_{\max}$ até o novo limite de $1{,}5 W_{\max}$, o Reno precisa percorrer uma variação de $1{,}0 W_{\max}$. Por ter uma taxa de subida constante e lenta, ele demora um tempo longo para atingir $1{,}5 W_{\max}$ (no instante $t_4^{\text{Reno}}$).
    
3. **Reação à Perda:** Ao atingir $1{,}5 W_{\max}$, ocorre a perda por congestionamento. O Reno corta a janela pela metade:
    
    $$\text{Taxa pós-perda} = \frac{1{,}5 W_{\max}}{2} = \mathbf{0{,}75 W_{\max}}$$
    

 **TCP CUBIC**

1. **Crescimento:** Parte de $0{,}5 W_{\max}$ visando a sua referência anterior $W_{\max}$.
    
    - Primeiramente, ele sobe rápido e desacelera (achata) ao redor de $W_{\max}$.
        
    - Como não ocorre perda ao atingir $W_{\max}$ (já que o novo teto é $1{,}5 W_{\max}$), o CUBIC entra no seu **modo de sondagem (_probing mode_)**.
        
    - À medida que $t > K$, a função cúbica $C(t-K)^3$ passa a crescer **extremamente rápido** (curva convexa acentuada) para buscar nova largura de banda.
        
2. **Nova Perda:** Essa aceleração rápida após ultrapassar $W_{\max}$ faz com que o CUBIC atinja a nova barreira de $1{,}5 W_{\max}$ **muito mais rápido que o TCP Reno** ($t_4^{\text{CUBIC}} < t_4^{\text{Reno}}$).
    
3. **Reação à Perda:**
    
    - O CUBIC atualiza sua referência para $W_{\max}^{\text{novo}} = 1{,}5 W_{\max}$.
        
    - Corta a taxa de envio pela metade (no modelo simplificado do livro):
        
        $$\text{Taxa pós-perda} = \frac{1{,}5 W_{\max}}{2} = \mathbf{0{,}75 W_{\max}}$$
### 3. Evolução da Rodada 2 (Segunda Perda)

 **TCP Reno**

1. **Crescimento:** Parte de $0{,}75 W_{\max}$ e sobe linearmente até atingir $1{,}5 W_{\max}$ novamente em $t_5^{\text{Reno}}$.
    
2. **Reação:** Corta a taxa pela metade ao sofrer a perda:
    
    $$\text{Taxa pós-perda} = \frac{1{,}5 W_{\max}}{2} = \mathbf{0{,}75 W_{\max}}$$
    

 **TCP CUBIC**

1. **Crescimento:** Parte de $0{,}75 W_{\max}$ tendo agora $W_{\max}^{\text{novo}} = 1{,}5 W_{\max}$ como objetivo.
    
2. **Padrão da Curva:** Sobe rapidamente no início a partir de $0{,}75 W_{\max}$, achata-se ao se aproximar de $1{,}5 W_{\max}$ e sofre nova perda em $t_5^{\text{CUBIC}}$ exatamente ao tentar ultrapassá-lo.
    
3. **Reação:** Recua novamente para a metade: $\mathbf{0{,}75 W_{\max}}$.
    

| **Evento / Parâmetro**                     | **TCP Reno**                                    | **TCP CUBIC**                                         |
| ------------------------------------------ | ----------------------------------------------- | ----------------------------------------------------- |
| **Ponto de partida em $t_3$**              | $0{,}5 W_{\max}$                                | $0{,}5 W_{\max}$                                      |
| **Comportamento após passar $W_{\max}$**   | Mantém inclinação linear constante (+1 MSS/RTT) | Acelera vertiginosamente (crescimento cúbico convexo) |
| **Momento da 1ª perda ($1{,}5 W_{\max}$)** | Demora muito tempo ($t_4^{\text{Reno}}$)        | Atinge muito mais rapidamente ($t_4^{\text{CUBIC}}$)  |
| **Recuo pós-1ª perda**                     | $0{,}75 W_{\max}$                               | $0{,}75 W_{\max}$                                     |
| **Momento da 2ª perda ($1{,}5 W_{\max}$)** | Atinge em $t_5^{\text{Reno}}$                   | Atinge em $t_5^{\text{CUBIC}}$                        |
| **Recuo pós-2ª perda**                     | $0{,}75 W_{\max}$                               | $0{,}75 W_{\max}$                                     |

Quando a capacidade da rede aumenta, o TCP CUBIC aproveita a nova largura de banda disponível **muito mais rápido** do que o TCP Reno. Enquanto o Reno sofre para subir lentamente de forma linear, a fase de sondagem convexa do CUBIC dispara para encontrar a nova capacidade.

## Exercício 1
