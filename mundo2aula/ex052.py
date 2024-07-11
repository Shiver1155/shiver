num = int(input('digite um valor'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m ', end=' ')
    print(f' {c}', end='')
print(f'\033[m O valor {num} foi divisivel por {tot}')
if tot == 2:
    print('\033[34m Esse valor é PRIMO')
else:
    print('\033[36m Esse valor nao é PRIMO')
