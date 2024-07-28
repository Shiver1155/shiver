pessoas = []
while True:
    nome = str(input('Nome'))
    peso = int(input('peso'))

    pessoas.append([nome, peso])

    n2 = str(input('Deseja sair:'))
    if n2.upper() in 'Ss':
        break

maior = max(p[1] for p in pessoas)

menor = min(p[1] for p in pessoas)

for p in pessoas:
    if p[1] == maior:
        print(f' O mais pessado {p[0]} com {p[1]} quilos')

for p in pessoas:
    if p[1] == menor:
        print(f'O mais leve {p[0]} com {p[1]} quilos')
