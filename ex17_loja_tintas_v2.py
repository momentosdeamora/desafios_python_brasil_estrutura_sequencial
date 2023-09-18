'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math

tamanho = float(input('Qual o valor em metros quadrados do espaço? '))

metros_litro = 6
litros_lata = 18
preco_lata = 80.00
litros_galao = 3.6
preco_galao = 25.00

litros_necessarios = tamanho / metros_litro

qtd_latas = math.ceil(litros_necessarios / litros_lata)
preco_total_latas = qtd_latas * preco_lata
print(f'Você precisará de {qtd_latas} latas de tinta.')
print(f'O preço total com latas será de R$ {preco_total_latas:.2f}')

qtd_galao = math.ceil(litros_necessarios / litros_galao)
preco_total_galoes = qtd_galao * preco_galao
print(f'Você precisará de {qtd_galao} galões de tinta.')
print(f'O preço total com galões será de R$ {preco_total_galoes:.2f}')

qtd_latas_mistura = math.ceil(litros_necessarios / litros_lata)
qtd_galao_mistura = math.ceil((litros_necessarios % litros_lata) / litros_galao)
preco_total_mistura = (qtd_latas_mistura * preco_lata) + (qtd_galao_mistura * preco_galao)
print(f'Você precisará de {qtd_latas_mistura} latas de tinta e {qtd_galao_mistura} galões de tinta na mistura.')
print(f'O preço total na mistura será de R$ {preco_total_mistura:.2f}')
