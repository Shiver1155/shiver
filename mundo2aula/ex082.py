valores = []
par = []
impar = []
while True:
    n = int(input('Digite um numero'))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
    n1 = str(input('Deseja sair? S/N')).upper()
    if n1 == 'S':
        break
print(f'A lista de valores {valores}')
print(f'Essa Lista e par {par}')
print(f'Essa lista e impar {impar}')
