#2.1
# a)
x = float(input("Введите x: "))
y = 17 * x**2 - 6 * x + 13
print("y =", y)

# б)
a = float(input("Введите a: "))
y = 3 * a**2 + 5 * a - 21
print("y =", y)

#2.2
import math

a = float(input("Введите a: "))
y = (a**2 + 10) / math.sqrt(a**2 + 1)
print("y =", y)

#2.3
import math

# a)
a = float(input("Введите a: "))
y = math.sqrt((2 * a + math.sin(abs(3 * a))) / 3.56)
print("y =", y)

# б)
x = float(input("Введите x: "))
y = math.sin((3.2 + math.sqrt(1 + x)) / abs(5 * x))
print("y =", y)

#2.4
a = float(input("Введите сторону квадрата: "))
P = 4 * a
print("Периметр квадрата =", P)

#2.5
r = float(input("Введите радиус окружности: "))
d = 2 * r
print("Диаметр окружности =", d)

#2.6
import math

R = 6350  # радиус Земли, км
h = float(input("Введите высоту точки над Землей (км): "))
distance = math.sqrt((R + h)**2 - R**2)
print("Расстояние до линии горизонта =", distance, "км")

#2.7
a = float(input("Введите длину ребра куба: "))
V = a**3
S = 4 * a**2
print("Объем куба =", V)
print("Площадь боковой поверхности =", S)

#2.8
import math

r = float(input("Введите радиус окружности: "))
C = 2 * math.pi * r
S = math.pi * r**2
print("Длина окружности =", C)
print("Площадь круга =", S)

#2.9
import math

# a)
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = 2 * x**3 - 3.44 * x * y + 2.3 * x**2 - 7.1 * y + 2
print("z =", z)

# б)
a = float(input("Введите a: "))
b = float(input("Введите b: "))
z = 3.14 * (a + b)**3 + 2.75 * b**2 + 1.7 * a - 4.1
print("z =", z)

#2.10
import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

avg = (a + b) / 2
geom = math.sqrt(a * b)

print("Среднее арифметическое =", avg)
print("Среднее геометрическое =", geom)

#2.11
m = float(input("Введите массу тела (кг): "))
V = float(input("Введите объем тела (м^3): "))
density = m / V
print("Плотность материала =", density, "кг/м^3")

#2.12
N = float(input("Введите количество жителей (чел): "))
S = float(input("Введите площадь территории (км^2): "))
density = N / S
print("Плотность населения =", density, "чел/км^2")