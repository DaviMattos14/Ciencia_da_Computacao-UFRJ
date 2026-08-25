> **Nome**: Davi dos Santos Mattos            **DRE**: 119133049

1) P2 -- explique porque o uso de store-and-forward implica que o atraso de transmissão aumente em função do número de links envolvidos no caminho origem-destino, enquanto que cut-through não

Equação 1.1 (um único pacote, N enlaces, todos com taxa R):

$$d_{fim-a-fim} = N \cdot \frac{L}{R}$$

Agora, para P pacotes enviados consecutivamente (back-to-back), assim que o host de origem termina de transmitir o pacote 1 (o que leva L/R segundos), ele já começa a transmitir o pacote 2 imediatamente, e assim por diante, sem esperar o pacote 1 chegar ao destino.

O "gargalo" desse é: o último pacote (o P-ésimo) só pode começar a ser transmitido pela origem depois que os P−1 pacotes anteriores já tiverem sido totalmente transmitidos. Isso adiciona $(P−1)·(L/R)$ de atraso extra antes mesmo do último pacote começar sua jornada. A partir daí, esse último pacote ainda precisa percorrer os N enlaces normalmente, levando $N·(L/R)$.

Logo, o atraso total (tempo até o **último bit do último pacote** chegar ao destino) é:

$$d_{fim-a-fim} = (P-1)\cdot\frac{L}{R} + N \cdot \frac{L}{R} = (N + P - 1)\cdot\frac{L}{R}$$
**Store-and-forward:** cada roteador no caminho segue a regra de esperar receber o pacote inteiro antes de começar a retransmiti-lo para o próximo enlace. Ou seja, cada um dos N enlaces do caminho "cobra" seu próprio L/R inteiro, de forma sequencial e cumulativa. O roteador N não pode começar a transmitir enquanto não recebeu 100% do pacote vindo do roteador N−1. É exatamente por isso que a fórmula tem o fator **N·(L/R)**: o atraso de transmissão se **multiplica** pelo número de saltos (hops).

**Cut-through switching:** nessa abordagem alternativa, o roteador não espera o pacote inteiro chegar. Assim que ele lê apenas o cabeçalho (o suficiente para saber por qual enlace de saída o pacote deve seguir), ele já começa a retransmitir os bits que já chegaram, à medida que os bits seguintes ainda estão chegando pelo enlace anterior. Ou seja, os "estágios" (enlaces) passam a operar de forma sobreposta/paralela, e não mais sequencial.

Por isso, no cut-through, o componente de atraso de transmissão deixa de ser proporcional a N, ele fica próximo de apenas $L/R$ , e os demais saltos adicionam apenas pequenos atrasos de processamento/propagação, não um L/R completo cada. O atraso deixa de "empilhar" a cada roteador extra no caminho.

2) P3  

	a) A comutação de circuitos seria mais apropriada para esse cenário. Ela consegue garantir a taxa constante que a aplicação precisa (sem risco de atraso de fila ou perda de pacotes por disputa de enlace), e não desperdiça recursos porque não há ociosidade a "aproveitar".

	b) Não, não é necessário nenhuma forma de controle de congestionamento nesse cenário específico. O controle de congestionamento existe justamente para lidar com situações em que a demanda pode, em algum momento, superar a capacidade e neste cenário esta situação nunca ocorre.
	
3) P4 -- circuit switch  

	a) 16 conexões simultâneas.
	b) 8 conexões simultâneas entre A e C.
	c) Sim, é possível acomodar as 8 conexões simultaneamente, desde que o roteamento seja feito de forma balanceada (2 conexões de cada grupo por cada rota alternativa), usando os 16 circuitos da rede em sua capacidade máxima.
  
4) P6 -- diferença propagação e transmissão  

	a) Atraso de propagação
$$d_{prop} = \frac{m}{s}$$
	b) Atraso de transmissão
$$d_{trans} = \frac{L}{R}$$
	c) Atraso fim-a-fim (ignorando processamento e fila)

	Os dois atrasos são **somados**, pois são sequenciais: primeiro A precisa empurrar todos os bits para o enlace (transmissão), e o **último bit** só termina de "viajar" depois de percorrer toda a distância (propagação):

