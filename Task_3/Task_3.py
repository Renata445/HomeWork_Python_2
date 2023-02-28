N = int(input('Введите число N: '))
a, k = 1, 1
while a * k <= N:
    print(a * k, end=' ')
    k = k * 2