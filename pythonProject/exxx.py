def par():
    numero = 0
    while numero < 10:
        numero += 2
    return numero

def impar():
    numero = 0
    while numero < 10:
        numero += 3
    return numero

# Exemplo de uso
numero_par = par()
print("Número par:", numero_par)

numero_impar = impar()
print("Número ímpar:", numero_impar)
