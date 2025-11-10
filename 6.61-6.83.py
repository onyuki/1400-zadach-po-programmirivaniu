# Общие вспомогательные функции
def digits_list(n):

    return [int(ch) for ch in str(n)]

def digits_list_rev(n):
    return [int(ch) for ch in str(n)[::-1]]

 # 6.61
def two_max_min_positions(n):
    s = str(n)
    digits = [int(ch) for ch in s]
    pairs = [(d, i+1) for i, d in enumerate(digits)]
    sorted_desc = sorted(pairs, key=lambda x: x[0], reverse=True)
    sorted_asc = sorted(pairs, key=lambda x: x[0])
    max1, max2 = sorted_desc[0], sorted_desc[1]
    min1, min2 = sorted_asc[0], sorted_asc[1]
    length = len(digits)
    def from_end(pos_from_start):
        return length - pos_from_start + 1
    res = {
        'max': {
            'from_start': (max1[1], max2[1]),
            'from_end': (from_end(max1[1]), from_end(max2[1]))
        },
        'min': {
            'from_start': (min1[1], min2[1]),
            'from_end': (from_end(min1[1]), from_end(min2[1]))
        }
    }
    return res

 # 6.62
def reverse_number(n):
    return int(str(n)[::-1])

def surround_with_two(n):
    return int('2' + str(n) + '2')

def remove_digit(n, a):
    s = str(n).replace(str(a), '')
    return int(s) if s != '' else 0

def swap_first_last(n):
    s = str(n)
    if len(s) == 1:
        return n
    s2 = s[-1] + s[1:-1] + s[0]
    return int(s2)

def append_self(n):
    return int(str(n) + str(n))

 # 6.63
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

 # 6.64
def minimal_banknotes(n):
    denominations = [64, 32, 16, 8, 4, 2, 1]
    counts = []
    remaining = n
    total_count = 0
    for d in denominations:
        c = remaining // d
        counts.append((d, c))
        total_count += c
        remaining -= c * d
    return counts, total_count

 # 6.65
def gcd(a, b):
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a

import math

 # 6.66
def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)

 # 6.67
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // math.gcd(a, b) * b)

 # 6.68
def reduce_fraction(a, b):
    if b == 0:
        raise ValueError("Знаменатель не должен быть 0")
    g = math.gcd(a, b)
    return (a // g, b // g)

 # 6.69
def rectangle_to_squares(w, h):
    res = []
    W, H = w, h
    while W > 0 and H > 0:
        side = min(W, H)
        if W >= H:
            count = W // H
            res.append((H, count))
            W = W % H
        else:
            count = H // W
            res.append((W, count))
            H = H % W
    return res

 # 6.70: Общ случ — исп ту же функw rectangle_to_squares(w,h)

 # 6.71
def fib_index(n):
    if n <= 0:
        return -1
    if n == 1:
        return 1
    a, b = 1, 1
    idx = 2
    while b < n:
        a, b = b, a + b
        idx += 1
    return idx if b == n else -1

 # 6.72
def in_arithmetic_progression(x, a, d):
    if d == 0:
        return x == a
    if (x - a) % d != 0:
        return False
    k = (x - a) // d
    return k >= 0

 # 6.73
def in_geometric_progression(x, g, q):
    if g == x:
        return 0
    if g == 0:
        return x == 0
    if q == 1:
        return x == g
    if q == 0:
        return x == g or x == 0
    k = 0
    val = g
    while True:
        k += 1
        val *= q
        if val == x:
            return True
        if abs(q) > 1 and abs(val) > abs(x):
            return False
        if q == -1:
            return False
        if k > 1000:
            return False

 # 6.74
def is_power(n, base):
    if n <= 0:
        return False, -1
    power = 0
    val = 1
    while val < n:
        val *= base
        power += 1
    if val == n:
        return True, power
    return False, -1

 # 6.75
def bisection(f, a, b, tol=1e-3, max_iter=1000):
    fa = f(a)
    fb = f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError("f(a) и f(b) должны иметь разные знаки")
    left, right = a, b

    for i in range(max_iter):
        mid = 0.5 * (left + right)
        fm = f(mid)
        if abs(right - left) <= tol:
            return mid
        if fm == 0:
            return mid
        if fa * fm < 0:
            right = mid
            fb = fm
        else:
            left = mid
            fa = fm
    return 0.5 * (left + right)

def digits_of(n):
    return list(map(int, str(n)))

# Общ пров послед:
def is_strictly_increasing(seq):
    return all(seq[i] > seq[i-1] for i in range(1, len(seq)))

def is_nondecreasing(seq):
    return all(seq[i] >= seq[i-1] for i in range(1, len(seq)))

def is_strictly_decreasing(seq):
    return all(seq[i] < seq[i-1] for i in range(1, len(seq)))

def is_nonincreasing(seq):
    return all(seq[i] <= seq[i-1] for i in range(1, len(seq)))

 # 6.77
def all_digits_equal(n):
    d = digits_of(n)
    return all(x == d[0] for x in d)

def has_adjacent_equal_digits(n):
    d = digits_of(n)
    return any(d[i] == d[i+1] for i in range(len(d)-1))

 # 6.78
def right_to_left_strictly_increasing(n):
    d = digits_of(n)[::-1]
    return is_strictly_increasing(d)

 # 6.79
def right_to_left_nondecreasing(n):
    d = digits_of(n)[::-1]
    return is_nondecreasing(d)

 # 6.80
def left_to_right_strictly_increasing(n):
    d = digits_of(n)
    return is_strictly_increasing(d)

 # 6.81
def left_to_right_monotone_increasing_strict(n):
    return left_to_right_strictly_increasing(n)

 # 6.82
def left_to_right_nondecreasing(n):
    d = digits_of(n)
    return is_nondecreasing(d)

 # 6.83
def left_to_right_strictly_monotone(n):
    d = digits_of(n)
    return is_strictly_increasing(d) or is_strictly_decreasing(d)

 # Вспом функц для печат рез по всем задач:
def analyze_number(n):
    return {
        'n': n,
        'all_digits_equal': all_digits_equal(n),
        'has_adjacent_equal_digits': has_adjacent_equal_digits(n),
        'right_to_left_strictly_increasing': right_to_left_strictly_increasing(n),
        'right_to_left_nondecreasing': right_to_left_nondecreasing(n),
        'left_to_right_strictly_increasing': left_to_right_strictly_increasing(n),
        'left_to_right_monotone_increasing_strict': left_to_right_monotone_increasing_strict(n),
        'left_to_right_nondecreasing': left_to_right_nondecreasing(n),
        'left_to_right_strictly_monotone': left_to_right_strictly_monotone(n),
    }






































