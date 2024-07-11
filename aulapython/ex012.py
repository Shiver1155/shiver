preco = float(input('Qual é o preco do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O preco do pruduto R${:.2f}, com 5% de desconto vai custar R${:.2f}'.format(preco,novo))
