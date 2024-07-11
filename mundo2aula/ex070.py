


valores = []
produtos = {}
cont_acima_de_mil = 0

while True:
    
    n = input('Nome do produto: ')
    n1 = int(input('Valor do produto: '))
    valores.append(n1)
    produtos[n] = n1
   
    if n1 > 1000:
        cont_acima_de_mil += 1


    n2 = input('Deseja continuar? [S/N]').upper()
    if n2 == 'N':
        break
   
soma = sum(valores)
menor_valor = min(produtos, key=produtos.get)
print(f'A soma dos produto foram {soma}')
print(f'menor valor {menor_valor}')
print(f'{cont_acima_de_mil} produto de R$1000 ')
