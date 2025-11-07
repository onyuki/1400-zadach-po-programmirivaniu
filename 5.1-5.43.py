 #  5.1
def print_row(value=20, count=9):
    print(" ".join(str(value) for _ in range(count)))

 # 5.2
def print_repeated_number(x, count=9):
    print(" ".join(str(x) for _ in range(count)))

 # 5.3
 # a
def part_a():
    for i in range(20, 36):
        print(i)

 # b
def part_b():
    a = int(input("Введите a (a <= 50): "))
    for i in range(a, 51):
        print(i*i)

 # c
def part_c():
    b = int(input("Введите b (b >= 10): "))
    for i in range(10, b+1):
        print(i**3)

 # d
def part_d():
    a = int(input("Введите a: "))
    b = int(input("Введите b (b > a): "))
    for i in range(a, b+1):
        print(i)

 # 5.7
def price_table(unit_price=20.4, start=2, stop=20):
    print("Кол-во  Стоимость")
    for k in range(start, stop+1):
        print(f"{k:>5}  {k*unit_price:>8.2f}")

 # 5.8
def pounds_to_kg_table(max_pounds=10, grams_per_pound=453):
    print("Фунты  Кг")
    for p in range(1, max_pounds+1):
        kg = p * grams_per_pound / 1000.0
        print(f"{p:>6} {kg:>6.3f}")

 # библиотека для задач ниже ->
import math

 # 5.9
def p5_9():
    # 5.9: дюймы -> сантиметры для 10..22 дюйма (1 in = 2.54 cm)
    print("5.9: дюймы -> сантиметры")
    for inches in range(10, 23):
        cm = inches * 2.54
        print(f"{inches} in = {cm:.2f} cm")
    print()

 # 5.10
def p5_10():
    rate = float(input("5.10: Введите курс (рублей за 1 доллар): "))
    print("Доллары -> Рубли")
    for usd in range(1, 21):
        rub = usd * rate
        print(f"${usd} = {rub:.2f} руб.")
    print()

 # 5.11
def p5_11():
    R = 6350.0
    print("5.11: расстояние до линии горизонта (R=6350 км)")
    print("h(км) | d_line_of_sight(km) | arc_length_on_surface(km)")
    for h in range(1, 11):
        d = math.sqrt((R + h) ** 2 - R ** 2)
        arg = R / (R + h)
        arg = min(1.0, max(-1.0, arg))
        s = R * math.acos(arg)
        print(f"{h:4d}  | {d:18.6f} | {s:18.6f}")
    print()

 # 5.12
def p5_12():
    p0 = 1.29
    k = 1.25e-4
    print("5.12: плотность воздуха p(h) (кг/м^3)")
    for h in range(0, 1001, 100):
        p = p0 * math.exp(-k * h)
        print(f"h = {h:4d} m -> p = {p:.6f} kg/m^3")
    print()

 # 5.13
def p5_13():
    print("5.13: Таблица умножения на 7")
    for i in range(1, 10):
        print(f"{i} x 7 = {i*7}")
    print()

 # 5.14
def p5_14():
    print("5.14: Таблица умножения на 9")
    for i in range(1, 10):
        print(f"{i} x 9 = {i*9}")
    print()

 # 5.15
def p5_15():
    n = int(input("5.15: Введите n (1..9) для таблицы умножения: "))
    print(f"Таблица умножения на {n}")
    for i in range(1, 10):
        print(f"{i} x {n} = {i*n}")
    print()

 # 5.16
def p5_16():
    print("5.16: sin(2), sin(3), ..., sin(15) (в радианах)")
    for x in range(2, 16):
        print(f"sin({x}) = {math.sin(x):.6f}")
    print()

 # 5.17
def p5_17():
    print("5.17: y = 3 t^2 + 4.87 t - 3, t = x+3")
    for x in range(4, 29):
        t = x + 3
        y = 3 * t**2 + 4.87 * t - 3
        print(f"x={x:2d}, t={t:2d} -> y={y:.6f}")
    print()

 # 5.18
