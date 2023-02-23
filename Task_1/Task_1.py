n = int(input('Введите кол-во монеток: '))
sum = 0
for i in range(1, n + 1):
    a = int(input('Введите числа: ')) # Допустим решка это 1, а герб это 0
    sum += a
if sum <= n / 2:
    print(sum)
else:
    print(n - sum)