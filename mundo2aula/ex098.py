
from time import sleep

def main():
    print('-=' * 20)
    print('Contagem de 1 ate 10 de 1 em 1')
    
    
    for i in range(1, 11):
        print(f'{i}', end=' ', flush=True)
        sleep(0.3)
    print('FIM')
    print('-=' * 20)

    print('COntagem de 10 ate 0 em 2 em 2')
    for i in range(10, -1, -2):
        print(f'{i}', end=' ', flush=True)
        sleep(0.3)
    print('FIM')
    print('-=' * 20)


def contador(Inicio, Fim, Passos):
    if Passos < 0:

        print('-=' * 20)
        print(f'Contagem de {Inicio} ate {Fim} de {Passos} em {Passos}')
        for p in range(Inicio, -Fim, Passos):
            print(f'{p}', end=' ', flush=True)
            sleep(0.3)
        print('FIM')


    if Inicio < Fim:

        print('-=' * 20)
        print(f'Contagem de {Inicio} ate {Fim} de {Passos} em {Passos}')
        for p in range(Inicio, Fim, Passos):
            print(f'{p}', end=' ', flush=True)
            sleep(0.3)
        print('FIM')

    else:

        print('-=' * 20)
        print(f'Contagem de {Inicio} ate {Fim} de {Passos} em {Passos}')
        for p in range(Inicio, Fim - 1, -Passos):
            print(f'{p}', end=' ', flush=True)
            sleep(0.3)
        print('FIM')


if __name__ == '__main__':
    main()

Inicio1 = int(input('Inicio: '))
Fim2 = int(input('Fim: '))
Passos3 = int(input('Passos: '))
contador(Inicio1, Fim2, Passos3)

