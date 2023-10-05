def round_number(a, b):
    c = round(a, b)
    return c

# не используем запятые для перечесления - лишь точку.
d = float(input("Введите число: "))
e = int(input("Введите количество знаков после запятой: "))

f = round_number(d, e)

print("Округленное число:", f)
