from random import randint
from time import sleep
n = int(input('Digite um valor'))


for c in range(0, n):
    print(f'jogo {c}:', end=' ')
    for l in range(0, 6):
        num_alea = randint(0, 60)
        print(num_alea, end=' ')
    print()
    sleep(1)