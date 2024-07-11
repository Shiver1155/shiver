from random import choice
item = ['pedra', 'papel', 'tesoura']
pc = choice(item)
jogador = str(input('faca sua jogada'))
print(f'A MAQUINA ESCOLHEU {pc}')
if pc == 'pedra':
    if jogador == 'pedra':
        print('EMPATE')
    elif jogador == 'papel':
        print('VOCE GANHOU')
    elif jogador == 'tesoura':
        print('VOCE PERDEU')

if pc == 'papel':
    if jogador == 'pedra':
        print('VOCE PERDEU')
    elif jogador == 'papel':
        print('EMPATE')
    elif jogador == 'tesoura':
        print('VOCE GAANHOU')

    if pc == 'tesoura':
        if jogador == 'pedra':
            print('VOCE GANHOU')
        elif jogador == 'papel':
            print('VOCE PERDEU')
        elif jogador == 'tesoura':
            print('EMPATE')
