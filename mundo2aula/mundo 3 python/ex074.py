from random import randint
sorteio = [randint(1, 10) for _ in range(4)]
maior = max(sorteio)
menor = min(sorteio)
print(sorteio)
print(f'O maior valor é {maior} e o menor valor é {menor}')