$$d_{fim-a-fim} = d_{trans} + d_{prop} = \frac{L}{R} + \frac{m}{s}$$
	d) Em t = d_trans, onde está o **último bit** do pacote?
	
	Em t = d_trans, o Host A **acabou de terminar** de transmitir o pacote inteiro — ou seja, o último bit **acabou de sair de A e entrar no enlace**. Ele ainda não percorreu nenhuma distância significativa além do ponto de partida (está "no início" do enlace, saindo do host A).
	
	e) Se d_prop > d_trans, onde está o **primeiro bit** em t = d_trans?
	
	Se d_prop > d_trans, isso significa que a propagação é **mais lenta** que a transmissão — ou seja, o primeiro bit, mesmo tendo saído em t=0, **ainda não teve tempo suficiente para percorrer todo o enlace** até t = d_trans. Portanto: o primeiro bit está **em algum ponto no meio do enlace** (ainda "a caminho", não chegou a B).

	f) Se d_prop < d_trans, onde está o **primeiro bit** em t = d_trans?

	Se d_prop < d_trans, a propagação é **mais rápida** que a transmissão. Isso significa que o primeiro bit **já teve tempo de sobra** para percorrer todo o enlace antes mesmo de A terminar de transmitir o pacote inteiro. Portanto: o primeiro bit **já chegou ao Host B** (está no receptor, esperando o resto do pacote chegar).

	g) Encontrar m tal que d_prop = d_trans
	
	Dados: s = 2,5 × 10⁸ m/s, L = 1500 bytes, R = 10 Mbps

	Primeiro, converter unidades:
	- L = 1500 bytes × 8 bits/byte = **12.000 bits**
	- R = 10 Mbps = **10 × 10⁶ bits/s**

	Calculando d_trans:
	$$d_{trans} = \frac{L}{R} = \frac{12.000}{10 \times 10^6} = 1,2 \times 10^{-3} \text{ s} = 1,2 \text{ ms}$$

	Queremos d_prop = d_trans, ou seja:
	$$\frac{m}{s} = d_{trans} \implies m = s \times d_{trans}$$

	$$m = (2,5 \times 10^8) \times (1,2 \times 10^{-3}) = 3 \times 10^5 \text{ m} = 300 \text{ km}$$

	**Resposta:** m = 300.000 metros (300 km).

5) P7 -- exercício interessante por olhar para camada de aplicação VoIP  
  
6) P23 -- muito importante -- packet pair  
  
7) Vídeo distribuições -- assista e resuma o vídeo, trazendo perguntas: [https://www.youtube.com/watch?v=C8DxAQT5goE](https://www.youtube.com/watch?v=C8DxAQT5goE)  
  
8) Vídeo lei de Little -- assista e resuma o vídeo, trazendo perguntas: [https://www.youtube.com/watch?v=p1sG7mm1Ixo](https://www.youtube.com/watch?v=p1sG7mm1Ixo)  
  
9) Estude os slides [https://tinyurl.com/filaufrj20261](https://tinyurl.com/filaufrj20261) e liste 3 dúvidas  
  
10) derive, por conta própria, o resultado N = I/(I-I) usando a abordagem apresentada nos slides (é só reescrever com suas palavras)  
  
11) repita a mesma coisa, agora usando cadeias de Markov, e mostre que o resultado é o mesmo  
  
12) o que acontece se o tempo de transmissão for determinístico igual a L/R ao invés de exponencial? Como fica a equação de N? E a equação de W?  
  
13) o que acontece se a taxa de chegada dobrar e a capacidade de serviço também? Ou seja, a'=2a e R'=2R. Quanto vale N e W depois das modificações? E La/R? Qual muda e qual não muda? Justifique intuitivamente sua resposta.  
  
14) P13 do livro 8a edição  
  
15)  P14 do livro 8a edição  
  
16)  P15 do livro 8a edição  
  
17) P16 do livro 8a edição -- esse enunciado talvez tenha um problema! caso encontre um problema, aponte o problema e conserte o enunciado, como julgar adequado. depois de propor um novo enunciado, resolva o problema que você mesmo bolou  
  
18) P17 do livro 8a edição  
  
19) P22 do livro 8a edição -- perda de pacotes  
  
20) melhorar o material em [https://www.overleaf.com/read/wmkckszznbjz#04ba5c](https://www.overleaf.com/read/wmkckszznbjz#04ba5c) possivelmente mexendo direto nos arquivos que estão no overleaf  criando uma cópia do repositório ou então listando sugestões