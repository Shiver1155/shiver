n = str(input('Digite Sim para jogar: ')).upper()
while n not in 'S':
    from random import choice
    from time import sleep
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    pc = choice(lista)
    print('''ESCOLHA ENTRE {}PEDRA, PAPEL OU TESOURA {}'''.format('\033[35m', '\033[m'))
    jogador = str(input('Escolha sua Jogada')).upper()

    print('JO')
    sleep(1)
    print('KEM')
    sleep(1)
    print('PO')
    sleep(1)
    print(f'Maquina escolheu {pc}')
    if pc == 'PEDRA':
        if jogador == 'PEDRA':
            print('{}EMPATOU{}'.format('\033[34m', '\033[m'))
        elif jogador == 'TESOURA':
            print('{}PERDEU{}'.format('\033[31m', '\033[m'))
        elif jogador == 'PAPEL':
            print('{}GANHOU{}'.format('\033[32m', '\033[m'))


    if pc == 'TESOURA':
        if jogador == 'PEDRA':
            print('{}GANHOU{}'.format('\033[32m', '\033[m'))
        elif jogador == 'TESOURA':
            print('{}EMPATOU{}'.format('\033[34m', '\033[m'))
        elif jogador == 'PAPEL':
            print('{}PERDEU{}'.format('\033[31m', '\033[m'))


    if pc == 'PAPEL':
        if jogador == 'PEDRA':
            print('{}PERDEU{}'.format('\033[31m', '\033[m'))
        elif jogador == 'TESOURA':
            print('{}GANHOU{}'.format('\033[32m', '\033[m'))
        elif jogador == 'PAPEL':
            print('{}EMPATOU{}'.format('\033[34m', '\033[m'))

    n = str(input('Digite Sim para jogar: ')).upper()
