#2.37
f = float(input("Введите температуру в градусах Фаренгейта (например, 450): "))
c = (f - 32) * 5.0 / 9.0
print(f"{f} °F = {c} °C")

#2.38
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

print(f"{a}+{b}={a + b}")
print(f"{a}-{b}={a - b}")
print(f"{a}*{b}={a * b}")

if b != 0:
    print(f"{a}/{b}={a / b}")
else:
    print(f"{a}/{b}=деление на ноль невозможно")

avg = (a + b) / 2
print(f"({a}+{b})/2={avg}")

#3.1
def full_meters(cm: int) -> int:
    return cm // 100

#3.2
def full_centners(kg: int) -> int:
    return kg // 100

#3.3
def full_weeks(days: int) -> int:
    return days // 7

#3.4
def divide_apples(n: int, k: int):
    per = k // n
    rem = k % n
    return per, rem

#3.5
a, b, s = 543, 130, 130
num_squares = (a // s) * (b // s)
print(num_squares)

#3.6
def compartment_number(seat: int, seats_per_compartment: int = 4) -> int:
    return (seat - 1) // seats_per_compartment + 1

#3.7
def floor_by_flat(flat: int, floors: int = 5, total_flats: int = 15) -> int:
    flats_per_floor = total_flats // floors
    return (flat - 1) // flats_per_floor + 1

#3.8
def row_by_ticket(ticket: int, seats_per_row: int = 15) -> int:
    return (ticket - 1) // seats_per_row + 1

#3.9
def time_breakdown(s: int):
    minutes = s // 60
    hours = s // 3600
    minutes_in_hour = (s % 3600) // 60
    seconds_in_minute = s % 60
    return minutes, hours, minutes_in_hour, seconds_in_minute

# 3.10
def weekday_number(k, d):
    return (d + k - 1) % 7

if __name__ == "__main__":
    k = int(input("k (1..365): "))
    d = int(input("d (1..7, 1=пн,..,7=вс): "))
    n = weekday_number(k, d)
    print("n =", n)

# 3.11
def month_number(n):
    return (n % 12) + 1

if __name__ == "__main__":
    n = int(input("n (количество прошедших месяцев): "))
    x = month_number(n)
    print("x =", x)

# 3.12
def floor_and_pos_3_12(N):
    per_floor = 4
    floor = (N - 1) // per_floor + 1
    pos = (N - 1) % per_floor + 1
    return floor, pos

if __name__ == "__main__":
    N = int(input("Номер квартиры (1..20): "))
    floor, pos = floor_and_pos_3_12(N)
    print("Этаж:", floor)
    print("Позиция на этаже:", pos)

# 3.13
def row_col_3_13(n):
    cols = 5
    row = (n - 1) // cols + 1
    col = (n - 1) % cols + 1
    return row, col

if __name__ == "__main__":
    n = int(input("n (1..50): "))
    r, c = row_col_3_13(n)
    print("Строка:", r)
    print("Столбец:", c)

# 3.14
def locate_apartment_3_14(N):
    floors = 9
    per_floor = 6
    per_entrance = floors * per_floor
    entrance = (N - 1) // per_entrance + 1
    offset = (N - 1) % per_entrance
    floor = offset // per_floor + 1
    pos = offset % per_floor + 1
    return entrance, floor, pos

if __name__ == "__main__":
    N = int(input("Номер квартиры (1..216): "))
    entrance, floor, pos = locate_apartment_3_14(N)
    print("Подъезд:", entrance)
    print("Этаж внутри подъезда:", floor)
    print("Позиция на этаже:", pos)

#3.15

def variantA(n):

#Вариант A (рис.3.1):

    if not (1 <= n <= 1200):
        raise ValueError("Номер места должен быть в диапазоне 1..1200")
    per_tier = 8 * 15
    tier = (n - 1) // per_tier + 1
    pos_in_tier = (n - 1) % per_tier + 1
    section = (pos_in_tier - 1) // 15 + 1
    place_in_section_tier = (pos_in_tier - 1) % 15 + 1
    return section, tier, place_in_section_tier

def variantB(n):

#Вариант B (рис.3.2):

    if not (1 <= n <= 1200):
        raise ValueError("Номер места должен быть в диапазоне 1..1200")
    per_section = 10 * 15
    section = (n - 1) // per_section + 1
    within_section = (n - 1) % per_section
    place_in_tier = within_section // 10 + 1
    tier = within_section % 10 + 1
    return section, tier, place_in_tier

# 3.16
def digits_two(n):
    n_abs = abs(n)
    if not (10 <= n_abs <= 99):
        raise ValueError("Число должно быть двухзначным")
    tens = n_abs // 10
    ones = n_abs % 10
    return tens, ones

# 3.17
def sum_digits_two(n):
    t, o = digits_two(n)
    return t + o

# 3.18
def swapped_two(n):
    sign = -1 if n < 0 else 1
    t, o = digits_two(n)
    return sign * (o * 10 + t)

# 3.19
def digits_three(n):
    n_abs = abs(n)
    if not (100 <= n_abs <= 999):
        raise ValueError("Число должно быть трёхзначным")
    a = n_abs // 100
    b = (n_abs // 10) % 10
    c = n_abs % 10
    if n < 0:
        return -a, -b, -c
    return a, b, c

def digits_of(n):
    return [int(d) for d in str(n)]

def sum_digits(n):
    return sum(digits_of(n))

def prod_digits(n):
    p = 1
    for d in digits_of(n):
        p *= d
    return p

# 3.20
def task_3_20(n):
    assert 100 <= abs(n) <= 999
    n = abs(n)
    units = n % 10
    tens = (n // 10) % 10
    hundreds = n // 100
    s = units + tens + hundreds
    p = units * tens * hundreds
    return {'units': units, 'tens': tens, 'sum': s, 'product': p}

# 3.21
def task_3_21(n):
    assert 100 <= abs(n) <= 999
    n = abs(n)
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    return c * 100 + b * 10 + a

# 3.22
def task_3_22(n):
    assert 100 <= abs(n) <= 999
    n = abs(n)
    return (n % 100) * 10 + (n // 100)

# 3.23
def task_3_23(n):
    assert 100 <= abs(n) <= 999
    n = abs(n)
    return (n % 10) * 100 + (n // 10)

# 3.24
def task_3_24(n):
    assert 100 <= abs(n) <= 999
    n = abs(n)
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    return b * 100 + a * 10 + c

# 3.25
def task_3_25(n):
    assert 100 <= abs(n) <= 999
    n = abs(n)
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    return a * 100 + c * 10 + b

# 3.26
import itertools
def task_3_26(n):
    s = str(abs(n))
    assert len(s) == 3 and len(set(s)) == 3
    perms = sorted(int(''.join(p)) for p in set(itertools.permutations(s, 3)))
    return perms

# 3.27
def task_3_27_a(n):
    assert 1000 <= abs(n) <= 9999
    return sum_digits(abs(n))

def task_3_27_b(n):
    assert 10000 <= abs(n) <= 99999
    return sum_digits(abs(n))

# 3.28
def task_3_28_a(n):
    #a)
    assert 1000 <= abs(n) <= 9999
    s = str(abs(n))
    return int(s[::-1])

def task_3_28_b(n):
    #б)
    assert 1000 <= abs(n) <= 9999
    s = str(abs(n))
    a,b,c,d = s
    return int(b + a + d + c)

def task_3_28_c(n):
    #в)
    assert 1000 <= abs(n) <= 9999
    s = str(abs(n))
    a,b,c,d = s
    return int(a + c + b + d)

def task_3_28_d_method1(n):
    #г)
    assert 1000 <= abs(n) <= 9999
    n = abs(n)
    a = n // 1000
    b = (n // 100) % 10
    c = (n // 10) % 10
    d = n % 10
    return c * 1000 + d * 100 + a * 10 + b

def task_3_28_d_method2(n):
    #г)
    assert 1000 <= abs(n) <= 9999
    s = str(abs(n))
    return int(s[2:] + s[:2])

# 3.29
def task_3_29(n):
    assert n > 9
    units = n % 10
    tens = (n // 10) % 10
    return {'units': units, 'tens': tens}


# 3.32
def reconstruct_from_rotated_right(n):
    c = n // 100
    a = (n // 10) % 10
    b = n % 10
    return 100*a + 10*b + c

# 3.33
def reconstruct_from_shift_left(n):
    b = n // 100
    c = (n // 10) % 10
    a = n % 10
    return 100*a + 10*b + c

# 3.36
def reconstruct_second_to_left(n):
    b = n // 100
    a = (n // 10) % 10
    c = n % 10
    return 100*a + 10*b + c

# 3.37
def reconstruct_second_to_right(n):
    a = n // 100
    c = (n // 10) % 10
    b = n % 10
    return 100*a + 10*b + c
















