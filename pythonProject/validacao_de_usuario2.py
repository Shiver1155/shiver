senha = 'senha123'
tentativas = 0
while True:
    n = input('Digite uma senha: ')

    if n == senha:
        print('senha correta ')
        break

    elif n != senha:
        print('Senha incorreta')
        tentativas += 1
        if tentativas >= 3:
            print('conta bloqueada')
            break

