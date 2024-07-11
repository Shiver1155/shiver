lista = ('ovo', 2.99, 'banana', 3.99)


for listagem in lista:
    if isinstance(listagem, str) % 2 == 1:
        print(f'{listagem :.<30}', end='R$ ')

    elif isinstance(listagem, int) % 2 == 0:
        print(listagem)