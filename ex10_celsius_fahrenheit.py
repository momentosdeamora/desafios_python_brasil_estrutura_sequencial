#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input('Digite a temperatura em graus em Celsius: '))

F = (C * 9/5) + 32

print(f'A temperatura é de {C:.2f}ºF')
