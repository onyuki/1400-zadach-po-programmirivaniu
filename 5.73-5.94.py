 # 5.73
import math

L = 4.5
x = 3.0
step = 0.2
eps = 1e-9

while x <= L + eps:
    cosv = x / L
    cosv = max(-1.0, min(1.0, cosv))
    theta_deg = math.degrees(math.acos(cosv))
    print(f"x = {x:.1f} m -> θ = {theta_deg:.2f}°")
    x += step

 # 5.74
 # Вариант 1
def odd_10_100_if():
    for i in range(10, 101):
        if i % 2 != 0:
            print(i, end=' ')
    print()

 # Вариант 2
def odd_10_100_no_if():
    start = 11 if 11 <= 100 else None
    if start:
        for i in range(start, 101, 2):
            print(i, end=' ')
    print()

 # 5.75
def mult_5_100_200():
    for i in range(100, 201):
        if i % 5 == 0:
            print(i, end=' ')
    print()

 # 5.76
def multiples_in_range(a, b, c):
    if a > b:
        a, b = b, a
    start = ((a + c - 1) // c) * c
    for x in range(start, b+1, c):
        print(x, end=' ')
    print()

 # 5.77
def odd_two_digit_last_div_by_3_or_7():
    for n in range(10, 100):
        last = n % 10
        if n % 2 != 0 and (last % 3 == 0 or last % 7 == 0):
            print(n, end=' ')
    print()

 # 5.78
def find_3digit_mod47_43_mod45_15():
    res = []
    for n in range(100, 1000):
        if n % 47 == 43 and n % 45 == 15:
            res.append(n)
    print(res)

 # 5.79
def find_4digit_mod133_125_mod111_113():
    res = []
    for n in range(1000, 10000):
        if n % 133 == 125 and n % 111 == 113:
            res.append(n)
    print(res)

 # 5.80
def two_digit_divisible_or_contains(n):
    if not (0 <= n <= 9):
        raise ValueError("n должен быть цифрой 0..9")
    res = []
    for x in range(10, 100):
        if x % n == 0 if n != 0 else False:
            res.append(x)
        else:
            if str(n) in str(x):
                res.append(x)
    print(res)

 # 5.81
 # часть (a)
automorphic = [n for n in range(100, 1000) if (n * n) % 1000 == n]
print("a) автоморфные 3-значные числа:", automorphic)

 # часть (b)
b_numbers = [n for n in range(100, 1000) if n % 7 == 0 and sum(map(int, str(n))) % 7 == 0]
print("b) 3-значные числа, кратные 7 и с суммой цифр, кратной 7:", b_numbers)
print("Всего таких чисел:", len(b_numbers))

 # 5.82
def two_digit_sum_squares_div13():
    res = []
    for n in range(10, 100):
        s2 = sum(int(d)**2 for d in str(n))
        if s2 % 13 == 0:
            res.append(n)
    print(res)

def three_digit_n_equals_S_plus_S_squared():
    res = []
    for n in range(100, 1000):
        S = sum(int(d) for d in str(n))
        if n == S + S*S:
            res.append(n)
    print(res)

 # 5.83
s_583 = sum(range(1, 50, 2))

 # 5.84
s_584 = sum(range(100, 1000, 2))

 # 5.85
def sum_multiples_of_4(a, b):

    a = max(a, 1)
    if a > b:
        return 0
    first = ((a + 3) // 4) * 4
    last = (b // 4) * 4
    if first > last:
        return 0
    n = (last - first) // 4 + 1
    return n * (first + last) // 2

  # 5.86
s_586 = sum(x for x in range(31, 100) if x % 3 == 0 and x % 10 in (2, 4, 8))

import math

 # 5.87
def count_sum_digits_in_range(a, b, target):
    def sum_digits(x):
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s
    cnt = 0
    for x in range(a, b + 1):
        if sum_digits(x) == target:
            cnt += 1
    return cnt

 # 5.88
def count_three_digit_with_sum(s):
    if s <= 0 or s >= 27:
        return 0
    cnt = 0
    for x in range(100, 1000):
        if (x // 100) + ((x // 10) % 10) + (x % 10) == s:
            cnt += 1
    return cnt

 # 5.89
def count_three_digit_mult7_and_digit_sum_mult7():
    cnt = 0
    for x in range(100, 1000):
        if x % 7 == 0:
            s = (x // 100) + ((x // 10) % 10) + (x % 10)
            if s % 7 == 0:
                cnt += 1
    return cnt

print("5.89:", count_three_digit_mult7_and_digit_sum_mult7())

 # 5.90
def is_fib_sum_even(n):

    return (n + 2) % 3 != 0

 # 5.91
def get_divisors(n):

    if n <= 0:
        return []
    divs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            j = n // i
            if j != i:
                divs.append(j)
    return sorted(divs)

def sum_divisors(n):
    return sum(get_divisors(n))

def sum_even_divisors(n):
    return sum(d for d in get_divisors(n) if d % 2 == 0)

def count_divisors(n):
    return len(get_divisors(n))

def count_odd_divisors(n):
    return sum(1 for d in get_divisors(n) if d % 2 == 1)

def count_divisors_greater_than(n, d):
    return sum(1 for x in get_divisors(n) if x > d)

def count_divisors_greater_than_and_even(n, d):
    return sum(1 for x in get_divisors(n) if x > d and x % 2 == 0)

 # 5.92
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    i = 3
    while i <= r:
        if n % i == 0:
            return False
        i += 2
    return True

 # 5.93
def is_perfect(n):
    if n <= 1:
        return False
    s = 1
    r = int(math.sqrt(n))
    for i in range(2, r + 1):
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
    return s == n

 # 5.94
def numbers_whose_square_leq(N):
    if N < 1:
        return []
    max_k = int(math.isqrt(N))
    return list(range(1, max_k + 1))







































