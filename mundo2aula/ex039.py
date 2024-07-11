from datetime import date
atual = date.today().year
print('ALISTAMENTO MILITAR')
data = int(input('digite sua data de nascimento'))
soma = atual - data

print('')
if soma == 18:

    print('IDADE APROVADA')
    print(f'VOCE TEM {soma} ANOS')

elif soma > 18:
    n1 = 18 + data
    print(f'VOCE ULTRAPASSOU O LIMITE DE IDADE ')
    print(f'DEVIA SER ALISTAR EM {n1}')

elif soma < 18:
    n4 = 18 - soma
    print('VOCE NAO ATINGIU A IDADE ')
    print(f'FALTAM {n4} ANOS PARA SER ALISTAR')
