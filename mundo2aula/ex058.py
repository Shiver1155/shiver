from random import randint
pc = randint(1, 10)
print(f'{pc}')
jogador = int(input('Tente adivilhar de 1 a 10 '))
acertou = False
palpite = 0
while not acertou:
    palpite += 1
    if pc > jogador:
        print('maior')
    elif pc < jogador:
        print('menor')
    elif pc == jogador:
        print('ganhou')
        acertou = True
    print(f'tentativa {palpite}')
    jogador = int(input('tente de novo'))

