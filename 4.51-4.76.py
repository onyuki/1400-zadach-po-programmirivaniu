#библиотеки для всех ниже прорешенных задач:
import math
import cmath
from typing import Tuple, List, Union

 # 4.51
def three_digit_contains(n: int, digit: int) -> bool:

    if not 100 <= abs(n) <= 999:
        raise ValueError("n должно быть трехзначным по модулю")
    if not (0 <= digit <= 9):
        raise ValueError("digit должен быть 0..9")
    return digit in digits_of(n)

def three_digit_contains_any_of(n: int, digits_set: List[int]) -> bool:
    if not 100 <= abs(n) <= 999:
        raise ValueError("n должно быть трехзначным по модулю")
    return any(d in digits_of(n) for d in digits_set)

 # 4.54, 4.55
def four_digit_contains(n: int, digit: int) -> bool:
    if not 1000 <= abs(n) <= 9999:
        raise ValueError("n должно быть четырехзначным по модулю")
    if not (0 <= digit <= 9):
        raise ValueError("digit должен быть 0..9")
    return digit in digits_of(n)

def four_digit_contains_any_of(n: int, digits_set: List[int]) -> bool:
    if not 1000 <= abs(n) <= 9999:
        raise ValueError("n должно быть четырехзначным по модулю")
    return any(d in digits_of(n) for d in digits_set)


 # 4.56
def is_four_digit_palindrome(n: int) -> bool:
    if not 1000 <= n <= 9999:
        raise ValueError("n должно быть натуральным четырехзначным числом")
    s = str(n)
    return s == s[::-1]


 # 4.57
def remainder_equals_one_of(a: int, b: int, c: int, d: int) -> bool:
    if a < 0:
        raise ValueError("a должно быть неотрицательным")
    if b <= 0:
        raise ValueError("b должно быть положительным")
    r = a % b
    return r == c or r == d

 # 4.58
def has_equal_pair(a: float, b: float, c: float) -> bool:
    return (a == b) or (a == c) or (b == c)

 # 4.59
def triangle_properties(a: float, b: float, c: float) -> Tuple[bool, bool]:

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны должны быть положительными")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("С указанными длинами невозможно построить треугольник")
    is_equilateral = (a == b == c)
    is_isosceles = (a == b) or (a == c) or (b == c)
    return is_equilateral, is_isosceles


 # 4.60
def heights_equalities(h1: float, h2: float, h3: float) -> Tuple[bool, bool]:

    all_equal = (h1 == h2 == h3)
    any_two_equal = (h1 == h2) or (h1 == h3) or (h2 == h3)
    return all_equal, any_two_equal


 # 4.61
