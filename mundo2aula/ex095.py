import os
dic = dict()
lista = list()

while True:
    os.system('cls')
    dic['nome'] = nome = str(input('Nome: '))
    partida = int(input(f'Quantas partidas {dic["nome"]} jogou: '))

    gols_por_partidas = []
    for i in range(1, partida + 1):
        gols_por_partidas.append(int(input(f'Quantos gols na partida {i}? ')))

    dic['gols'] = gols_por_partidas
    dic['total'] = somar_gols = sum(gols_por_partidas)

    lista.append(dic.copy())
    
    n = str(input('Para sair [S]')).upper()
    if n == 'S':
        break

print('-=' * 25)
print('cod', end='')
for k in dic.keys():
    print(f'{k:>15}', end='')
print()
print('-' * 50)
for i, pessoa in enumerate(lista):
    print(f'{i} {pessoa["nome"]:>15} {str(pessoa["gols"]):>15} {pessoa["total"]:>13}')
print('-' * 50)


while True:
    buscar = int(input('Mostar dados de qual jogador? (999 para sair)'))

    if buscar == 999:
        break
    if buscar >= len(lista):
        print(f'ERRO! nao existe Jogador com codigo {buscar}')
        
    else:
        print(f'LEVANTAMENTO DO JOGADOR {lista[buscar]["nome"]}')
        for i, g in enumerate(lista[buscar]['gols']):
            print(f'No jogo{i} fez {g} gols')
