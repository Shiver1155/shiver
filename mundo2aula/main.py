preco = float(input('Qual o valor '))
print('-=-' * 7)
print('''
[1] A VISTA
[2] A VISTA NO CARTAO
[3] PARCELADO DUAS VEZES
[4] PARCELADO TREZ VEZES''')
print('-=-' * 7)
parcela = float(input('A VISTA OU PARCELADO?'))

if parcela == 1:
    total = preco - (preco * 2/100)
    print('O VALOR É {:.2f} COM DESCONTO SERÁ {:.2f}'.format(preco, total))

elif parcela == 2:
    total = preco - (preco * 3/100)
    print('O VALOR É {:.2f} COM DESCONTO SERÁ {:.2f}'.format(preco, total))

elif parcela == 3:
    total = preco / 2
    print('O VALOR É {:.2f} COM DESCONTO SERÁ {:.2f}'.format(preco, total))

elif parcela == 4:
    total = preco / 3
    print('O VALOR É {:.2f} COM DESCONTO SERÁ {:.2f}'.format(preco, total))

