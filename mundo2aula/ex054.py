from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'EM QUE ANO A {pess} PESSOA NASCEU?'))
    idade = atual - nasc


    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Sao {totmaior} Pessoas de maior ')
print(f'Sao {totmenor} Pessoas de menor')
