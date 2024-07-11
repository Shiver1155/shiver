from random import randint
from time import sleep
computador = randint(0, 5)
print('pense em um numero entre 0 ou 5 ')
jogador = int(input('Em que numero eu pensei ?'))
print('PROCESSADOR...')
sleep(2)
if jogador == computador:
    print(f'EU GANHEI! PENSEI NO {computador}')
else:
    print(f'VOCE PERDEU! PENSEI NO {computador}')
