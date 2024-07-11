valores = []
indece = 0
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    indece += 1
    n1 = str(input('Deseja sair [S/N]: '))
    if n1 == 's':
        break


if 5 in valores:
    print(f'valor 5 esta na lista')

else:
    print('o valor 5 nao esta na lista')
valores.sort(reverse=True)
print(f'Dados amazenados decrescente {valores}')
print(f'Voce digitou {indece} elementos')