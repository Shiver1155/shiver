soma = 0
valores = []
cont = 1
while True:
    n = int(input('Qual o Valor'))
    valores.append(n)
    n1 = input('Deseja Sair? S/N').upper()
    if n1 == 'S':
        break
    cont += 1
soma = sum(valores)
maior = max(valores)
menor = min(valores)
media = soma / len(valores)
print(f'maior : {maior}, menor :{menor}, media : {media}, cont:{cont}')
