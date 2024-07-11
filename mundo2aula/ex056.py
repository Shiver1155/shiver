somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'_______PESSOA NUMERO {c}_______')
    nome = str(input(f'Nome da pessoa n{c}')).strip()
    idade = int(input(f'Idade da psssoa n{c}'))
    sexo = str(input(f'Sexo da pessoa n{c} [M/F]')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mn':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'medias de idade {mediaidade}')
print(f'homen velho se chama {maioridadehomen} idade {nomevelho}')
print(f'ao todo sao {totmulher20} mulheres')
