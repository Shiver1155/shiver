valores = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor '))
    valores.append(n)

    if n % 2 == 0:
        pares.append(n)
        

    elif n % 2 == 1:
        impares.append(n)
        

    n1 = str(input('Deseja continuar? [S/N]')).upper()
    if n1 == 'N':
        break

print(f'os valores sao {valores}')
print(f'valores pares {pares}')
print(f'valores impare {impares}')