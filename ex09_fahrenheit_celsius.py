#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

F = float(input('Digite os graus em Fahrenheit: '))

C = 5 * ((F-32) / 9)

print(f'A temperatura é de {C:.2f}ºC')
