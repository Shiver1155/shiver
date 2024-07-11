COR_VERMELHA = '\033[91m'
COR_VERDE = '\033[92m'
COR_AMARELA = '\033[93m'
COR_AZUL = '\033[94m'
RESET_COR = '\033[0m'

def cores(texto,cor):
    return f'{cor}{texto}{RESET_COR}'

n = int(input('Qual o valor'))
n1 = int(input('Digite outro valor'))
t = 0
while t != 5:

    print('''[1] SOMA
[2] MULTI
[3] MAIOR
[4] NOVO NUMERO
[5] SAIR''') 

    n2 = int(input('Qual opcao'))

    if n2 == 1:
        s = n + n1
        print(cores(f'{s}',COR_AZUL))

    elif n2 == 2:
        s = n * n2
        print(f'{s}')

    elif n2 == 3:
        s = max(n, n1)
        print(f'{s}')

    elif n2 == 4:
        n = int(input('Qual o valor'))
        n1 = int(input('Digite outro valor'))

    elif n2 == 5:
        print('FINALIZADO...')
