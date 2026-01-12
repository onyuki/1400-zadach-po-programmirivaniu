 # 9.1
 #a
for _ in range(5):
    print(" ".join(["8"]*3))
 #б
for i in range(1, 8):
    print(" ".join([str(i)] * 4))
 #в
for i in range(10, 90, 10):
    print(" ".join([str(i)] * 4))
 #г
for i in range(12, 83, 10):
    print(" ".join([str(i)] * 4))
 #д
row = " ".join(str(i) for i in range(2, 21))
for _ in range(4):
    print(row)
 #е
row = " ".join(str(i) for i in range(15, 2, -1))
for _ in range(3):
    print(row)
 #ж
for _ in range(6):
    print(" ".join(["0"] * 5))
 #з
max_len = 8
for length in range(max_len, 0, -1):
    print(" ".join(str(i) for i in range(max_len, max_len - length, -1)))
 #и
row = " ".join(str(i) for i in range(2, 11))
for _ in range(4):
    print(row)
 #й
n = 5
for length in range(1, n+1):
    print(" ".join(str(i) for i in range(2, 2+length)))
 #к
start = 3
for i in range(start, start + 4):
    print(" ".join([str(i)] * (i - start + 1)))
 #л
start = 21
rows = 5
for r in range(rows):
    val = start + r
    print(" ".join([str(val)]*(r+1)))
 #м
for i in range(1, 6):
    print(" ".join([str(i)]*7))
 #н
for i in range(10, 60, 10):
    print(" ".join([str(i)]*4))

 # 9.2
def addition_table(n=9):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i}+{j}={i+j}", end='\t')
        print()

addition_table()

 # 9.3
def multiplication_table(n=9):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i}*{j}={i*j}", end='\t')
        print()

multiplication_table()

 # 9.4
def sum_grades_by_rows():
    grades = []
    total = 0
    for idx in range(1, 13):
        row = list(map(int, input(f"Ученик {idx}, введите 3 оценки через пробел: ").split()))
        grades.append(row)
        total += sum(row)
    print("Сумма всех оценок:", total)
    return grades, total

def sum_grades_by_columns():
    grades = [[0]*3 for _ in range(12)]
    total = 0
    for subj in range(3):
        col = list(map(int, input(f"Предмет {subj+1}, введите 12 оценок через пробел: ").split()))
        for i in range(12):
            grades[i][subj] = col[i]
            total += col[i]
    print("Сумма всех оценок:", total)
    return grades, total

 # 9.5
def salaries_summary():
    n_workers = 12
    n_months = 3
    table = []
    for worker in range(1, n_workers+1):
        row = list(map(float, input(f"Работник {worker}, введите {n_months} зарплат (месяцы 1..3) через пробел: ").split()))
        table.append(row)

    total_all = sum(sum(row) for row in table)
    per_worker = [sum(row) for row in table]
    per_month = [sum(table[w][m] for w in range(n_workers)) for m in range(n_months)]

    print("Общая выплата за квартал всем работникам:", total_all)
    for i, s in enumerate(per_worker, 1):
        print(f"Работник {i}: квартальная зарплата = {s}")
    for m, s in enumerate(per_month, 1):
        print(f"Месяц {m}: выплачено всего = {s}")
    return table, total_all, per_worker, per_month

 # 9.6
N = 15
M = 3

print("Введите 15 строк по 3 числа (баллы) через пробел:")
data = []
for i in range(N):
    row = list(map(float, input(f"{i+1}> ").split()))
    while len(row) != M:
        print("Нужно 3 числа, попробуйте ещё раз:")
        row = list(map(float, input().split()))
    data.append(row)

for i, row in enumerate(data, start=1):
    print(f"Спортсмен {i}: средний балл = {sum(row)/M:.2f}")

for j in range(M):
    col = [row[j] for row in data]
    print(f"Программа {j+1}: средний балл = {sum(col)/N:.2f}")

 # 9.7
N = 15
M = 3

print("Введите 15 строк по 3 целых оценки (1-5) через пробел:")
data = []
for i in range(N):
    row = list(map(int, input(f"{i+1}> ").split()))
    while len(row) != M:
        print("Нужно 3 числа, попробуйте ещё раз:")
        row = list(map(int, input().split()))
    data.append(row)

 #а
total_fives = sum(1 for row in data for v in row if v == 5)
print("Общее количество пятёрок:", total_fives)

 #б
