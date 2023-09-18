'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

altura = float(input('Digite a sua altura em metros: '))
sexo = input('Digite o seu sexo (M para masculino, F para feminino): ')

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    genero = 'homem'
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    genero = 'mulher'
else:
    print('Sexo não reconhecido. Por favor, digite M ou F para masculino ou feminino.')
    exit()

print(f'Se você for {genero}, então seu peso ideal é de: {peso_ideal:.2f} kg')
