from time import sleep


def cores():
    return {'vermelho': '\033[31m',
            'azul': '\033[34m',
            'limpar': '\033[0m'}


lista = []
while True:
    cor = cores()
    print('''\nMenu:
[1] ADICIONAR
[2] REMOVER
[3] EXIBIR LISTA
[4] SAIR 
    ''')

    add = int(input('Digite um valor '))

    if add == 1:
        n = str(input('Adicionar'))
        lista.append(n)
        print(f'{cor["azul"]}adicionado {n} {cor["limpar"]}')
        print(lista)

    elif add == 2:
        if lista:
            valor = str(input('Deletar: '))
            if valor in lista:
                lista.remove(valor)
                print(f"{cor['vermelho']} Item removido {valor} {cor['limpar']}")
                print(f'Lista atualizada {lista}')
            else:
                print('Item nao encotrado')
        else:
            print('Valor nao encotrado')

    elif add == 3:
        print(f'A lista exibida {lista}')
    elif add == 4:
        print('Saindo', end=' ')
        print('.', end=' ')
        sleep(0.5)
        print('.', end=' ')
        sleep(0.5)
        print('.', end=' ')
        break
    else:
        print('opcao invalida. tente novamente')
