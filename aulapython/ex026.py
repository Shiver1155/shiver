frase = str(input('digite uma frase')).upper().strip()
print('A letra aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra apareceu na posicao {} '.format(frase.find('A')+1))
print('A ultima letra apareceu na posicao {} '.format(frase.rfind('A')+1))
