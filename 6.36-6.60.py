def digits_str(n):
    return str(n)

def digits_list(n):
    return [int(ch) for ch in str(n)]

 # 6.36 а)
def count_digit(n, a):
    s = digits_str(n)
    return s.count(str(a))

 # 6.36 б)
def sum_digits_greater_than(n, a):
    return sum(d for d in digits_list(n) if d > a)

# 6.36 в)
def sum_even_digits(n):
    return sum(d for d in digits_list(n) if d % 2 == 0)

# 6.36 г)
def count_digits_x_y(n, x, y):
    s = digits_str(n)
    return s.count(str(x)) + s.count(str(y))

 # 6.37/6.38.
def pos_digit_from_end(n, d):
    s = digits_str(n)
    dch = str(d)
    for i, ch in enumerate(reversed(s), start=1):
        if ch == dch:
            return i
    return 0

 # 6.39
def kth_digit_from_start(n, k):
    s = digits_str(n)
    if 1 <= k <= len(s):
        return int(s[k-1])
    return None

 # 6.40
def count_adjacent_pair(n, a, b):
    s = digits_str(n)
    pair = str(a) + str(b)
    count = 0
    for i in range(len(s)-1):
        if s[i:i+2] == pair:
            count += 1
    return count

 # 6.41
def max_digit(n):
    return max(digits_list(n))

def min_digit(n):
    return min(digits_list(n))

def sum_max_min(n):
    return max_digit(n) + min_digit(n)

def diff_max_min(n):
    return max_digit(n) - min_digit(n)
def max_min_digits(n):
    if n == 0:
        return 0, 0
    mn = 9
    mx = 0
    while n > 0:
        d = n % 10
        if d < mn:
            mn = d
        if d > mx:
            mx = d
        n //= 10
    return mx, mn

 # 6.42
def task_642(n):
    mx, mn = max_min_digits(n)
    difference = mx - mn
    summ = mx + mn
    return mx, mn, difference, summ

 # 6.43
def task_643(n, k):
    mx, mn = max_min_digits(n)
    return (mx + mn) % k == 0

 # 6.44
def is_sum_max_min_divisible_by_a(n, a):
    if a == 0:
        raise ValueError("Деление на ноль не определено")
    return sum_max_min(n) % a == 0
from typing import List, Tuple, Optional, Dict
def digits(n: int) -> List[int]:
    return [int(d) for d in str(n)]
def product_of_digits(digs: List[int]) -> int:
    p = 1
    for d in digs:
        p *= d
    return p

 # 6.45
s = input().strip()
n = len(s)

max_digit = -1
min_digit = 10
pos_max_from_start = pos_max_from_end = None
pos_min_from_start = pos_min_from_end = None

for i, ch in enumerate(s):
    d = int(ch)
    pos_start = i + 1
    pos_end = n - i

    if d > max_digit:
        max_digit = d
        pos_max_from_start = pos_start
        pos_max_from_end = pos_end

    if d < min_digit:
        min_digit = d
        pos_min_from_start = pos_start
        pos_min_from_end = pos_end

 # 6.46
def solve_6_46(n: int) -> Tuple[int,int,int,int]:
    digs = digits(n)
    max_d = max(digs)
    min_d = min(digs)
    # позиции с начала (1-based)
    pos_max_start = digs.index(max_d) + 1
    pos_min_start = digs.index(min_d) + 1
    # позиции с конца (1-based)
    pos_max_end = len(digs) - (pos_max_start - 1)
    pos_min_end = len(digs) - (pos_min_start - 1)
    return pos_max_end, pos_min_end, pos_max_start, pos_min_start

 # 6.47
def solve_6_47(n: int) -> str:

    digs = digits(n)
    max_d = max(digs)
    min_d = min(digs)
    pos_max = digs.index(max_d)
    pos_min = digs.index(min_d)
    if pos_max < pos_min:
        return 'max'
    elif pos_min < pos_max:
        return 'min'
    else:
        return 'same'

 # 6.48
def solve_6_48(n: int) -> Tuple[Optional[int], int]:
    digs = digits(n)
    odd_digits = [d for d in digs if d % 2 == 1]
    max_odd = max(odd_digits) if odd_digits else None
    pos_min = digs.index(min(digs)) + 1
    return max_odd, pos_min

 # 6.49
