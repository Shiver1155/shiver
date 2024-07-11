def cores():
    return{
        'amarelo': '\033[33m',
        'azul': '\033[41m',
        'limpar': '\033[0m'
    }

lista = (
    'curso', 'video', 'python'
)

for listagem in lista:
    print(f'na palavra {listagem} temos', end=' ')
    c = cores()
    for vogal in listagem:
        if vogal in 'aeiou':
            print(f"{c['amarelo']} {vogal} {c['limpar']}",end=' ')
    print()