for i, row in enumerate(data, start=1):
    print(f"Ученик {i}: число двоек = {row.count(2)}")

 #в
for j in range(M):
    fives = sum(1 for row in data if row[j] == 5)
    print(f"Предмет {j+1}: пятёрок = {fives}")

 #9.8
N = 14
M = 3

print("Введите 14 строк по 3 целых оценки (1-5) через пробел:")
data = []
for i in range(N):
    row = list(map(int, input(f"{i+1}> ").split()))
    while len(row) != M:
        print("Нужно 3 числа, попробуйте ещё раз:")
        row = list(map(int, input().split()))
    data.append(row)

 #а
students_no_twos = sum(1 for row in data if 2 not in row)
print("Студентов без двоек:", students_no_twos)

 #б
subjects_all_fives = sum(1 for j in range(M) if all(row[j] == 5 for row in data))
print("Предметов, по которым только пятёрки:", subjects_all_fives)

 #в
for j in range(M):
    avg = sum(row[j] for row in data) / N
    print(f"Предмет {j+1}: средний балл = {avg:.2f}")

 # 9.9
n = 8
m = 5
print("Введите", n, "строк по", m, "оценок (через пробел):")
scores = [list(map(float, input().split())) for _ in range(n)]
max_score = max(max(row) for row in scores)
totals = [sum(row) for row in scores]
winner_points = max(totals)
print("Максимальная оценка в таблице:", max_score)
print("Баллов у победителя (макс. сумма):", winner_points)

 # 9.10
n = 12
m = 3
print("Введите", n, "строк по", m, "зарплат (через пробел):")
salaries = [list(map(float, input().split())) for _ in range(n)]
max_salary = max(max(row) for row in salaries)
worker_totals = [sum(row) for row in salaries]
best_worker = worker_totals.index(max(worker_totals)) + 1
month_totals = [sum(salaries[i][j] for i in range(n)) for j in range(m)]
best_month = month_totals.index(max(month_totals)) + 1
print("Максимальная зарплата в таблице:", max_salary)
print("Номер работника с наибольшей суммой за квартал:", best_worker)
print("Номер месяца с максимальной общей зарплатой:", best_month)

 # 9.11
data = [list(map(int, input().split())) for _ in range(12)]
for i, row in enumerate(data, start=1):
    mx = max(row)
    months = [j+1 for j, v in enumerate(row) if v == mx]
    print(f"Работник {i}: max в месяце(ах) {months}")

for m in range(3):
    col = [data[i][m] for i in range(12)]
    mx = max(col)
    workers = [i+1 for i, v in enumerate(col) if v == mx]
    print(f"Месяц {m+1}: max зарплата = {mx}, работники {workers}")

 # 9.12
tabla = [list(map(int, input().split())) for _ in range(11)]

 # a
min_class = min(min(row) for row in tabla)
print("a) Самый малочисленный класс (число учеников):", min_class)

 # b
sums_by_parallel = [sum(row) for row in tabla]
min_parallel_sum = min(sums_by_parallel)
print("b) Минимальное число учеников в параллели (сумма по строке):", min_parallel_sum)

 # c
sums_by_class_letter = [sum(tabla[i][j] for i in range(11)) for j in range(4)]
letters = ['A','Б','В','Г']
min_sum = min(sums_by_class_letter)
min_letter = letters[sums_by_class_letter.index(min_sum)]
print("c) Минимальная сумма по буквам классов:", min_sum, "для класса", min_letter)

 # 9.13
tabla = [list(map(int, input().split())) for _ in range(11)]

 # a
for i, row in enumerate(tabla, start=1):
    print(f"Параллель {i}: минимальный класс = {min(row)}")

 # b
letters = ['A','Б','В','Г']
for j, letter in enumerate(letters):
    s = sum(tabla[i][j] for i in range(11))
    avg = s / 11
    print(f"Класс {letter}: среднее число учеников = {avg:.2f}")

 # 9.14
m = [list(map(int, input().split())) for _ in range(3)]

 # а
sums = [sum(row) for row in m]
best_store = sums.index(max(sums)) + 1
print("Лучший магазин по сумме:", best_store)

 # б
day_sums = [m[0][j] + m[1][j] + m[2][j] for j in range(10)]
best_day = day_sums.index(max(day_sums)) + 1
print("Лучший день по сумме всех магазинов:", best_day)

 # в
