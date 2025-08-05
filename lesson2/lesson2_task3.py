import math


def square(s):
    return math.ceil(s * s)


length = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата равна {(square(length))}")
