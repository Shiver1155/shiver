distancia = float(input('Qual a distancia da sua viagem'))
print(f'voce esta preste a comecar a viagem de {distancia}')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'preco da sua passagem e {preco}')
