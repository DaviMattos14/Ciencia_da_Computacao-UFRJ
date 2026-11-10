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

**Variante 2**: GBN Padrão ($N_{rcv} = 1$)

- **Janela do Receptor:** Tamanho $1$ (só aceita o pacote exatamente em ordem `expectedseqnum`).

- **Pior Cenário:** O emissor envia os pacotes $0, 1, \dots, N-1$. O receptor recebe todos e avança seu `expectedseqnum` para $N \bmod k$. Porém, todos os ACKs são perdidos.

- **Conclusão:** O emissor faz _timeout_ e retransmite a partir do pacote $0$. O receptor está esperando o pacote $N \bmod k$. Para que o receptor não confunda a retransmissão do pacote $0$ com o novo pacote esperado, o número de sequência $N \bmod k$ não pode coincidir com $0$.

- **Resultado:** **$N \le k - 1$** (ou seja, $k \ge N + 1$).

**Variante 3**: Selective Repeat (SR)
