maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Qual peso da {c}'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'maior {maior}')
print(f'menor {menor}')
