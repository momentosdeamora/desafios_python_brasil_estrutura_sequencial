#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Informe o raio de um círculo: '))
pi = 3.1415

area = pi * (raio ** 2)

print(f'A área deste círculo é de {area:.2f}.')
