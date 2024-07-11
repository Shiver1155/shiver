cont = 0
n = tuple(int(input('Digite um valor')) for _ in range(4))
print(n)

print(f'O valor 9 apareceu {n.count(9)} vezes')

print(f'O valor 3 apareceu na posicao{n.index(3) + 1}')

for valor in n:
    if valor % 2 == 0:
        cont += 1
print(f'O valores pares apareceu {cont} vezes')