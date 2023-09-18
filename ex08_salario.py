#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganha_hora = float(input('Digite quanto você ganha por hora trabalhada: R$ '))
hora_trabalhada = int(input('Digite quantas horas você trabalhou esse mês: '))

salario = ganha_hora * hora_trabalhada

print(f'Seu salário este mês é de R$ {salario:2f}')
