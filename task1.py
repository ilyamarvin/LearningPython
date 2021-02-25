import math


def f11(x, y):
    a = math.sqrt((20 * x ** 7 - math.exp(7)) / (math.exp(y) + x ** 7 + 84))
    b = (((x ** 3 / 88) - 97 * x ** 5) / (5 * y ** 5 + x ** 4))
    c = math.sqrt(53 * y ** 7 + 6 * x ** 4)
    return a - b + c


def f12(x):
    if x < 2:
        return x ** 8 + x ** 5 - 58
    elif 2 <= x < 25:
        return (x ** 8 + (x ** 4 / 27)) ** 6 + math.cos(x)
    elif 25 <= x < 80:
        return x ** 3 / 50 - x ** 2
    else:
        return math.sin((x ** 4 / 39) - x - 15) - 60 * x ** 7 + 19


def f13(n, m):
    a, b = 0, 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a += 20 * i ** 6 - math.exp(j)
        b += (36 * i ** 3 + 85 * i ** 4)
    return a + 49 * b


def f14(n):
    if n == 0:
        return 8
    elif n > 0:
        return abs(f14(n - 1)) + (1 / 87) * f14(n - 1) ** 2
    else:
        pass
