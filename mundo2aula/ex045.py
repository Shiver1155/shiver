from random import randint
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 ,2)
print('''SUA OPCOES:
[0] PAPEL
[1] PEDRA
[2] TESOURA''')
jogador = int(input('Qual sua jogada ?'))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-' * 10)
print('Computador jogou {}'.format(item[computador]))
print('O jogador jogou {}'.format(item[jogador]))
print('-=-' * 10)
if computador == 0:
    if jogador == 0:
        print('DEU EMPATE')
    elif jogador == 1:
        print('O JOGADOR GANHOU')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('O JOGADOR GANHOU')
    elif jogador == 1:
        print('DEU EMPATE')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('O COMPUTADOR GANHOU')

    elif jogador == 1:
        print('O JOGADOR GANHOU')
    elif jogador == 2:
        print('DEU EMPATE')
    else:
        print('JOGADA INVALIDA')
