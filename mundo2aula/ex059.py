from time import sleep
n = int(input('primeiro numero'))
n1 = int(input('segundo numero'))
t = 0
while True:

    print('''[1] SOMAR
[2] MULTI
[3] MAIOR
[4] NOVO NUMERO
[5] SAIR DO PROGRAMA''')
    t = int(input('qual opcao'))
    if t == 1:
        s = n + n1
        print(f'{s}')
    elif t == 2:
        s = n * n1
        print(f'{s}')
    elif t == 3:
        s = max(n, n1)
        print(f'{s}')
    elif t == 4:
        n = int(input('primeiro numero'))
    elif t == 5:
        print('Saindo do programa')
        sleep(2)
        break
    else:
        print('{} Opcao invalida, Tente novamente {}'.format('\33[31m', '\033[m'))

