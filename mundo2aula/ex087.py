matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l} {c} '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

soma_pares = []
for p in matriz:
    for linha in p:
        if linha % 2 == 0:
            soma_pares.append(linha)

print(f'A soma dos valores pares é {sum(soma_pares)}')
coluna = []
for p in matriz:
    if p[2]:
        coluna.append(p[2])

print(f'A soma dos valores da terceira coluna é {sum(coluna)}')

maior = max(matriz[1])
print(f'O maior valor da segunda linha é {maior}')
