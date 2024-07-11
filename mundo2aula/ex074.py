cont = 0
b = (
    int(input('Digite um valor')),
    int(input('Digite um valor')),
    int(input('Digite um valor')),
    int(input('Digite um valor')))

print(f'o numero 9 apareceu {b.count(9)}')
print(f'o numero 3 apareceu {b.index(3)}')
for c in b:
    if c % 2 == 0:
        cont += 1
print(f'Os valores pares foram {cont}')