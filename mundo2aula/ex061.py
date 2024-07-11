
primeiro_termo = int(input('Digite um numero'))
razao = int(input('Digite um valor'))
termo = primeiro_termo

cont = 1
while cont <= 10:
    print(f'{termo} >', end='')
    termo += razao
    cont += 1


