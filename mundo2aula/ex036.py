casa = float(input('Valor do emprestimo'))
salario = float(input('salario do comprador'))
ano = int(input('Em quantos anos que financiar'))
prestacoes = casa / (ano * 12)
minimo = salario * 30 / 100
print('para pegar uma casa de {} em anos {}'.format(casa, ano), end='')
print('a prestacao sera {} '.format(prestacoes))
if minimo >= salario:
    print('APROVADO')
else:
    print('RECUSADO')
