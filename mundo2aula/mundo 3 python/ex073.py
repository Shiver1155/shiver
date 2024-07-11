def separa():
    print('-=-' * 20)

cores = {'amarelo': '\033[33m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'limpar': '\033[0m'}

times_brasileirao = ['Flamengo', 'Internacional', 'Atlético-MG',
                     'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
                     'Santos', 'Athletico-PR', 'Bragantino', 'Ceará',
                     'Corinthians', 'Atlético-GO', 'Bahia', 'Sport',
                     'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo']
separa()
print(cores['azul'] + f'Os 5 primeiros {times_brasileirao[:5]}' + cores['limpar'])

separa()
print(cores['verde'] + f'{times_brasileirao[7]} oitava posicao' + cores['limpar'])

separa()
print(cores['vermelho'] + f'Os 4 ultimos {times_brasileirao[-4:]}' + cores['limpar'])
separa()

times_brasileirao.sort()


print(cores['amarelo'] + 'em irdem alfabetica' + cores['limpar'], times_brasileirao[:20])
separa()