def solve_quadratic(a: float, b: float, c: float) -> Union[str, Tuple]:

    if a == 0:
        raise ValueError("a не должен равняться 0")
    D = b * b - 4 * a * c
    if D > 0:
        sqrtD = math.sqrt(D)
        x1 = (-b - sqrtD) / (2 * a)
        x2 = (-b + sqrtD) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        return ("two_real", x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return ("one_real", x)
    else:
        sqrtD = cmath.sqrt(D)
        z1 = (-b - sqrtD) / (2 * a)
        z2 = (-b + sqrtD) / (2 * a)
        return ("two_complex", z1, z2)

 # 4.62
def fits_rectangle(a, b, c, d):

    return (a <= c and b <= d) or (a <= d and b <= c)

 # 4.63
def fits_card_in_envelope(a, b, c, d, margin=1):
    needed_w = c + 2*margin
    needed_h = d + 2*margin
    return (needed_w <= a and needed_h <= b) or (needed_w <= b and needed_h <= a)

 # 4.64
def head_through(a, b, d, margin=1):
    return d + 2*margin <= min(a, b)

 # 4.65
from itertools import combinations, permutations

def brick_through(a, b, c, x, y):
    edges = (a, b, c)
    for p, q in combinations(edges, 2):
        if (p <= x and q <= y) or (p <= y and q <= x):
            return True
    return False

 # 4.66
def box_in_suitcase(a1, a2, a3, b1, b2, b3):
    from itertools import permutations
    suitcase = (a1, a2, a3)
    box = (b1, b2, b3)
    for perm in permutations(box):
        if all(perm[i] <= suitcase[i] for i in range(3)):
            return True
    return False

 # 4.67
def is_lucky_number(n):
    s = str(abs(int(n)))
    s = s.zfill(6)
    if len(s) != 6:

        s = s[-6:]
    left = sum(int(ch) for ch in s[:3])
    right = sum(int(ch) for ch in s[3:])
    return left == right

 # 4.68
def is_leap_year(n):
    n = int(n)
    return (n % 4 == 0) and (n % 100 != 0 or n % 400 == 0)

 # 4.69
def max_domino_pieces(a, b, c, d):

    count1 = (a // c) * (b // d)
    count2 = (a // d) * (b // c)
    return max(count1, count2)

import math # для всех ниже перечисленных

 # 4.70
def day_type(k):

    if not (1 <= k <= 365):
        raise ValueError("k должен быть в диапазоне 1..365")
    weekday = (k - 1) % 7
    return "выходной" if weekday in (5, 6) else "рабочий"

 # 4.71
def projectile_hit(v0, alpha_deg, R, H, g=9.8, eps=1e-6):

    alpha = math.radians(alpha_deg)
    cos_a = math.cos(alpha)

    if abs(cos_a) < 1e-12:

        if abs(R) < eps:
            # t = 0 -> y = 0
            y = 0.0
            if abs(y - H) < eps:
                return "попадает"
            elif y > H:
                return "пролетит выше цели"
            else:
                return "упадёт ниже цели"
        else:
            return "не достигнет цели по горизонтали"

    t = R / (v0 * cos_a)
    if t < 0:
        return "цель находится в обратном направлении (t<0)"
    y = v0 * t * math.sin(alpha) - g * t * t / 2.0
    if abs(y - H) < eps:
        return "попадает"
    elif y > H:
        return "пролетит выше цели"
    else:
        return "упадёт ниже цели"

 # 4.72
def rects_relations(x1, y1, w1, h1, x2, y2, w2, h2):

    def inside(r1, r2):
        (x1, y1, w1, h1) = r1
        (x2, y2, w2, h2) = r2
        return x1 >= x2 - 1e-12 and (x1 + w1) <= (x2 + w2) + 1e-12 and y1 >= y2 - 1e-12 and (y1 + h1) <= (y2 + h2) + 1e-12

    def intersect(r1, r2):
        (x1, y1, w1, h1) = r1
        (x2, y2, w2, h2) = r2

        overlap_x = (x1 + w1) >= x2 - 1e-12 and (x2 + w2) >= x1 - 1e-12
        overlap_y = (y1 + h1) >= y2 - 1e-12 and (y2 + h2) >= y1 - 1e-12
        return overlap_x and overlap_y

    r1 = (x1, y1, w1, h1)
    r2 = (x2, y2, w2, h2)
    a = inside(r1, r2)
    b = a or inside(r2, r1)
    c = intersect(r1, r2)
    return a, b, c

 # 4.73
def digits_diff(a_tens, a_units, b):

    if not (1 <= a_tens <= 9 and 0 <= a_units <= 9 and 0 <= b <= 9):
        raise ValueError("Неверные цифры")
    A = 10 * a_tens + a_units
    D = A - b
    if not (10 <= D <= 99):
        raise ValueError("Разность не является двузначным числом (по условию это должно быть двузначное число)")
    d_tens = D // 10
    d_units = D % 10
    return d_tens, d_units


 # 4.74
def digits_diff(a1, a2, b1, b2):

    for x in (a1, a2, b1, b2):
        if not (0 <= x <= 9):
            raise ValueError("Цифры должны быть в диапазоне 0..9")
    n1 = 10 * a2 + a1
    n2 = 10 * b2 + b1
    diff = n1 - n2
    if not (10 <= diff <= 99):
        raise ValueError("Разность не является двузначным положительным числом")
    return diff // 10, diff % 10

 # 4.75
def digits_sum(a1, a2, a3, b1, b2):

    for x in (a1, a2, a3, b1, b2):
        if not (0 <= x <= 9):
            raise ValueError("Цифры должны быть в диапазоне 0..9")
    n1 = 100 * a3 + 10 * a2 + a1
    n2 = 10 * b2 + b1
    s = n1 + n2
    if not (100 <= s <= 999):
        raise ValueError("Сумма не является трёхзначным числом")
    return s // 100, (s // 10) % 10, s % 10


 # 4.76
def _check_coord(x):
    return 1 <= x <= 8

def _validate_coords(a, b, c, d):
    if not (_check_coord(a) and _check_coord(b) and _check_coord(c) and _check_coord(d)):
        raise ValueError("Координаты должны быть в диапазоне 1..8")

def rook_threat(a, b, c, d):

    _validate_coords(a, b, c, d)
    return (a == c or b == d) and not (a == c and b == d)

def bishop_threat(a, b, c, d):

    _validate_coords(a, b, c, d)
    return abs(a - c) == abs(b - d) and not (a == c and b == d)

def king_move(a, b, c, d):

    _validate_coords(a, b, c, d)
    dx = abs(a - c); dy = abs(b - d)
    return max(dx, dy) == 1 and (dx + dy > 0)

def queen_threat(a, b, c, d):

    _validate_coords(a, b, c, d)
    return rook_threat(a, b, c, d) or bishop_threat(a, b, c, d)

def white_pawn_can_move_normal(a, b, c, d):

    _validate_coords(a, b, c, d)
    if a != c:
        return False
    if d == b + 1:
        return True
    if b == 2 and d == b + 2:
        return True
    return False

def white_pawn_can_capture(a, b, c, d):

    _validate_coords(a, b, c, d)
    return abs(a - c) == 1 and d == b + 1

def black_pawn_can_move_normal(a, b, c, d):

    _validate_coords(a, b, c, d)
    if a != c:
        return False
    if d == b - 1:
        return True
    if b == 7 and d == b - 2:
        return True
    return False

def black_pawn_can_capture(a, b, c, d):

    _validate_coords(a, b, c, d)
    return abs(a - c) == 1 and d == b - 1

def knight_threat(a, b, c, d):

    _validate_coords(a, b, c, d)
    dx = abs(a - c); dy = abs(b - d)
    return (dx, dy) in ((1, 2), (2, 1))

















