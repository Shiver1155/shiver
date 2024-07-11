valores = [2, 4, 5, 6, 9, 0, 6, 0]
maior = max(valores)
valores_ondenados = sorted(valores)
valores_decrescente = sorted(valores, reverse=True)

print(valores_ondenados, valores_decrescente)
segundo_maior = float('-inf')
for valor in valores:
    if maior > valor > segundo_maior:
        segundo_maior = valor
print(segundo_maior, maior)
