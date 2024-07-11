velocidade = float(input('Qual e a minha velocidade ?'))
if velocidade > 80:
    print('MULTADO! Voce ultrapassou a velocidade da via de 80 km')
    multa = (velocidade - 80) * 7
    print(f'VALOR DA MULTA {multa}')
print('dirija com atencao')
