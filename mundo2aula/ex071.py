valor = int(input('Digite um valor'))

notas = [50, 20, 10, 1]

for nota in notas:
    quantidade = valor // nota
    valor %= nota
    if quantidade > 0:
        print(f'total de {quantidade} e r${nota}')