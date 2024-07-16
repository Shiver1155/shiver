valores = []

n = str(input('Digite um valor'))
for simb in n:
    if simb == '(':
        valores.append(')')
    elif simb == ')':
        if len(valores) > 0:
            valores.pop()
        else:
            valores.append(')')
if len(valores) > 0:
    print('formula errada')
else:
    print('formula correta')
