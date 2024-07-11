valores = []
valor_unico = set()
while True:
    n = int(input('Digite um valor'))
    valores.append(n)
    valor_unico.add(n)
    n1 = str(input('Deseja continuar? [s/n]'))
    if n1 == 'n':
        break
print(f'Os valores amazenados "sem tratamento" {valores} ')
print(f'Os valores amazenados "com tratamento" {sorted(valor_unico)}')