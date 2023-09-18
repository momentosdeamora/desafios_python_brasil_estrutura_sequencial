'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.'''

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = float(input('Digite o terceiro e último número real: '))

produto = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) + n3
cubo = n3 ** 3

print(f'O produto do dobro do primeiro com metade do segundo é de {produto}.')
print(f'A soma do triplo do primeiro com o terceiro é de {soma:.2f}')
print(f'O terceiro elevado ao cubo é de {cubo:.2f}')
