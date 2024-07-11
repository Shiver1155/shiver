num = int(input('digite um numero inteiro'))
print('''
[1] binario
[2] octal
[3]exagonimal''')
opcoes = int(input('converta'))
if opcoes == 1:
    print('{} binario {}'.format(num, bin(num)[2:]))
elif opcoes == 2:
     print('{} octal {}'.format(num, oct(num)[2:]))
elif opcoes == 3:
    print('{} exagonal {}'.format(num, hex(num)[2:]))
else:
    print('invalido')