max_val = -10**18
best_i = best_j = 0
for i in range(3):
    for j in range(10):
        if m[i][j] > max_val:
            max_val = m[i][j]
            best_i, best_j = i+1, j+1
print("Максимальный доход в день:", max_val, "магазин", best_i, "день", best_j)

 # 9.15
m = [list(map(int, input().split())) for _ in range(3)]

 # а
for i in range(3):
    day = m[i].index(max(m[i])) + 1
    print(f"Магазин {i+1}: лучший день {day}")

 # б
for j in range(10):
    best_store = 0
    best_val = -10**18
    for i in range(3):
        if m[i][j] > best_val:
            best_val = m[i][j]
            best_store = i+1
    print(f"День {j+1}: лучший магазин {best_store}")

n = int(input("Введите число курсов: "))
groups = 6

 # 9.16
a = [list(map(int, input().split())) for _ in range(n)]

 # а
for i in range(n):
    print("Курс", i+1, "всего студентов:", sum(a[i]))

 # б
min_val = 10**18
min_course = min_group = 0
for i in range(n):
    for j in range(groups):
        if a[i][j] < min_val:
            min_val = a[i][j]
            min_course, min_group = i+1, j+1
print("Минимальная группа:", "курс", min_course, "группа", min_group, "студентов", min_val)

 # в
for i in range(n):
    best_g = a[i].index(max(a[i])) + 1
    print("Курс", i+1, "самая многочисленная группа:", best_g)

from math import isqrt
from typing import List, Tuple

def build_spf(n: int) -> List[int]:
    spf = list(range(n+1))
    spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for i in range(2, isqrt(n) + 1):
        if spf[i] == i:
            step = i
            start = i * i
            for j in range(start, n+1, step):
                if spf[j] == j:
                    spf[j] = i
    return spf

def count_divisors(x: int, spf: List[int]) -> int:
    if x <= 1:
        return 1 if x == 1 else 0
    res = 1
    while x > 1:
        p = spf[x]
        if p == 1:
            # x is 1
            break
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        res *= (e + 1)
    return res

def is_prime(x: int, spf: List[int]) -> bool:
    if x < 2: return False
    return spf[x] == x

 # 9.17
def solve_9_17(prices: List[float], sales: List[List[int]], threshold_a: float = 0.0):
    m = len(prices)
    n = len(sales[0]) if sales else 0
    # a
    income_per_good = [prices[i] * sum(sales[i]) for i in range(m)]
    # b
    income_per_day = [sum(prices[i] * sales[i][j] for i in range(m)) for j in range(n)]
    # c
    total_income = sum(income_per_good)
    # d
    max_income = max(income_per_good)
    goods_with_max = [i for i,v in enumerate(income_per_good, start=1) if v == max_income]
    # e
    max_day_income = max(income_per_day)
    days_with_max = [j for j,v in enumerate(income_per_day, start=1) if v == max_day_income]
    # f
    days_above_a = sum(1 for v in income_per_day if v > threshold_a)
    return {
        'income_per_good': income_per_good,
        'income_per_day': income_per_day,
        'total_income': total_income,
        'goods_with_max': goods_with_max,
        'max_income_value': max_income,
        'days_with_max': days_with_max,
        'max_day_income': max_day_income,
        'days_above_a': days_above_a
    }

 # 9.18
def solve_9_18(groups: List[List[List[float]]]):
    averages = []
    for g in groups:
        total = 0.0
        count = 0
        for student in g:
            total += sum(student)
            count += len(student)
        avg = total / count if count else 0.0
        averages.append(avg)
    best_index = max(range(len(averages)), key=lambda i: averages[i]) if averages else None
    return {'averages': averages, 'best_group_index': (best_index + 1) if best_index is not None else None}

 # 9.20
def divisibility_graph(n: int) -> List[str]:
    if n < 1:
        return []
    spf = build_spf(n)
    lines = []
    for i in range(1, n+1):
        d = count_divisors(i, spf)
        lines.append(f"{i}" + "+" * d)
    return lines

 # (9.21 - 9.25)
def numbers_with_exactly_k_divisors_in_range(a: int, b: int, k: int) -> List[int]:
    if b < a:
        return []
    spf = build_spf(b)
    res = []
    for x in range(max(1,a), b+1):
        if count_divisors(x, spf) == k:
            res.append(x)
    return res

