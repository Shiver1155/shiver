n1 = float(input('primeiro triangulo'))
n2 = float(input('segundo triangulo'))
n3 = float(input('terceiro triangulo'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('formar um triangulo')
else:
    print('nao forma')
