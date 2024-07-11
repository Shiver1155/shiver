
valores = []
for valor in range(0, 5):
    n = int(input(f'Digite um valor {valor}: '))
    if not valores:
        valores.append(n)
        print('adisionado no final da fila')
    else:
        pos = 0
        while pos < len(valores) and n > valores[pos]:
            pos += 1

        print(f'Adicionado na posicao {pos}')
        valores.insert(pos, n)
        print(valores)
print(valores)
