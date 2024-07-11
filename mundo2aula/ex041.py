from datetime import date
data = int(input('Digite sua idade'))
atual = date.today().year
soma = atual - data
print(f'IDADE {soma}')
if soma == 9 and 13:
    print('ATLETA MIRIM')
elif soma == 14 and 18:
    print('ATLETA JUNIOR ')
elif soma == 19 and 24:
    print('ATLETA SENIOR')
else:
    print('ATLETA MASTER ')
