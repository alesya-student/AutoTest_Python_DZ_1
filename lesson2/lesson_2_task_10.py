x = float(input('Введите сумму: '))
y = int(input('Введите колтчество лет: '))
rate = (x * 0.1)


def bank(x, y):
    for y in range(y):
        x = (x + (y * rate))
    return x
print(bank(x, y))
