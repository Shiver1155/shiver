valores = [[], []]

for valor in range(1, 8):
    n = int(input(f'Digite o {valor} valor'))

    if n % 2 == 0:
        valores[0].append(n)

    elif n % 2 == 1:
        valores[1].append(n)

print(f'Os valores pares sao {valores[0]}')
print(f'os valores impares sao {valores[1]}')