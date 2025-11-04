#import math - для всех мат. функций!

# 4.1
def compare_two(a, b):
    if a == b:
        return "числа равны (по условию должны быть различны)"
    bigger = a if a > b else b
    smaller = b if a > b else a
    return f"большее: {bigger}, меньшее: {smaller}"

# 4.2
def compute_y_4_2(x):
    s2 = math.sin(x) ** 2
    if x > 0:
        return s2
    else:
        return 1 - 2 * s2

# 4.3
def compute_y_4_3(x):
    s2 = math.sin(x) ** 2
    if x > 0:
        return s2
    else:
        return 1 + 2 * s2

# 4.4
def classify_4_4(x, y):
    if y > 0 and 0 < x < 4:
        return "I"
    elif y > 0 and x > 4:
        return "II"
    else:
        return "точка не принадлежит I или II (либо на/за пределом областей)"

# 4.5
def classify_4_5(x, y):
    if y > 3:
        return "I"
    elif 0 < y < 3 and x > 0:
        return "II"
    else:
        return "точка не принадлежит I или II (либо на/за пределом областей)"

import math

# 4.6
def f_graph_a(x: float) -> float:
    if x <= 2:
        return x
    else:
        return 2.0

def f_graph_b(x: float) -> float:
    if x < 3:
        return -x
    else:
        return -3.0

# 4.7
def f_4_7(x: float) -> float:
    k = x*x if math.sin(x) < 0 else abs(x)
    if k < x:
        return k * x
    else:
        return k + x

# 4.8
def f_4_8(x: float) -> float:
    k = x*x if math.sin(x) >= 0 else abs(x)
    if x < k:
        return abs(x)
    else:
        return k * x

# 4.9
def min_max(a: float, b: float):
    if a < b:
        return a, b
    else:
        return b, a

# 4.10
def compare_dist(kilometers: float, feet: float):
    meters_from_km = kilometers * 1000.0
    meters_from_ft = feet * 0.3048
    if meters_from_km < meters_from_ft:
        return "kilometers", meters_from_km, meters_from_ft
    elif meters_from_km > meters_from_ft:
        return "feet", meters_from_km, meters_from_ft
    else:
        return "equal", meters_from_km, meters_from_ft

# 4.11.
def compare_speeds(v1_kmh, v2_ms):
    v2_kmh = v2_ms * 3.6
    if abs(v1_kmh - v2_kmh) < 1e-12:
        return "равны"
    return "v1 больше" if v1_kmh > v2_kmh else "v2 больше"

# 4.12
def compare_circle_square(r, a):
    area_circle = math.pi * r * r
    area_square = a * a
    if abs(area_circle - area_square) < 1e-12:
        return "площади равны"
    return "круг больше" if area_circle > area_square else "квадрат больше"

# 4.13
def compare_density(v1, m1, v2, m2):
    rho1 = m1 / v1
    rho2 = m2 / v2
    if abs(rho1 - rho2) < 1e-12:
        return "плотности равны"
    return "первого материала плотность больше" if rho1 > rho2 else "второго материала плотность больше"

# 4.14
def smaller_current(R1, U1, R2, U2):
    I1 = U1 / R1
    I2 = U2 / R2
    if abs(I1 - I2) < 1e-12:
        return "токи равны"
    return "в первом участке меньший ток" if I1 < I2 else "во втором участке меньший ток"

# 4.15
def has_real_roots(a, b, c):
    D = b*b - 4*a*c
    return D >= 0

# 4.16
def solve_quadratic(a, b, c):
    if abs(a) < 1e-15:
        raise ValueError("a должно быть отличным от 0")
    D = b*b - 4*a*c
    if D < 0:
        return "вещественных корней нет"
    elif abs(D) < 1e-12:
        x = -b / (2*a)
        return (x,)
    else:
        sqrtD = math.sqrt(D)
        x1 = (-b + sqrtD) / (2*a)
        x2 = (-b - sqrtD) / (2*a)
        return (x1, x2)

# 4.17
def full_years(birth_year, birth_month, cur_year, cur_month):
    years = cur_year - birth_year
    if cur_month < birth_month:
        years -= 1
    return years if years >= 0 else 0


# 4.18
def circle_square_fit(S_c, S_s):
    r = math.sqrt(S_c / math.pi)
    side = math.sqrt(S_s)

    circle_in_square = (2 * r) <= side + 1e-12

    diag = side * math.sqrt(2)
    square_in_circle = diag <= 2 * r + 1e-12
    return circle_in_square, square_in_circle

# 4.19
def circle_triangle_fit(S_c, S_t):
    r_c = math.sqrt(S_c / math.pi)

    a = math.sqrt(4 * S_t / math.sqrt(3))
    r_in = (math.sqrt(3) / 6) * a
    R_circum = a / math.sqrt(3)
    circle_in_triangle = r_c <= r_in + 1e-12
    triangle_in_circle = R_circum <= r_c + 1e-12
    return circle_in_triangle, triangle_in_circle

# 4.20
def bounding_rectangle(rect1, rect2):
    x1 = min(rect1[0], rect2[0])
    y1 = min(rect1[1], rect2[1])
    x2 = max(rect1[2], rect2[2])
    y2 = max(rect1[3], rect2[3])
    return (x1, y1, x2, y2)

# 4.21
def bounding_rectangle_from_pos(rect1, rect2):
    x11, y11, w1, h1 = rect1
    x21, y21, w2, h2 = rect2
    r1 = (x11, y11, x11 + w1, y11 + h1)
    r2 = (x21, y21, x21 + w2, y21 + h2)
    return bounding_rectangle(r1, r2)

# 4.22
def divide_or_message(n, m):
    if m == 0:
        return "деление на ноль"
    if n % m == 0:
        return n // m
    return f"{n} на {m} не делится"

# 4.23
def is_divisor(a, n):
    if a == 0:
        return False
    return n % a == 0

# 4.24
def task_4_24(n):
    is_even = (n % 2 == 0)
    ends_with_7 = (abs(n) % 10 == 7)
    return is_even, ends_with_7

# 4.25
def task_4_25(n):
    return n + 1


















