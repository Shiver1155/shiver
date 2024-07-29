def cores():
    return {'azul': '\033[34m',
            'vermelho': '\033[31m',
            'limpar': '\033[0m'}

def verificar_formula():

    valores = []
    n = input('Digite um valor')
    for simb in n:
        if simb == '(':
            valores.append('(')
        elif len(valores) > 0:
            if simb == ')':
                valores.pop()
        else:
            valores.append(')')
            break

    cor = cores()

    if len(valores) == 0:
        print(cor['azul'], 'Formula correta', cor['limpar'])
    else:
        print(cor['vermelho'], 'Formula incorreta', cor['limpar'])


if __name__ == "__main__":
    verificar_formula()
