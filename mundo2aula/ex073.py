def cores():
    return  {
        'amarelo': '\033[41m',
        'verde': '\033[42m',
        'amarelo_claro': '\033[43m',
        'azul': '\033[44m',
        'limpar': '\033[0m'
    }


lista  = ('América-MG', 'Athletico-PR','Atlético-MG','Bahia','Botafogo','Corinthians',
        'Coritiba','Cruzeiro','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás',
        'Grêmio','Internacional','Palmeiras','Bragantino','Santos','São Paulo','Vasco da Gama',)
c = cores()
print(f"{c['amarelo']} Os 5 primeiros sao {lista[0:5]} {c['limpar']}" )
print(f" {c['verde']} os 5 ultimos sao {lista[15:20]} {c['limpar']} ")
print(f"{c['azul']} Em orden alfabetica {sorted(lista)} {c['limpar']}")
print(f"{c['amarelo_claro']} o cruzeiro esta na posicao {lista.index('Cruzeiro')} {c['limpar']}")


