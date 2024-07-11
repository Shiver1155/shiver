a = int(input('primeiro valor'))
b = int(input('segundo valor'))
c = int(input('terceiro valor'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'menor valor {menor}')
print(f'maior valor {maior}')
