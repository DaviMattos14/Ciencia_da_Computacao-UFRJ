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
- **$L$ (Tamanho do pacote neste exercício):** $1.500\text{ bytes}$

