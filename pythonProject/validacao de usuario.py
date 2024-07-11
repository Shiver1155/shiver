senha_correta = 'senha123'
senha = input('Digite a senha')
while senha != senha_correta:
    senha = input('Senha incorreta')
print('Senha correta')