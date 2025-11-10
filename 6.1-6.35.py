 # 6.1
def div_and_mod_by_subtraction(a, b):
    if b <= 0:
        raise ValueError("b must be positive")
    q = 0
    r = a
    while r >= b:
        r -= b
        q += 1
    return q, r

 # 6.2.
def print_naturals_up_to(N):
    i = 1
    while i <= N:
        print(i, end=' ')
        i += 1
    print()

 # 6.3
def print_even_10_100():
    i = 10
    while i <= 100:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1
    print()

 # 6.4
def min_gt_190_div_by_17():

    k = 190 // 17 + 1
    return k * 17

 # 6.5
def max_le_5000_div_by_139():
    k = 5000 // 139
    return k * 139

 # 6.6
def find_n_by_factorial(F):
    if F < 1:
        return None
    prod = 1
    n = 1
    while prod < F:
        n += 1
        prod *= n
    return n if prod == F else None

 # 6.7
def print_numbers_square_le_N(N):
    i = 1
    while i * i <= N:
        print(i, end=' ')
        i += 1
    print()

 # 6.8
def first_square_gt_N(N):
    i = 1
    while i * i <= N:
        i += 1
    return i

 # 6.9 – 6.11
def input_positive_int(prompt="Введите натуральное число: "):
    while True:
        s = input(prompt)
        try:
            x = int(s)
            if x > 0:
                return x
            else:
                print("Число должно быть положительным (>0). Повторите.")
        except ValueError:
            print("Не целое число. Повторите.")

 # 6.12
def process_sequence_until_zero():
    print("Введите последовательность целых. Для окончания введите 0.")
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Неверный ввод, повторите.")
            continue
        if x == 0:
            break
        print("Положительное" if x > 0 else "Отрицательное")

 # 6.13
def print_10_to_30_column():
    for i in range(10, 31):
        print(i)
import math

 # 6.14
def task_6_14():
    i = 100
    while i >= 80:
        print(i)
        i -= 1

 # 6.15
def task_6_15():
    for i in range(2, 152, 10):
        print(i, i + 2)

 # 6.16
    seq = []
    i = 2.0
    while i <= n:
        seq.append(i)
        i *= 0.5
    for i in seq:
        print(n, i)

 # 6.17
def task_6_17():
    x = 1.0
    while x <= 13.5 + 1e-9:
        print(f"{x:.1f}")
        x += 0.5

 # 6.18
 # (a)
def task_6_18_while(a, b):
    i = a
    while i <= b:
        print(math.sqrt(i))
        i += 1

 # (b)
def task_6_18_do_while(a, b):
    i = a
    while True:
        print(math.sqrt(i))
        i += 1
        if i > b:
            break

 # 6.19
def task_6_19(n):
    s = str(n)
    for ch in s:
        print(ch)

 # 6.20
def task_6_20(n):
    if n == 0:
        return {
            "sum": 0,
            "count": 1,
            "product": 0,
            "average": 0.0,
            "sum_squares": 0,
            "sum_cubes": 0,
            "first_digit": 0,
            "first_plus_last": 0
        }

    s = str(n)
    digits = [int(ch) for ch in s]
    total = sum(digits)
    count = len(digits)
    product = 1
    for d in digits:
        product *= d
    avg = total / count
    sum_squares = sum(d * d for d in digits)
    sum_cubes = sum(d ** 3 for d in digits)
    first = digits[0]
    last = digits[-1]
    return {
        "sum": total,
        "count": count,
        "product": product,
        "average": avg,
        "sum_squares": sum_squares,
        "sum_cubes": sum_cubes,
        "first_digit": first,
        "first_plus_last": first + last
    }

 # 6.21
def second_digit_from_left(n: int) -> int:
    s = str(n)
    if len(s) < 2:
        raise ValueError("n должно иметь хотя бы 2 цифры")
    return int(s[1])

 # 6.22
def first_digit_from_left(n: int) -> int:
    s = str(n)
    if len(s) < 1:
        raise ValueError("некорректное n")
    return int(s[0])

 # 6.23
def sum_last_m_digits(n: int, m: int):
    s = str(n)
    if m <= 0:
        return 0
    if len(s) < m:
        return None
    return sum(int(ch) for ch in s[-m:])

 # 6.24
def alternating_sums(n: int):
    s = [int(ch) for ch in str(n)]
    rev = list(reversed(s))
    a = sum(((-1)**i) * rev[i] for i in range(len(rev)))
    b = sum(((-1)**(len(s)-1-i)) * s[i] for i in range(len(s)))
    return a, b

 # 6.25
