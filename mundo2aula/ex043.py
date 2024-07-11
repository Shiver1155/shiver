peso = int(input('Qual é seu peso?'))
altura = float(input('Qual é sua altura?'))

icm = peso / (altura ** 2)
if icm < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= icm < 25:
    print('NORMAL')
elif 25 <= icm < 30:
    print('SOBREPESO')
elif 30 <= icm < 35:
    print('OBESIDADE GRAU 1')
elif 35 <= icm < 40:
    print('OBESIDADE GRAU 2')
else:
    print('OBESIDADE GRAU 3')

