valores = []

n = input('Digite uma formula')
for simb in n:
    if simb == '(':
        valores.append('(')
    elif simb == ')':
        if len(valores) > 0:
            valores.pop()
        else:
            valores.append(')')
            break
if len(valores) == 0:
    print('Formula correta')
else:
    print('Formula incorreta')