def smallest_divisor(n: int) -> int:
    if n <= 1:
        raise ValueError("n должно быть > 1")
    if n % 2 == 0:
        return 2
    i = 3
    import math
    lim = int(math.isqrt(n))
    while i <= lim:
        if n % i == 0:
            return i
        i += 2
    return n

 # 6.26
def multiples_of_13_method1(upper: int):
    return list(range(13, upper, 13))

def multiples_of_13_method2(upper: int):
    return [x for x in range(1, upper) if x % 13 == 0]

 # 6.27
def first_k_divisible_in_interval(k: int, d: int, left: int, right: int = None):
    res = []
    x = left
    if x % d != 0:
        x += (d - x % d)
    while True:
        if right is not None and x >= right:
            break
        res.append(x)
        if len(res) >= k:
            break
        x += d
    return res

 # 6.28
def first_k_divisible_by_any(k: int, divisors: list, left: int, right: int = None):
    res = []
    x = left
    while True:
        if any(x % d == 0 for d in divisors):
            res.append(x)
            if len(res) >= k:
                break
        x += 1
        if right is not None and x >= right:
            break
    return res

 # 6.29
def first_k_with_last_digit_and_divisible(k: int, digit_end: int, d: int, left: int):
    res = []
    x = left
    while len(res) < k:
        if x % 10 == digit_end and x % d == 0:
            res.append(x)
        x += 1
    return res

 # 6.30
def integer_division_and_remainder(a, b):
    if a <= 0:
        raise ValueError("a must be positive")
    q = 0
    rem = b
    while rem >= a:
        rem -= a
        q += 1
    return q, rem

 # 6.31
def bank_growth(S0=1000.0, monthly_rate=0.02):
    s = S0
    # a)
    for _ in range(12):
        s *= (1 + monthly_rate)
    after_year = s
    # b)
    s2 = S0
    months = 0
    target = 1200.0
    while s2 <= target:
        s2 *= (1 + monthly_rate)
        months += 1
    return after_year, months

 # 6.32
def skier(d0=10.0, daily_increase_rate=0.10, limit_day_km=20.0, limit_total_km=100.0):
    day = 1
    today = d0
    total = today
    day_exceed_single = None
    if today > limit_day_km:
        day_exceed_single = 1
    if total > limit_total_km:
        day_exceed_total = 1
    else:
        day_exceed_total = None

    while day_exceed_single is None or day_exceed_total is None:
        day += 1
        today *= (1 + daily_increase_rate)
        total += today
        if day_exceed_single is None and today > limit_day_km:
            day_exceed_single = day
        if day_exceed_total is None and total > limit_total_km:
            day_exceed_total = day
    return day_exceed_single, day_exceed_total

 # 6.33
def crop_growth(initial=1.0, yearly_rate=0.05, target_yield=2.0, target_sum1=10.0, target_sum2=15.0):
    year = 1
    yield_year = initial
    if yield_year > target_yield:
        year_exceed_yield = 1
    else:
        year_exceed_yield = None
    total = yield_year
    year_exceed_sum1 = None
    year_exceed_sum2 = None
    if total > target_sum1:
        year_exceed_sum1 = 1
    if total > target_sum2:
        year_exceed_sum2 = 1

    while year_exceed_yield is None or year_exceed_sum1 is None or year_exceed_sum2 is None:
        year += 1
        yield_year *= (1 + yearly_rate)
        total += yield_year
        if year_exceed_yield is None and yield_year > target_yield:
            year_exceed_yield = year
        if year_exceed_sum1 is None and total > target_sum1:
            year_exceed_sum1 = year
        if year_exceed_sum2 is None and total > target_sum2:
            year_exceed_sum2 = year
    return year_exceed_yield, year_exceed_sum1, year_exceed_sum2

 # 6.34
m, n = map(int, input().split())
limit = m * n
multiples = sorted(set(range(m, limit + 1, m)) | set(range(n, limit + 1, n)))
print(*multiples)

# 6.35
def digit_tasks(n):
    if n <= 0:
        raise ValueError("n must be a natural number (>0)")
    s = str(n)
    num_digits = len(s)
    last_digit = s[-1]
    count_last = s.count(last_digit)
    count_0_and_5 = s.count('0') + s.count('5')
    return num_digits, count_last, count_0_and_5




































