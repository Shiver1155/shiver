frase = str(input('digite uma frase')).strip().upper()
palavra = frase.strip()
junto = '' .join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um polindromo')
else:
    print('Nao forma um polindromo')
print(f'Inverso de {junto} é {inverso}')
