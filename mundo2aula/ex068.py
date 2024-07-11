from random import randint
cont = 0
while True:
    
    pc = randint(0, 10)
    jogador = int(input('Digite um Valor: '))
    opcao = input('Ímpar ou Par? [I/P]: ').upper()
    cont += 1
    while opcao not in 'PI':
        opcao = input('OPcao invalida, tente [P ou I]: ')
    soma = pc + jogador
    if soma % 2 == 0:
        resultado = 'P'
    elif soma % 2 == 1:
        resultado = 'I'
    print(f'Maquina escolheu {pc}')
    if opcao == resultado:
        print('Voce Ganhou')
    else:
        print('Voce Perdeu')
        break
    
    print(f'Resultado deu {resultado}')
print(f'{cont} Nuneros digitados')
