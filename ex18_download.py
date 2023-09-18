'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade do link de Internet em Mbps: '))

tempo_download_segundos = tamanho_arquivo / (velocidade / 8) # Convertendo de Mbps para MBps (1 byte = 8 bits)
tempo_download_minutos = tempo_download_segundos / 60

print(f'O tempo de download do seu arquivo será de {tempo_download_minutos:.2f} minutos')
