def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
def sun_for_fatorial(n):
    sun_fatorial = 0
    for i in range(1, n + 1):
        sun_fatorial += fatorial(i)
        print(f'{i}!', end='')
        print('x'if i > 1 else '=', end='')
    return fatorial(i)
n = int(input('qual o fatorial'))
print(f'{sun_for_fatorial(n)}')
