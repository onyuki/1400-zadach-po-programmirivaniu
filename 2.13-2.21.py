#2.13

a = float(input("Введите a: "))
b = float(input("Введите b: "))

if a != 0:
    x = -b / a
    print("Решение уравнения: x =", x)
else:
    print("Ошибка: a не должно быть равно 0")

#2.14


import math

a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))

c = math.sqrt(a**2 + b**2)
print("Гипотенуза =", c)

#2.15

import math

r1 = float(input("Введите внешний радиус: "))
r2 = float(input("Введите внутренний радиус: "))

if r1 > r2:
    s = math.pi * (r1**2 - r2**2)
    print("Площадь кольца =", s)
else:
    print("Ошибка: внешний радиус должен быть больше внутреннего")

#2.16


import math

a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))

c = math.sqrt(a**2 + b**2)
P = a + b + c
print("Периметр =", P)

#2.17


import math

a = float(input("Введите основание a: "))
b = float(input("Введите основание b: "))
h = float(input("Введите высоту h: "))

side = math.sqrt(((a - b) / 2)**2 + h**2)
P = a + b + 2 * side
print("Периметр =", P)

#2.18


import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))

z = (x + 2 * y) / (x ** 2)
q = 7.25 * math.sin(x) - abs(y)
h = math.sqrt(x ** 2 + 10)

print(f"z = {z}\nq = {q}\nh = {h}")

#2.19


import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))

x = 2 / math.sqrt(b + a / b)
y = abs(a) / b - (2 * math.sin(b)) / (5.5 * a)

print(f"x = {x}\ny = {y}")

#2.20


import math

e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))

a = (3 / f) ** (1/3)
b = g - math.sin(e) + math.cos(h)**2
c = 33 * g / (e * f - 3)

print(f"a = {a}\nb = {b}\nc = {c}")

#2.21


import math

e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))

y = (e + f) / 3
b = abs(h ** 2 - 6)
x = ((e - g) ** 3 - 5 * math.sin(e)) / 3

print(f"y = {y}\nb = {b}\nx = {x}")

#2.22


import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

avg_arith = (abs(a) + abs(b)) / 2
avg_geom = math.sqrt(abs(a) * abs(b))

print(f"Среднее арифметическое модулей = {avg_arith}")
print(f"Среднее геометрическое модулей = {avg_geom}")
