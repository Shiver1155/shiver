nome = str(input('qual e seu nome'))
if nome == 'wesley':
    print('que nome bonito ')
elif nome == 'ana' or nome == 'bia' or nome == 'lucas':
    print('que nome normal')
elif nome in 'beatriz cladia julia':
    print('que nome feminino')
else:
    print('NOME NORMAL')
print('tenha um bom dia {}'.format(nome))
