
primeiro_termo = int(input('Digite um numero'))
razao = int(input('Digite um valor'))
termo = primeiro_termo
total = 0
cont = 1
mais = 10
while mais != 0:
    total = total + mais

    while cont <= total:
        print(f'{termo} >', end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quanto termo voce quer?'))
print('fim')