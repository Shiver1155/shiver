primeiro = int(input('Primeiro termo'))
razao = int(input('razao'))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' > ' )
print('acabou')