def p5_18():
    print("5.18: z = 4.3 t^2 - 8 t + 13, t = 3a")
    for a in range(2, 18):
        t = 3 * a
        z = 4.3 * t**2 - 8 * t + 13
        print(f"a={a:2d}, t={t:2d} -> z={z:.6f}")
    print()

 # 5.19
def p5_19():
    print("5.19: sin(0.1), sin(0.2), ..., sin(1.5)")
    val = 0.1
    while val <= 1.5 + 1e-12:
        print(f"sin({val:.1f}) = {math.sin(val):.6f}")
        val += 0.1
        val = round(val, 10)
    print()

 # 5.20
def p5_20():
    print("5.20: sqrt(0.1), sqrt(0.2), ..., sqrt(0.9)")
    for k in range(1, 10):
        v = k / 10.0
        print(f"sqrt({v:.1f}) = {math.sqrt(v):.6f}")
    print()

 # 5.21
def p5_21():
    price = float(input("5.21: Введите цену 1 кг сыра (руб.): "))
    print("Вес (г) | Стоимость (руб.)")
    for g in range(50, 1001, 50):
        cost = price * g / 1000.0
        print(f"{g:6d}   | {cost:12.2f}")
    print()

 # 5.22
def p5_22():
    price = float(input("5.22: Введите цену 1 кг конфет (руб.): "))
    print("Вес (г) | Стоимость (руб.)")
    for g in range(100, 2001, 100):
        cost = price * g / 1000.0
        print(f"{g:6d}   | {cost:12.2f}")
    print()

 # 5.23
for i in range(21, 29):
    print(i / 10)

 # 5.24
for i in range(32, 40):
    for _ in range(2):
        print(i / 10)

 # 5.25
for i in range(22, 43, 2):
    print(i / 10)

 # 5.26
for i in range(44, 65, 2):
    print(i / 10)

 # 5.27
 # a)
s_a = sum(range(200, 601))
print("5.27 a)", s_a)

 # b)
a = int(input("Введите a (a < 400) для 5.27 b): "))
if a < 400:
    s_b = sum(range(a, 401))
    print("5.27 b)", s_b)
else:
    print("Ошибка: a должно быть < 400")

 # c)
b = int(input("Введите b (b > -15) для 5.27 c): "))
if b > -15:
    s_c = sum(range(-15, b + 1))
    print("5.27 c)", s_c)
else:
    print("Ошибка: b должно быть > -15")

 # d)
a = int(input("Введите a для 5.27 d): "))
b = int(input("Введите b для 5.27 d) (b > a): "))
if b > a:
    s_d = sum(range(a, b + 1))
    print("5.27 d)", s_d)
else:
    print("Ошибка: b должно быть > a")

 # 5.28
import math

 # a)
prod_a = 1
for x in range(7, 15):
    prod_a *= x
print("5.28 a)", prod_a)

 # b)
a = int(input("Введите a (1 <= a <= 15) для 5.28 b): "))
if 1 <= a <= 15:
    prod_b = 1
    for x in range(a, 16):
        prod_b *= x
    print("5.28 b)", prod_b)
else:
    print("Ошибка: неверный a")

 # c)
b = int(input("Введите b (1 <= b <= 10) для 5.28 c): "))
if 1 <= b <= 10:
    prod_c = 1
    for x in range(1, b + 1):
        prod_c *= x
    print("5.28 c)", prod_c)
else:
    print("Ошибка: неверный b")

 # d)
a = int(input("Введите a для 5.28 d): "))
b = int(input("Введите b для 5.28 d) (b > a): "))
if b > a:
    prod_d = 1
    for x in range(a, b + 1):
        prod_d *= x
    print("5.28 d)", prod_d)
else:
    print("Ошибка: b должно быть > a")

 # 5.29
 # a)
s = sum(range(1, 751))
n = 750
print("5.29 a)", s / n)

 # b)
b = int(input("Введите b (b >= 150) для 5.29 b): "))
if b >= 150:
    s = sum(range(150, b + 1))
    n = b - 150 + 1
    print("5.29 b)", s / n)
else:
    print("Ошибка: b должно быть >= 150")

 # c)
