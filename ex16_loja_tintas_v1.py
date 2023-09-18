''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

tamanho = float(input('Qual o valor em metros quadrados do espaço? '))

metros_litro = 3
litros_lata = 18
preco_lata = 80.00

litros_necessarios = tamanho / metros_litro

qtd_latas = int(litros_necessarios / litros_lata)
if litros_necessarios % litros_lata != 0:
    qtd_latas += 1

preco_total = qtd_latas * preco_lata

print(f'Você precisará de {qtd_latas} latas de tinta.')
print(f'O preço total será de R$ {preco_total:.2f}')
