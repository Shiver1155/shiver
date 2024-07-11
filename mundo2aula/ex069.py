cont = 0
mulher = 0 
homen = 0 
abaixo_de_20 = 0

while True:
    idade = int(input('Idade'))
    n1 = str(input('[M/F]: ' )).upper()
    n = input('Quer continuar? [S/N]').upper()
    if n == 'N':
        print('FIM')
        break

    if n1 == 'F' :
        mulher += 1  
    if n1 == 'M':
        homen += 1

    if idade < 20:
        abaixo_de_20 += 1

    if idade > 18:
        cont += 1
        
   
print(f'Mulher cadastrada {mulher}') 
print(f'{abaixo_de_20} mulheres abaixo de 20 anos cadastrado')
print(f'homen cadastrado {homen}')
print(f'pessoas com mais de 18 anos: {cont}')



