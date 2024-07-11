'''
n = int(input('Qual a tabuada?'))
for c in range(1, True):
    n1 = n * c
    print(f'{n}x{c}={n1}')
   '''


while True:
    n = int(input('Tabuada de: '))
    c = 1
    if n < 0:
        break


    while True:
        n1 = n * c
        print(f'{n}x{c}={n1}')
        c += 1
        
        if c == 11:
            break
