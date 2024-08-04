def cores():
    return {'azul': '\033[34m',
            'limpar': '\033[0m',
            'vermelho': '\033[31m'}

def menu():
    cor = cores()
    print(cor['azul'], '''
    [1] separar pares e impares
    [2] matriz
    ''', cor['limpar'])
    n = int(input('Digite a opcao'))
    if n == 1:
        print('Voce escolheu a opcao [1] ')
        separar_pares_impares()


    elif n == 2:
        print('Voce escolheu a opcao [2] ')
        matrix()

def separar_pares_impares():

    valores = [[], []]

    for valor in range(1, 8):
        n = int(input('Digite um valor'))

        if n % 2 == 0:
            valores[0].append(n)
        elif n % 2 == 1:
            valores[1].append(n)

    print(valores[0])
    print(valores[1])

def matrix():

    valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for l in range(0, 3):
        for c in range(0, 3):
            valores[l][c] = int(input(f'Digite a matrix {l} {c}'))

    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{valores[l][c]:^5}]', end='')
        print()

if __name__ == "__main__":
    menu()