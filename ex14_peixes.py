'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.'''

peso = float(input('Digite quantos quilos você pescou hoje: '))
peso_limite = 50
valor_multa = 4

excesso = peso - peso_limite

if excesso > 0:
    multa = valor_multa * excesso
    print(f'Você excedeu o limite de peso para a pesca em {excesso:.2f} kg. Poranto, pagará a multa de R$ {multa:.2f}')
else:
    print(f'Você não atingiu o limite de peso para a pesca. Parabéns! Pode seguir em frente.')
