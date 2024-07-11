print('''
[1] Juros Simples
[2] Juros Composto
''')
n1 = int(input('Digite '))
if n1 == 1:
    principal = float(input('Qual valor'))
    taxa = float(input('Qual a taxa?'))
    tempo = int(input('Em quantos anos ?'))
    juros = principal * taxa * tempo
    montante = principal + juros
    print(f'{montante}')

if n1 == 2:
    principal1 = float(input('Qual Valor'))
    tempo = int(input('Em Quantos anos?'))
    taxa = float(input('Qual a taxa?'))
    montante = principal1 * (1 + taxa) ** tempo
    print(f'{montante}')