def numbers_with_exactly_five_divisors_1_to_300() -> List[int]:
    return numbers_with_exactly_k_divisors_in_range(1, 300, 5)

 def numbers_with_exactly_six_divisors_200_to_500() -> List[int]:
     return numbers_with_exactly_k_divisors_in_range(200, 500, 6)

 def maximize_divisors_in_interval(a: int, b: int) -> Tuple[int, List[int]]:
     if b < a:
         return (0, [])
     spf = build_spf(b)
     best = 0
     nums = []
     for x in range(max(1, a), b + 1):
         d = count_divisors(x, spf)
         if d > best:
             best = d
             nums = [x]
         elif d == best:
             nums.append(x)
     return best, nums

 def three_digit_primes() -> List[int]:
     a, b = 100, 999
     spf = build_spf(b)
     res = [x for x in range(a, b + 1) if is_prime(x, spf)]
     return res

def sum_divisors(n, proper=False):
    s = 0
    r = int(n**0.5)
    for i in range(1, r+1):
        if n % i == 0:
            j = n // i
            s += i
            if j != i:
                s += j
    if proper:
        s -= n
    return s

import math
from collections import defaultdict

def divisors(n):
    if n <= 0:
        return []
    divs = set()
    r = int(math.sqrt(n))
    for i in range(1, r+1):
        if n % i == 0:
            divs.add(i)
            divs.add(n//i)
    return sorted(divs)

def sum_divisors(n, proper=False):
    s = sum(divisors(n))
    if proper:
        return s - n
    return s

 # 9.26
def primes_first_n(n=100):
    primes = []
    x = 2
    while len(primes) < n:
        isprime = True
        r = int(math.sqrt(x))
        for p in primes:
            if p > r:
                break
            if x % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(x)
        x += 1
    return primes

 # 9.27
def sums_div_range(a, b, proper=False):
    return {i: sum_divisors(i, proper=proper) for i in range(a, b+1)}

 # 9.28
def numbers_sumdiv_eq(a, b, target):
    return [i for i in range(a, b+1) if sum_divisors(i) == target]

 # 9.29
def numbers_sumdiv_divisible(a, b, m):
    return [i for i in range(a, b+1) if sum_divisors(i) % m == 0]

 # 9.30
def three_digit_perfect():
    for i in range(100, 1000):
        if sum_divisors(i, proper=True) == i:
            return i
    return None

 # 9.31
def perfect_numbers_less_than(limit=100000):
    res = []
    for i in range(2, limit):
        if sum_divisors(i, proper=True) == i:
            res.append(i)
    return res

 # 9.32
def numbers_with_max_sumdiv(a, b):
    max_s = -1
    res = []
    for i in range(a, b+1):
        s = sum_divisors(i)
        if s > max_s:
            max_s = s
            res = [i]
        elif s == max_s:
            res.append(i)
    return res, max_s

 # 9.33
def amicable_pairs(limit=50000):
    sp = [0] * (limit+1)
    for i in range(1, limit+1):
        sp[i] = sum_divisors(i, proper=True)
    pairs = []
    for a in range(2, limit+1):
        b = sp[a]
        if b <= limit and b != a:
            if b > 0 and sum_divisors(b, proper=True) == a and a < b:
                pairs.append((a,b))
    return pairs

 # 9.34
def ways_to_pay_n(n, coins=(1,2,5,10)):
    ways = []
    c10 = n // 10
    for a10 in range(c10+1):
        rem10 = n - a10*10
        c5 = rem10 // 5
        for a5 in range(c5+1):
            rem5 = rem10 - a5*5
            c2 = rem5 // 2
            for a2 in range(c2+1):
                rem2 = rem5 - a2*2
                a1 = rem2
                ways.append({10: a10, 5: a5, 2: a2, 1: a1})
    return ways

def count_ways_to_pay_n(n, coins=(1,2,5,10)):
    return len(ways_to_pay_n(n, coins))

 # 9.35
def min_bills_binary(n, denoms=(64,32,16,8,4,2,1)):
    res = {}
    remaining = n
    count = 0
    for d in denoms:
        k = remaining // d
        res[d] = k
        count += k
        remaining -= k*d
    return count, res
 # 9.36
def rectangles(s, permutations_different=False):
    res = []
    if permutations_different:
        # a
        for a in range(1, s+1):
            if s % a == 0:
                res.append((a, s//a))
    else:
        # a <= b
        a = 1
        while a*a <= s:
            if s % a == 0:
                b = s // a
                res.append((a, b))
            a += 1
    return res

 # 9.37
def parallelepipeds(v, permutations_different=False):
    res = []
    if permutations_different:
        for a in range(1, v+1):
            if v % a != 0:
                continue
            v1 = v // a
            for b in range(1, v1+1):
                if v1 % b != 0:
                    continue
                c = v1 // b
                res.append((a, b, c))
    else:
        import math
        max_a = int(v ** (1/3)) + 2
        for a in range(1, max_a):
            if v % a != 0:
                continue
            v1 = v // a
            max_b = int(math.sqrt(v1)) + 2
            for b in range(a, max_b):
                if v1 % b != 0:
                    continue
                c = v1 // b
                if b <= c:
                    res.append((a, b, c))
    return res

 # 9.38
def pythagorean_triples(z_max):
    res = []
    for z in range(1, z_max+1):
        for x in range(1, z):
            for y in range(x, z):
                if x*x + y*y == z*z:
                    res.append((x, y, z))
    return res

 # 9.39
def sum_of_powers(m, n):
    return sum(pow(k, n) for k in range(1, m+1))

from math import gcd, isqrt
from itertools import combinations

 # 9.40
def sum_powers_self(n: int) -> int:
    return sum(pow(k, k) for k in range(1, n+1))

 # 9.41
def three_digit_with_digit_sum(n: int):
    res = []
    for x in range(100, 1000):
        if sum(map(int, str(x))) == n:
            res.append(x)
    return res

 # 9.42
def three_digit_distinct_digits():
    return [x for x in range(100, 1000) if len(set(str(x))) == 3]

 # 9.43
def gcd_list(numbers):
    if not numbers:
        return 0
    g = abs(numbers[0])
    for a in numbers[1:]:
        g = gcd(g, abs(a))
    return g

 # 9.44
WEIGHTS_944 = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]

def count_subsets_sum_w(w: int, weights=WEIGHTS_944) -> int:
    dp = {0: 1}
    for wt in weights:
        new_dp = dp.copy()
        for s, cnt in dp.items():
            ns = s + wt
            if ns <= w:
                new_dp[ns] = new_dp.get(ns, 0) + cnt
        dp = new_dp
    return dp.get(w, 0)

 # 9.45
def numbers_less_n_with_digit_sum(n: int, m: int):
    return [x for x in range(1, n) if sum(map(int, str(x))) == m]

 # 9.46
def digital_root(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return (n - 1) % 9 + 1

 # 9.47
def cattle_solutions():

    sols = []

    for b in range(0, 101):
        for c in range(0, 101 - b):
            t = 100 - b - c
            if 20*b + 10*c + t == 200:
                sols.append((b, c, t))
    return sols

 # 9.48
def prime_factorization(n: int):
    n0 = n
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3
    while f <= isqrt(n):
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2
    if n > 1:
        factors.append(n)
    return factors

def prime_factors_unique(n: int):
    return sorted(set(prime_factorization(n)))

 # 9.49
def prime_divisors(n: int):
    return prime_factors_unique(n)

 # 9.50
def coprimes_less_than_n(n: int):
    return [k for k in range(1, n) if gcd(k, n) == 1]

 # 9.51
def coprimes_less_than_n_with_m(n: int, m: int):
    return [k for k in range(1, n) if gcd(k, m) == 1]

 # 9.52
import math
def divisors_coprime(p, q):
    q_abs = abs(q)
    res = []
    for d in range(1, q_abs + 1):
        if q_abs % d == 0 and math.gcd(d, abs(p)) == 1:
            res.append(d)
    return res

 # 9.53
def smallest_taxicab(limit=200):
    sums = {}
    for a in range(1, limit+1):
        for b in range(a, limit+1):
            s = a**3 + b**3
            if s in sums:
                for (c, d) in sums[s]:
                    if (a, b) != (c, d):
                        return s, (c, d), (a, b)
                sums[s].append((a, b))
            else:
                sums[s] = [(a, b)]
    return None

print(smallest_taxicab(100))

 # 9.54
import math

def reduced_fractions(max_den=7):
    res = []
    for q in range(2, max_den + 1):
        for p in range(1, q):
            if math.gcd(p, q) == 1:
                res.append((p, q, p / q))
    res.sort(key=lambda x: x[2])
    return [(p, q) for p, q, _ in res]

print(reduced_fractions(7))



















