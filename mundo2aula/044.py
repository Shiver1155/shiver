n1 = float(input('Valor do produto'))
print('''
[1] A VISTA
[2] A VISTA NO CARTAO
[3] PARCELA DE 2 VEZES
[4] PARCELA DE 3 VEZES''')
parcela = int(input('valor da parcela'))

if parcela == 1:
    total = n1 - 10
    print('A VISTA FICARA {:.2f}'.format(total))


elif parcela == 2:
    total = n1 + 10
    print('NO CARTAO FICARA {:.2f}'.format(total))


elif parcela == 3:
    total = n1 / 2
    print('EM DUAS VEZES FICARA {:.2f}'.format(total))


elif parcela == 4:
    total = n1 / 3
    print('EM TRES VEZES FICARA {:.2f}'.format(total))

