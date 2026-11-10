## P6

Suponha emissor em “esperar chamada 0” e receptor em “esperar 0”. O emissor envia o pacote 0, que chega intacto. O receptor entrega o dado, envia ACK e vai para “esperar 1”. O ACK é corrompido. O emissor, ao receber um ACK corrompido, retransmite o pacote 0. O receptor, em “esperar 1”, recebe um pacote intacto com SN 0 e, pela Fig. 3.60, responde NAK. O emissor recebe o NAK e retransmite o pacote 0, e o ciclo se repete indefinidamente. O emissor espera um ACK válido que nunca virá, e o receptor espera o pacote 1, que o emissor só enviará após receber esse ACK. Gerando um deadlock.

