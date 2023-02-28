sum = int(input('Введите сумму двух задуманных чисел: '))
composition = int(input('Введите произведение двух задуманных чисел: '))
for x in range(1, 1000):
    for y in range(1, 1000):
        if x + y == sum and x * y == composition:
            print(x, y)