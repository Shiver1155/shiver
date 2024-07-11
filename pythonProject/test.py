

lista = [1, 2]


valor = int(input('Digite '))

if valor in lista:
    lista.remove(valor)
    print(valor)
print(lista)