 # 11.1
arr = [37, 0, 50, 46, 34, 46, 0, 13]
print(arr)

 # 11.2
arr = []
for i in range(10):
    x = input(f"Введите элемент {i+1}: ")
    arr.append(x)
print(arr)

 # 11.3
import random

n = 15

 # a
a = [random.random() for _ in range(n)]

 # b
b = [22 + random.random() for _ in range(n)]

 # c
c = [10 * random.random() for _ in range(n)]

 # d
d = [-50 + 100 * random.random() for _ in range(n)]

 # e
e = [random.randint(0, 10) for _ in range(n)]

print("a", a)
print("b", b)
print("c", c)
print("d", d)
print("e", e)

 # 11.4
arr = ['#'] * 20
print(arr)

 #11.5
import random
heights = [random.randint(163, 190) for _ in range(12)]
print(heights)

 # 11.6
import random
weights = [random.randint(50, 100) for _ in range(22)]
print(weights)

 # 11.7
import random

def random_int_array(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

arr = random_int_array(10, -5, 5)
print(arr)

 # 11.8
arr = [10, 20, 30, 40, 50]

i = int(input("Введите 0-based индекс: "))
if 0 <= i < len(arr):
    print(arr[i])
else:
    print("Индекс вне диапазона")

j = int(input("Введите 1-based индекс: "))
if 1 <= j <= len(arr):
    print(arr[j-1])
else:
    print("Индекс вне диапазона")

 # 11.9
arr = [1,2,3,4,5]

for x in reversed(arr):
    print(x)

print(arr[::-1])

 # 11.10
arr = list(range(1, 13))
print(arr)

 # 11.11
arr = list(range(1, 26))
arr.append(100)
arr.append(200)
print(arr)

from math import isqrt

 # 11.13
def task_11_13(n=20):
    return [2**i for i in range(n)]

 # 11.14
def task_11_14(n):
    if not (0 <= n <= 999999):
        raise ValueError("n должно быть в диапазоне 0..999999")
    length = 6
    arr = [0] * length
    x = n
    i = 0
    while x > 0 and i < length:
        arr[i] = x % 10
        x //= 10
        i += 1
    digits_of_n = arr[:i]
    return arr, digits_of_n

 # 11.15
def task_11_15():
    dec = [100 - 3*i for i in range(8)]
    inc = [-5 + 4*i for i in range(8)]
    return dec, inc

 # 11.16
def task_11_16_arithmetic(a1, d, count=10):
    return [a1 + i*d for i in range(count)]

def task_11_16_geometric(a1, q, count=20):
    res = []
    val = a1
    for i in range(count):
        res.append(val)
        val = val * q
    return res

 # 11.17
def task_11_17(count=10):
    if count <= 0:
        return []
    fib = [1, 1]
    while len(fib) < count:
        fib.append(fib[-1] + fib[-2])
    return fib[:count]

 # 11.18
def task_11_18_a(start=300, needed=21):
    res = []
    x = start
    while len(res) < needed:
        if x % 13 == 0 or x % 17 == 0:
            res.append(x)
        x += 1
    return res

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = isqrt(n)
    i = 3
    while i <= r:
        if n % i == 0:
            return False
        i += 2
    return True

def task_11_18_b(needed=20):
    res = []
    x = 2
    while len(res) < needed:
        if is_prime(x):
            res.append(x)
        x += 1
    return res


import random

 # 11.20
def task_11_20(num_questions=20, interactive=True):
    questions = []
    user_answers = []
    correct_answers = []
    for i in range(num_questions):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        questions.append((a, b))
        correct = a * b
        correct_answers.append(correct)
        prompt = f"{i+1}. Чему равно произведение {a} на {b}? "
        if interactive:
            try:
                ans = int(input(prompt))
            except Exception:
                ans = None
            user_answers.append(ans)
        else:
            print(prompt + f"(симулирую ответ = {correct})")
            user_answers.append(correct)
    return questions, user_answers, correct_answers

 # 11.21
def task_11_21(n=20, low=1, high=1000):
    if high - low + 1 < n:
        raise ValueError("Диапазон слишком мал для уникальных чисел.")
    return random.sample(range(low, high + 1), n)

 # 11.22
def task_11_22(arr):
    nonneg = [x for x in arr if x >= 0]
    le_100 = [x for x in arr if x <= 100]
    print("11.22 a) Неотрицательные элементы:", nonneg)
    print("11.22 b) Элементы <= 100:", le_100)
    return nonneg, le_100

 # 11.23
def task_11_23(arr):
    evens = [x for x in arr if x % 2 == 0]
    end_with_zero = [x for x in arr if abs(x) % 10 == 0]
    print("11.23 a) Чётные элементы:", evens)
    print("11.23 b) Элементы, оканчивающиеся нулём:", end_with_zero)
    return evens, end_with_zero

 # 11.24
def task_11_24(arr):
    two_digit = [x for x in arr if 10 <= x <= 99]
    three_digit = [x for x in arr if 100 <= x <= 999]
    print("11.24 a) Двузначные:", two_digit)
    print("11.24 b) Трёхзначные:", three_digit)
    return two_digit, three_digit

 # 11.25
def task_11_25(arr):
    every_2nd = [arr[i] for i in range(1, len(arr), 2)]
    every_3rd = [arr[i] for i in range(2, len(arr), 3)]
    print("11.25 a) 2-й, 4-й, ... элементы (1-based):", every_2nd)
    print("11.25 b) 3-й, 6-й, ... элементы (1-based):", every_3rd)
    return every_2nd, every_3rd

 # 11.26
def task_11_26(arr):
    nonneg = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    print("11.26 Сначала неотрицательные:", nonneg)
    print("11.26 Затем отрицательные:", neg)
    return nonneg + neg

 # 11.27
def task_11_27(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    print("11.27 Сначала чётные:", evens)
    print("11.27 Затем нечётные:", odds)
    return evens + odds

 # 11.28
def task_11_28(arr):

    indices = [i + 1 for i, x in enumerate(arr) if abs(x) % 10 == 0]
    print("11.28 Номера элементов, оканчивающихся на 0 (1-based):", indices)
    return indices

# 11.29
def task_11_29(rainfalls):
     if len(rainfalls) != 31:
         raise ValueError("Ожидается массив длины 31 (январь).")
     days_no_rain = [i + 1 for i, v in enumerate(rainfalls) if v == 0]
     print("11.29 В какие дни осадков не было (дни 1-based):", days_no_rain)
     return days_no_rain

 # 11.30
def task_11_30(wins):
     if len(wins) != 20:
         raise ValueError("Ожидается массив длины 20 (команды).")
     teams = [i + 1 for i, v in enumerate(wins) if v < 3]
     print("11.30 Номера команд с менее чем 3 победами (1-based):", teams)
     return teams

 # 11.31
def task_11_31(arr):
     even_pos = [arr[i] for i in range(1, len(arr), 2)]
     odd_pos = [arr[i] for i in range(0, len(arr), 2)]
     print("11.31 Сначала элементы на чётных местах (1-based):", even_pos)
     print("11.31 Затем элементы на нечётных местах (1-based):", odd_pos)
     return even_pos + odd_pos

 # 11.32
def task_11_32(arr):
     part_a = [abs(x) if x < 0 else x for x in arr]
     part_b = [x ** 2 if (i % 2 == 0) else x for i, x in enumerate(arr)]
     print("11.32 a) Отрицательные заменены на модуль:", part_a)
     print("11.32 b) Элементы с нечётными номерами (1-based) возведены в квадрат:", part_b)
     return part_a, part_b

import math
from typing import List, Union, Sequence

Number = Union[int, float]

def _to0(i: int, base: int) -> int:
    return i - 1 if base == 1 else i

 # 11.33
def task_11_33_a(arr: Sequence[Number]) -> List[float]:
    return [math.sqrt(x) if x > 10 else float(x) for x in arr]

def task_11_33_b(arr: Sequence[Number], base: int = 1) -> List[Number]:
    res = list(arr)
    for i in range(len(res)):
        idx = i + 1 if base == 1 else i
        if idx % 2 == 0:
            res[i] = abs(res[i])
    return res

 # 11.34
def task_11_34_a(arr: Sequence[Number], k1: int, k2: int, base: int = 1) -> List[Number]:
    res = list(arr)
    k1i = _to0(k1, base)
    k2i = _to0(k2, base)
    v1 = arr[k1i]
    v2 = arr[k2i]
    for i, x in enumerate(res):
        res[i] = x - v1 if x > 0 else x - v2
    return res

def task_11_34_b(arr: Sequence[Number], base: int = 1) -> List[Number]:
    res = list(arr)
    for i in range(len(res)):
        idx = i + 1 if base == 1 else i
        if idx % 2 == 1:
            res[i] = res[i] + 1
        else:
            res[i] = res[i] - 1
    return res

 # 11.35
def task_11_35_a(arr: Sequence[Number], m1: int, m2: int, base: int = 1) -> List[Number]:
    res = list(arr)
    m1i = _to0(m1, base)
    m2i = _to0(m2, base)
    v1 = arr[m1i]
    v2 = arr[m2i]
    for i, x in enumerate(res):
        res[i] = x + v1 if x < 0 else x + v2
    return res

def task_11_35_b(arr: Sequence[Number], base: int = 1) -> List[Number]:
    res = list(arr)
    for i in range(len(res)):
        idx = i + 1 if base == 1 else i
        if idx % 2 == 0:
            res[i] = res[i] * 2
        else:
            res[i] = res[i] - 1
    return res

 # 11.36
def task_11_36_a(arr: Sequence[Number], k1: int, n: Number, base: int = 1) -> List[Number]:
    res = list(arr)
    k1i = _to0(k1, base)
    v = arr[k1i]
    for i, x in enumerate(res):
        if x > 0:
            res[i] = x - v
        elif x < 0:
            res[i] = x - n
        else:
            res[i] = x
    return res

def task_11_36_b(arr: Sequence[Number], n: Number, b: Number) -> List[Number]:
    res = list(arr)
    for i, x in enumerate(res):
        if x == 0:
            res[i] = x + n
        elif x > 0:
            res[i] = x - n
        else:
            res[i] = x + b
    return res

 # 11.37
def task_11_37_a(arr: Sequence[Number], m1: int, b: Number, base: int = 1) -> List[Number]:
    res = list(arr)
    m1i = _to0(m1, base)
    v = arr[m1i]
    for i, x in enumerate(res):
        if x < 0:
            res[i] = x + v
        elif x == 0:
            res[i] = x - b
        else:
            res[i] = x
        return res

def task_11_37_b(arr: Sequence[Number], a: Number, b: Number, c: Number) -> List[Number]:
        res = list(arr)
        for i, x in enumerate(res):
            if x > 0:
                res[i] = x - a
            elif x < 0:
                res[i] = x - b
            else:
                res[i] = x + c
            return res

 # 11.38
def task_11_38_a(arr: Sequence[int]) -> List[Union[int, float]]:
    res = list(arr)
    for i, x in enumerate(res):
        if abs(x) % 10 == 4:
            res[i] = x / 2
    return res

def task_11_38_b(arr: Sequence[int]) -> List[int]:
    res = []
    for x in arr:
        if x % 2 == 0:
            res.append(x * x)
        else:
            res.append(x * 2)
    return res

def task_11_38_c(arr: Sequence[int], a: Number, b: Number, base: int = 1) -> List[Number]:
    res = list(arr)
    for i, x in enumerate(res):
        if x % 2 == 0:
            res[i] = x + a
    for i in range(len(res)):
        idx = i + 1 if base == 1 else i
        if idx % 2 == 0:
            res[i] = res[i] - b
    return res

 # 11.39
def task_11_39_a(arr: Sequence[int]) -> List[int]:
    return [0 if x % 10 == 0 else x for x in arr]

def task_11_39_b(arr: Sequence[int]) -> List[Union[int, float]]:
    res = []
    for x in arr:
        if x % 2 == 0:
            res.append(x * 2)
        else:
            res.append(x / 2)
    return res

def task_11_39_c(arr: Sequence[int], n: Number, base: int = 1) -> List[Number]:
    res = list(arr)
    for i, x in enumerate(res):
        if x > 0:
            res[i] = x * 2
    for i in range(len(res)):
        idx = i + 1 if base == 1 else i
        if idx % 2 == 1:
            res[i] = res[i] - n
    return res

 # 11.40
def sqrt_of_element(arr: Sequence[Number], idx: int, base: int = 1) -> float:
    i = _to0(idx, base)
    x = arr[i]
    if x < 0:
        raise ValueError("Невозможно взять корень из отрицательного числа")
    return math.sqrt(x)

def average(arr: Sequence[Number]) -> float:
    if len(arr) == 0:
        return 0.0
    return sum(arr) / len(arr)

from typing import List, Tuple, Union

from typing import List, Optional, Tuple

# 11.41 a
def is_positive(arr: List[int], s: int) -> Optional[bool]:
    if s < 1 or s > len(arr):
        return None
    return arr[s-1] > 0

# 11.41 b
def is_even(arr: List[int], k: int) -> Optional[bool]:
    if k < 1 or k > len(arr):
        return None
    return arr[k-1] % 2 == 0

# 11.41 c
def compare_k_s(arr: List[int], k: int, s: int) -> Optional[str]:
    if k < 1 or k > len(arr) or s < 1 or s > len(arr):
        return None
    a = arr[k-1]
    b = arr[s-1]
    if a > b:
        return "k > s"
    elif a < b:
        return "k < s"
    else:
        return "k == s"

# 11.42 a
def sum_all(arr: List[int]) -> int:
    return sum(arr)

# 11.42 b
def prod_all(arr: List[int]) -> int:
    if not arr:
        return 0
    p = 1
    for x in arr:
        p *= x
    return p

# 11.42 c
def sum_squares(arr: List[int]) -> int:
    return sum(x*x for x in arr)

# 11.42 d
def sum_first_six(arr: List[int]) -> int:
    return sum(arr[:6])

# 11.42 e
def sum_range(arr: List[int], k1: int, k2: int) -> Optional[int]:
    if k1 < 1 or k2 < k1 or k2 > len(arr):
        return None
    return sum(arr[k1-1:k2])

 # 11.42 f
def average_all(arr: List[int]) -> Optional[float]:
    if not arr:
        return None
    return sum(arr) / len(arr)

 # 11.42 g
def average_range(arr: List[int], s1: int, s2: int) -> Optional[float]:
    if s1 < 1 or s2 < s1 or s2 > len(arr):
        return None
    sub = arr[s1-1:s2]
    if not sub:
        return None
    return sum(sub) / len(sub)

 # 11.43
def alternating_sum(arr: List[int]) -> int:
    total = 0
    for i, val in enumerate(arr, start=1):
        if i % 2 == 1:
            total += val
        else:
            total -= val
    return total

 # 11.44
def total_precipitation(arr: List[int]) -> int:
    return sum(arr)

 # 11.45
def total_cost_12(arr: List[float]) -> Optional[float]:
    if len(arr) != 12:
        return sum(arr)
    return sum(arr)

 # 11.46
def total_resistance_series(arr: List[float]) -> float:
    return sum(arr)

 # 11.47
def total_resistance_parallel(arr: List[float]) -> Optional[float]:
    if not arr:
        return None
    if any(r == 0 for r in arr):
        return 0.0
    inv_sum = 0.0
    for r in arr:
        inv_sum += 1.0 / r
    if inv_sum == 0:
        return None
    return 1.0 / inv_sum

 # 11.48
def decade_sums(arr: List[int], days_in_month: int = 30, decade_size: int = 10) -> List[int]:
    res = []
    n = min(len(arr), days_in_month)
    for start in range(0, n, decade_size):
        res.append(sum(arr[start:start + decade_size]))
    return res

 # 11.49
def average_per_day(arr: List[int]) -> Optional[float]:
    if not arr:
        return None
    return sum(arr) / len(arr)

 # 11.50
def average_per_decade(arr: List[int], days_in_month: int = 30, decade_size: int = 10) -> List[Optional[float]]:
    n = min(len(arr), days_in_month)
    res = []
    for start in range(0, n, decade_size):
        chunk = arr[start:start+decade_size]
        if chunk:
            res.append(sum(chunk) / len(chunk))
        else:
            res.append(None)
    return res

 # 11.51
def is_sum_odd(arr: List[int]) -> Optional[bool]:
    if not arr:
        return None
    return sum(arr) % 2 != 0

 # 11.52
def task_11_52(arr: List[int]) -> Tuple[bool, bool]:
    s = sum(arr)
    sum_sq = sum(x*x for x in arr)
    return (s % 2 == 0, 10000 <= sum_sq <= 99999)

 # 11.53
def task_11_53(arr: List[int]) -> bool:
    total = sum(arr)
    return 1000 <= total <= 9999

 # 11.54
def task_11_54(arr: List[int]) -> bool:
    total = sum(arr)
    return 100000 <= total <= 999999

 # 11.55
def task_11_55(weights: List[Union[int, float]], capacity: Union[int, float]) -> bool:
    return sum(weights) <= capacity

 # 11.56
def task_11_56(scores: List[Union[int, float]], threshold: Union[int, float]) -> bool:
    return sum(scores) > threshold

# 11.57
def task_11_57(daily_precip: List[Union[int, float]]) -> Tuple[str, Union[int, List[int]]]:
    n = len(daily_precip)
    mid = n // 2
    first_sum = sum(daily_precip[:mid])
    second_sum = sum(daily_precip[mid:])
    if first_sum > second_sum:
        which = "first"
    elif first_sum < second_sum:
        which = "second"
    else:
        which = "equal"

    decade_sums = []
    decade_sums.append(sum(daily_precip[0:10]))
    decade_sums.append(sum(daily_precip[10:20]))
    decade_sums.append(sum(daily_precip[20:30]))
    max_sum = max(decade_sums)
    best = [i+1 for i, v in enumerate(decade_sums) if v == max_sum]
    if len(best) == 1:
        best = best[0]
    return which, best

 # 11.58
def task_11_58(scores: List[Union[int, float]]) -> str:
    if len(scores) < 18:
        obligatory = sum(scores[:6])
        free = sum(scores[6:])
    else:
        obligatory = sum(scores[:6])
        free = sum(scores[6:18])
    if obligatory > free:
        return "obligatory"
    elif obligatory < free:
        return "free"
    else:
        return "equal"

 # 11.59
def task_11_59(arr: List[Union[int, float]], a: Union[int, float]) -> Tuple[Union[int, float], Union[int, float]]:

    sum_le_20 = sum(x for x in arr if x <= 20)
    sum_gt_a = sum(x for x in arr if x > a)
    return sum_le_20, sum_gt_a

 # 11.60
def task_11_60(arr: List[int], k: int, a: int, b: int) -> Tuple[int, int, int]:
    sum_odd = sum(x for x in arr if x % 2 != 0)
    sum_mult_k = sum(x for x in arr if k != 0 and x % k == 0)
    sum_mult_a_b = sum(x for x in arr if (a != 0 and x % a == 0) or (b != 0 and x % b == 0))
    return sum_odd, sum_mult_k, sum_mult_a_b

 # 11.61
def task_11_61(arr: List[Union[int, float]]) -> Union[int, float]:
     return sum(arr[1::2])

 # 11.62
def task_11_62(daily_precip_feb: List[Union[int, float]]) -> Union[int, float]:
     return sum(daily_precip_feb[1::2])

 # 11.63
def task_11_63(monthly_precip: List[Union[int, float]]) -> Union[int, float]:
     indices = [2, 5, 8, 11]
     return sum(monthly_precip[i] for i in indices if i < len(monthly_precip))

from typing import List, Tuple, Optional


 # 11.64
def task_11_64(a: List[float]) -> Optional[float]:

    sum_pos = sum(x for x in a if x > 0)
    sum_neg = sum(x for x in a if x < 0)
    if sum_neg == 0:
        return None
    return sum_pos / abs(sum_neg)

 # 11.65
def task_11_65(a: List[int]) -> Tuple[bool, bool]:

    sum_gt20 = sum(x for x in a if x > 20)
    count_lt50 = sum(1 for x in a if x < 50)
    return (sum_gt20 > 100, count_lt50 % 2 == 0)

 # 11.66
def task_11_66(precip: List[float]) -> bool:

    odd_sum = sum(precip[i] for i in range(0, len(precip), 2))   # дни 1,3,...
    even_sum = sum(precip[i] for i in range(1, len(precip), 2))  # дни 2,4,...
    return even_sum > odd_sum

 # 11.67
def task_11_67(residents: List[int]) -> str:
    odd_sum = sum(residents[i] for i in range(0, len(residents), 2))
    even_sum = sum(residents[i] for i in range(1, len(residents), 2))
    if odd_sum > even_sum:
        return 'odd'
    if even_sum > odd_sum:
        return 'even'
    return 'equal'

 # 11.68
def task_11_68(a: List[float]) -> int:
    return sum(1 for x in a if x >= 0)

 # 11.69
def task_11_69(a: List[int], k: int) -> Tuple[int, int]:
    if not a:
        return (0, 0)
    last = a[-1]
    count_not_equal_last = sum(1 for x in a if x != last)
    count_div_by_k = sum(1 for x in a if k != 0 and x % k == 0)
    return (count_not_equal_last, count_div_by_k)

 # 11.70
def task_11_70(precip: List[float]) -> int:
    return sum(1 for x in precip if x == 0)

 # 11.71
def task_11_71(grades: List[int]) -> int:
    return sum(1 for g in grades if g < 3)

 # 11.72
def task_11_72(sales: List[float], s: float) -> int:
    return sum(1 for x in sales if x > s)

 # 11.73
def task_11_73(heights: List[float], r: float) -> int:
    return sum(1 for h in heights if h <= r)

 # 11.74
def task_11_74(a: List[float], left: float, right: float) -> int:
    if left > right:
        return sum(1 for x in a if left <= x <= right)

 # 11.75
def task_11_75(results: List[int]) -> Tuple[int, int, int]:
    wins = sum(1 for r in results if r == 3)
    draws = sum(1 for r in results if r == 1)
    losses = sum(1 for r in results if r == 0)
    return (wins, draws, losses)

 # 11.76
def task_11_76(grades: List[int]) -> int:
    return sum(1 for g in grades if g == 4 or g == 5)

from typing import List, Tuple, Optional
import statistics

 # 11.91
def avg_full_and_others(masses: List[float], threshold: float = 100.0) -> Tuple[Optional[float], Optional[float]]:
    full = [m for m in masses if m > threshold]
    others = [m for m in masses if m <= threshold]
    avg_full = statistics.mean(full) if full else None
    avg_others = statistics.mean(others) if others else None
    return avg_full, avg_others

 # 11.92
def avg_height_by_gender(heights: List[float]) -> Tuple[Optional[float], Optional[float]]:
    boys = [abs(h) for h in heights if h < 0]
    girls = [h for h in heights if h > 0]
    avg_boys = statistics.mean(boys) if boys else None
    avg_girls = statistics.mean(girls) if girls else None
    return avg_boys, avg_girls

 # 11.93
def is_cars_avg_more_than_ratio(cars: List[float], motos: List[float], ratio: float = 3.0) -> bool:
    if not cars or not motos:
        raise ValueError("Списки автомобилей и/или мотоциклов не должны быть пустыми.")
    avg_cars = statistics.mean(cars)
    avg_motos = statistics.mean(motos)
    return avg_cars > ratio * avg_motos

 # 11.94
def is_boys_avg_higher_by(heights: List[float], diff_cm: float = 10.0) -> Optional[bool]:
    avg_boys, avg_girls = avg_height_by_gender(heights)
    if avg_boys is None or avg_girls is None:
        return None
    return (avg_boys - avg_girls) > diff_cm

 # 11.95
def elements_greater_than_sum_of_rest(arr: List[float]) -> Tuple[int, List[int]]:
    total = sum(arr)
    indices = []
    for i, val in enumerate(arr):
        if val > (total - val):
            indices.append(i + 1)  # 1-based
    return len(indices), indices

 # 11.96
def elements_greater_than_avg_min_max(arr: List[float]) -> Tuple[int, List[int], Optional[float]]:
    if not arr:
        return 0, [], None
    mn = min(arr)
    mx = max(arr)
    threshold = (mn + mx) / 2.0
    indices = [i + 1 for i, v in enumerate(arr) if v > threshold]
    return len(indices), indices, threshold

 # 11.97
def count_above_class_avg(heights: List[float]) -> Tuple[int, List[int], Optional[float]]:
    if not heights:
        return 0, [], None
    avg = statistics.mean(heights)
    indices = [i + 1 for i, h in enumerate(heights) if h > avg]
    return len(indices), indices, avg

 # 11.98
def count_items_below_average(prices: List[float]) -> Tuple[int, List[int], Optional[float]]:
    if not prices:
        return 0, [], None
    avg = statistics.mean(prices)
    indices = [i + 1 for i, p in enumerate(prices) if p < avg]
    return len(indices), indices, avg

 # 11.99
def january_precip_days_above_avg(precip: List[float]) -> Tuple[int, List[int], Optional[float]]:
    if not precip:
        return 0, [], None
    avg = statistics.mean(precip)
    days = [i + 1 for i, v in enumerate(precip) if v > avg]
    return len(days), days, avg

 # 11.100
def students_below_average(grades: List[float]) -> Tuple[int, List[int], Optional[float]]:
    if not grades:
        return 0, [], None
    avg = statistics.mean(grades)
    indices = [i + 1 for i, g in enumerate(grades) if g < avg]
    return len(indices), indices, avg

 # 11.101
def yearly_precip_mean_and_deviations(years: List[float]) -> Tuple[Optional[float], List[float]]:
    if not years:
        return None, []
    mean_val = statistics.mean(years)
    deviations = [y - mean_val for y in years]
    return mean_val, deviations

 # 11.102
def element_closest_to_average(arr: List[float]) -> Tuple[Optional[float], Optional[int], Optional[float]]:
    if not arr:
        return None, None, None
    avg = statistics.mean(arr)
    best_idx = 0
    best_diff = abs(arr[0] - avg)
    for i, v in enumerate(arr):
        d = abs(v - avg)
        if d < best_diff:
            best_diff = d
            best_idx = i
    return arr[best_idx], best_idx + 1, best_diff








