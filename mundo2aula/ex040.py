n1 = float(input('Digite um valor'))
n2 = float(input('Digite outro valor'))
n3 = (n1 + n2) / 2
print(f'o aluno tirando {n1} e {n2} a media é {n3}')
if n3 > 7:
    print('O ALUNO FOI APROVANDO')
elif n3 == 5 or 6.9:
    print('O ALUNO ESTA DE RECUPERACAO')
elif n3 < 5:
    print('O ALUNO FOI REPROVADO')
