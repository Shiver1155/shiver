
cor = {'amarelo': '\033[33m'}
limpar = {'limpar': '\033[0m'}

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove','dez', 'onze', 'doze', 'trez',
        'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    n = int(input('Digite um numero'))
    if 0 <= n <= 20:
        print(cor['amarelo'] + f'numero é {cont[n]}', limpar['limpar'])
    n1 = input('deseja continuar? [S/N]').upper()
    if n1 == 'N':
        break

