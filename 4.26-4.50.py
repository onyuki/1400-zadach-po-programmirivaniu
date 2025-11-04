#import math - для всех мат. функций!

# 4.26
def task_4_26(n):
    n_abs = abs(n)
    a = n_abs // 10
    b = n_abs % 10
    if a > b:
        which = "first"
    elif a < b:
        which = "second"
    else:
        which = "equal"
    equal = (a == b)
    return a, b, which, equal

# 4.27
def task_4_27(n):
    n_abs = abs(n)
    a = n_abs // 10
    b = n_abs % 10
    return n * n == a*a + b*b

# 4.30
def is_three_digit_palindrome(n):
    n_abs = abs(n)
    if n_abs < 100 or n_abs > 999:
        raise ValueError("Ожидается трёхзначное число")
    return (n_abs // 100) == (n_abs % 10)

# 4.31
def task_4_31(n):
    n_abs = abs(n)
    a = n_abs // 100
    b = (n_abs // 10) % 10
    c = n_abs % 10
    return {
        'first_vs_last': 'first' if a > c else ('last' if a < c else 'equal'),
        'first_vs_second': 'first' if a > b else ('second' if a < b else 'equal'),
        'second_vs_last': 'second' if b > c else ('last' if b < c else 'equal'),
        'digits': (a, b, c)
    }

# 4.32
def task_4_32(n):
    n_abs = abs(n)
    a = n_abs // 100
    b = (n_abs // 10) % 10
    c = n_abs % 10
    return n * n == a*a + b*b + c*c


def digits3(n):
    n = abs(n)
    if not (100 <= n <= 999):
        raise ValueError("Число не трёхзначное")
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    return a, b, c

def digits4(n):
    n = abs(n)
    if not (1000 <= n <= 9999):
        raise ValueError("Число не четырёхзначное")
    a = n // 1000
    b = (n // 100) % 10
    c = (n // 10) % 10
    d = n % 10
    return a, b, c, d

 # 4.33
def task_4_33(n, a_param):
    a1, b1, c1 = digits3(n)
    s = a1 + b1 + c1
    p = a1 * b1 * c1

    results = {}

    results['sum_is_two_digit'] = 10 <= s <= 99
    # б) является ли произведение его цифр трёхзначным числом
    results['prod_is_three_digit'] = 100 <= p <= 999
    # в) больше ли числа a произведение его цифр
    results['number_gt_product'] = n > p
    # г) кратна ли пяти сумма его цифр
    results['sum_div_by_5'] = (s % 5 == 0)
    # д) кратна ли сумма его цифр числу a_param (если a_param == 0 — неопределено)
    if a_param == 0:
        results['sum_div_by_a'] = None  # нельзя делить на ноль
    else:
        results['sum_div_by_a'] = (s % a_param == 0)

    results['sum'] = s
    results['prod'] = p
    return results

 # 4.34
def task_4_34(n):
    a1, b1, c1 = digits3(n)
    results = {}
    # а) все ли цифры одинаковые
    results['all_equal'] = (a1 == b1 == c1)
    # б) есть ли среди цифр одинаковые (хотя бы пара)
    results['any_equal'] = (a1 == b1) or (a1 == c1) or (b1 == c1)
    return results

 # 4.35
def task_4_35(n):
    a1, b1, c1, d1 = digits4(n)
    s = a1 + b1 + c1 + d1
    p = a1 * b1 * c1 * d1
    results = {}
    # а) равна ли сумма двух первых цифр сумме двух последних
    results['first2_eq_last2'] = (a1 + b1 == c1 + d1)
    # б) кратна ли трем сумма его цифр
    results['sum_div_by_3'] = (s % 3 == 0)
    # в) кратно ли четырём произведение его цифр
    results['prod_div_by_4'] = (p % 4 == 0)
    results['sum'] = s
    results['prod'] = p
    return results

# 4.36
def ends_even(n: int) -> bool:
    return (abs(n) % 10) % 2 == 0

def ends_odd(n: int) -> bool:
    return (abs(n) % 10) % 2 == 1

# 4.37
def is_divisor(a: int, b: int) -> (bool, bool):
    a_div_b = (a != 0) and (b % a == 0)
    b_div_a = (b != 0) and (a % b == 0)
    return a_div_b, b_div_a

# 4.38
def max_count_orientation(a: int, b: int, c: int, d: int) -> dict:

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        raise ValueError("Все размеры должны быть положительными целыми числами.")

    count_long_on_long = (a // d) * (b // c)

    count_long_on_short = (a // c) * (b // d)
    if count_long_on_long > count_long_on_short:
        winner = "long_on_long"
    elif count_long_on_short > count_long_on_long:
        winner = "long_on_short"
    else:
        winner = "equal"
    return {
        "long_on_long": count_long_on_long,
        "long_on_short": count_long_on_short,
        "winner": winner
    }

# 4.39
def traffic_light(t: float) -> str:

    if not isinstance(t, (int, float)):
        raise ValueError("t должен быть числом.")
    t_mod = t % 5.0

    return "green" if t_mod < 3.0 else "red"

# 4.40
def in_interval_minus5_3(x: float) -> bool:

    return (-5.0 < x) and (x < 3.0)

# 4.41
def is_two_digit(n: int) -> bool:

    return 10 <= abs(n) <= 99

# 4.42

def point_in_region_a(x: float, y: float) -> bool:

    return (0.0 <= x <= 2.0) and (0.0 <= y <= 2.0)

def point_in_region_b(x: float, y: float) -> bool:

    return (-2.0 <= x <= 0.0) and (-4.0 <= y <= 0.0)

import math

# 4.43
def in_region_I_4_43(x, y):
    return (x > 3) and (0 < y < 2)

 # 4.44
def which_region_4_44(x, y):
    if x > 5:
        return "I"
    elif x < -1:
        return "III"
    else:
        return "neither I nor III"

 # 4.45
def f_4_45(x):
    return x**2 if -2.4 <= x <= 5.7 else 4

 # 4.46
def f_4_46(x):
    return math.sin(x) if 0.2 <= x <= 0.9 else 1

import math
import cmath
from typing import Tuple, List, Union


 # 4.47
def check_chain_ascending(a: float, b: float, c: float) -> bool:
    return a < b < c

def check_chain_b_gt_a_gt_c(a: float, b: float, c: float) -> bool:
    return b > a > c

 # 4.48
def is_one_divisor_of_other(x: int, y: int) -> bool:

    if x == 0 and y == 0:

        return False
    if x == 0:
        return False if y != 0 else False
    if y == 0:
        return False
    return (y % x == 0) or (x % y == 0)

def digits_of(n: int) -> List[int]:
    n = abs(n)
    if n == 0:
        return [0]
    digs = []
    while n > 0:
        digs.append(n % 10)
        n //= 10
    return digs[::-1]


 # 4.49
def two_digit_contains(n: int, digit: int) -> bool:

    if not 10 <= abs(n) <= 99:
        raise ValueError("n должно быть двухзначным по модулю")
    if not (0 <= digit <= 9):
        raise ValueError("digit должен быть в 0..9")
    return digit in digits_of(n)

 # 4.50
def two_digit_contains_any_of(n: int, digits_set: List[int]) -> bool:
    if not 10 <= abs(n) <= 99:
        raise ValueError("n должно быть двухзначным по модулю")
    return any(d in digits_of(n) for d in digits_set)


