a = int(input("Введите a (a <= 200) для 5.29 c): "))
if a <= 200:
    s = sum(range(a, 201))
    n = 200 - a + 1
    print("5.29 c)", s / n)
else:
    print("Ошибка: a должно быть <= 200")

 # d)
a = int(input("Введите a для 5.29 d): "))
b = int(input("Введите b для 5.29 d) (b >= a): "))
if b >= a:
    s = sum(range(a, b + 1))
    n = b - a + 1
    print("5.29 d)", s / n)
else:
    print("Ошибка: b должно быть >= a")

 # 5.30
 # a)
sum_cubes = sum(i**3 for i in range(25, 41))
print("5.30 a)", sum_cubes)

 # b)
a = int(input("Введите a (0 <= a <= 50) для 5.30 b): "))
if 0 <= a <= 50:
    sum_sq_b = sum(i**2 for i in range(a, 51))
    print("5.30 b)", sum_sq_b)
else:
    print("Ошибка: a вне диапазона")

 # c)
n = int(input("Введите n (1 <= n <= 100) для 5.30 c): "))
if 1 <= n <= 100:
    sum_sq_c = sum(i**2 for i in range(1, n + 1))
    print("5.30 c)", sum_sq_c)
else:
    print("Ошибка: n вне диапазона")

 # d)
a = int(input("Введите a для 5.30 d): "))
b = int(input("Введите b для 5.30 d) (b > a): "))
if b > a:
    sum_sq_d = sum(i**2 for i in range(a, b + 1))
    print("5.30 d)", sum_sq_d)
else:
    print("Ошибка: b должно быть > a")

 # 5.31
def sum_5_31(n):
    s = 0
    for k in range(n, 2*n + 1):
        s += k * k
    return s

 # 5.32
def sum_5_32(n):
    s = 0.0
    for k in range(1, n+1):
        s += 1.0 / k
    return s

 # 5.33
def sum_5_33():
    s = 0.0
    for num in range(2, 11):
        s += num / (num + 1)
    return s

 # 5.34
def sum_5_34(n):
    s = 0
    for k in range(1, n+1):
        s += k * k
    return s

 # 5.35
def sum_5_35(n):
    s = 0
    for k in range(1, n):
        s += k * (k + 1)
    return s

 # 5.36
def sum_5_36(n):
    s = 0.0
    for k in range(1, n+1):
        denom = 2*k - 1
        s += 1.0 / (denom * denom)
    return s

 # 5.37
def sum_5_37(n):
    s = 0.0
    sign = 1.0
    for k in range(1, n+1):
        s += sign * (1.0 / k)
        sign *= -1.0
    return s

 # 5.38
def sum_5_38(x):
    s = 0.0
    power = x
    for exp in range(1, 12, 2):
        if exp != 1:
            pass
        s += power / exp
        power = power * x * x
    return s

 # 5.39
def sum_5_39():
    s = 0.0
    sign = 1.0
    for k in range(1, 12):
        s += sign * (k / (k + 1))
        sign *= -1.0
    return s

 # 5.40
def sum_digits_5_40(number):
    n = abs(int(number))
    s = 0
    count = 0
    while n > 0 and count < 9:
        s += n % 10
        n //= 10
        count += 1
    return s

 # 5.41
def last_n_digits_sum_prod_5_41(number, n):
    if n <= 0:
        return 0, 1
    m = abs(int(number))
    s = 0
    prod = 1
    for i in range(n):
        d = m % 10
        s += d
        prod *= d
        m //= 10
    return s, prod

 # 5.42
def strange_husband(N):
    pos = sum((1.0 / k) * (1 if (k % 2 == 1) else -1) for k in range(1, N+1))
    total = sum(1.0 / k for k in range(1, N+1))
    return pos, total

 # 5.43
def iterate_babylonian(a0, n):
    a = a0
    seq = [a]
    for k in range(1, n+1):
        a = 0.5 * (a + 1.0 / a)
        seq.append(a)
    return seq

def fib_list(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def fib_n(n):
    if n <= 0:
        raise ValueError("n must be positive")
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a + b
    return b



















































