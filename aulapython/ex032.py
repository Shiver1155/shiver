from datetime import date
ano = int(input('Que ano quer analizar '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'ano {ano} é bissexto')
else:
    print(f'o ano {ano} nao é bissexto')
