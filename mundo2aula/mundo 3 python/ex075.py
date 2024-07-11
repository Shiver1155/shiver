n = (int(input('Qual o valor')),
     int(input('Qual o valor')),
     int(input('Qual o valor')),
     int(input('Qual o valor')))
if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else:
    print('O valor 9 nao foi encontrado')

if 3 in n:
    print(f'O valor 3 apareceu {n.index(3) + 1} posicao')
else:
    print('O valor 3 nao foi encontrado')

print('Os valores pares foram ', end='')
for n1 in n:
    if n1 % 2 == 0:
        print(n1, end=' ')