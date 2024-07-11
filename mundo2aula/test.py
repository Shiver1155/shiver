valores = [1, 2, 4,  6, 8]

if 5 in valores:
    print(f'valor 5 esta na lista')

else:
    print(f'valor 5 nao esta presente')
    
print(valores.count(6))
print(valores.index(6))
print(valores[5:])