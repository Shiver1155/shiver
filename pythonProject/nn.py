valores = [1, 2, 3, 4, 5, 6, 7]
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

print(segundo_menor_valor)
print(segundo_maior_valor)
print(menor)
print(maior)