def solve_6_49(n: int) -> Dict[str, object]:
    digs = digits(n)
    s = sum(digs)
    p = product_of_digits(digs)
    length = len(digs)
    first = digs[0]
    last = digs[-1]
    res = {
        'a_sum_gt_10': s > 10,
        'b_prod_lt_50': p < 50,
        'c_num_digits_even': (length % 2 == 0),
        'd_is_four_digit': (length == 4),
        'e_first_le_6': (first <= 6),
        'f_same_first_last': (first == last),
    }
    if first > last:
        which = 'first'
    elif last > first:
        which = 'last'
    else:
        which = 'equal'
    res['g_which_digit_larger_first_or_last'] = which
    return res

 # 6.50
def solve_6_50(n: int, a: int, b: int, k: int, m: int) -> Dict[str, bool]:
    digs = digits(n)
    s = sum(digs)
    p = product_of_digits(digs)
    length = len(digs)
    first = digs[0]
    return {
        'a_sum_less_a': s < a,
        'b_prod_gt_b': p > b,
        'c_is_k_digits': (length == k),
        'd_first_le_m': (first <= m),
    }
 # 6.51
def digits(n):
    return [int(ch) for ch in str(n)]

def check_properties(num, k, b_limit, x, y, a_limit, b_div, m_sum, n_div):
    digs = digits(num)
    sum_d = sum(digs)
    prod_d = 1
    for d in digs:
        prod_d *= d
    num_digits = len(digs)
    first = digs[0]
    last = digs[-1]

    a_res = (sum_d > k) and (num % 2 == 0)
    b_res = (num_digits % 2 == 0) and (num <= b_limit)
    v_res = (first == x) and (last == y)
    g_res = (prod_d < a_limit) and (b_div != 0 and num % b_div == 0)
    d_res = (sum_d > m_sum) and (n_div != 0 and num % n_div == 0)

    return {
        'a': a_res,
        'b': b_res,
        'v': v_res,
        'g': g_res,
        'd': d_res
    }
# Общ утилиты
def digits_list(n):
    s = str(n)
    return [int(ch) for ch in s]

def count_digit(n, d):
    if n == 0:
        return 1 if d == 0 else 0
    cnt = 0
    while n:
        if n % 10 == d:
            cnt += 1
        n //= 10
    return cnt

 # 6.52
def has_digit_3(n):
    return count_digit(n, 3) > 0

def has_digits_2_and_5(n):
    return count_digit(n, 2) > 0 and count_digit(n, 5) > 0

 # 6.53
def has_digit_a(n, a):
    return count_digit(n, a) > 0

def no_digit_b(n, b):
    return count_digit(n, b) == 0

def digit_a_more_than_k(n, a, k):
    return count_digit(n, a) > k

def has_digits_a_and_b(n, a, b):
    return count_digit(n, a) > 0 and count_digit(n, b) > 0

 # 6.54
def which_more_0_or_9(n):
    c0 = count_digit(n, 0)
    c9 = count_digit(n, 9)
    if c0 > c9:
        return 0
    if c9 > c0:
        return 9
    return None

 # 6.55
def digit_a_less_than_b(n, a, b):
    return count_digit(n, a) < count_digit(n, b)

 # 6.56
def which_leftmost_of_2_and_5(n, x=2, y=5):
    s = str(n)
    i_x = s.find(str(x))
    i_y = s.find(str(y))
    if i_x == -1 or i_y == -1:
        return None
    return 'x' if i_x < i_y else 'y'

 # 6.57
def which_rightmost_of_a_and_b(n, a, b):
    s = str(n)
    i_a = s.rfind(str(a))
    i_b = s.rfind(str(b))
    if i_a == -1 or i_b == -1:
        return None
    return 'a' if i_a > i_b else 'b'

 # 6.58
def count_max_digit(n):
    s = str(n)
    maxd = max(int(ch) for ch in s)
    return s.count(str(maxd))

 # 6.59
def count_min_digit(n):
    s = str(n)
    mind = min(int(ch) for ch in s)
    return s.count(str(mind))

 # 6.60
def max_and_min_digit_distinct(n):
    s = str(n)
    digits = [int(ch) for ch in s]
    return max(digits), min(digits)






































