valores = []
for valor in range(0,5):
    n = int(input(f'Digite um valor para posicao {valor}: '))
    valores.append(n)
print(valores)
maior = max(valores)
menor = min(valores)

segundo_maior_valor = float('-inf')
for valor in valores:
    if maior > valor > segundo_maior_valor:
        segundo_maior_valor = valor

segundo_menor_valor = float('inf')
for valor in valores:
    if menor < valor < segundo_menor_valor:
        segundo_menor_valor = valor

print(f'O maior valor foi {maior} nas posiçoes ',end=' ')
for indece, valor in enumerate(valores):
    if valor == maior:
        print(f'{indece}...', end=' ')
print()
print(f'O menor valor foi {menor} nas posiçoes ',end=' ')
for indece, valor in enumerate(valores):
    if valor == menor:
        print(f'{indece}...', end=' ')
print()

print(f'Voce digitou os valores {valores}')
print(f'O segundo valor Maior {segundo_maior_valor} na posicao')
print(f'O segundo menor valor foi {segundo_menor_valor}')