valores = []
for valor in range(0, 5):
    n = int(input('Digite um valor: '))
    if not valor:
        valores.append(n)
        print('adicionado no final da fila')

    else:
        pos = 0
        while pos < len(valores) and n > valores[pos]:
            pos += 1
        valores.insert(pos, n)
        print(f'Adicionada na posicao {pos} ')

print(valores)