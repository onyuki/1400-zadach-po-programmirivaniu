 # 5.44
def fib_n(n):
    if n <= 0:
        raise ValueError("n должно быть положительным")
    a, b = 1, 1
    if n == 1:
        return a
    if n == 2:
        return b
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def fib_sequence(n):
    if n <= 0:
        return []
    seq = [1, 1]
    if n == 1:
        return [1]
    for i in range(3, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

 # 5.46
def frac_sequence(n):
    if n <= 0:
        return []
    nums = [1, 2]
    dens = [1, 1]
    if n == 1:
        return [(1, 1)]
    for i in range(3, n + 1):
        nums.append(nums[-1] + nums[-2])
        dens.append(dens[-1] + dens[-2])
    return list(zip(nums[:n], dens[:n]))

 # 5.47
def v_n(n):
    if n <= 0:
        raise ValueError("n должно быть положительным")
    if n == 1 or n == 2:
        return 0.0
    if n == 3:
        return 1.5
    v = [None, 0.0, 0.0, 1.5]
    for i in range(4, n + 1):
        vi = ( (i - 1) / (i**2 + 1) ) * v[i-1] - v[i-2] + v[i-3]
        v.append(vi)
    return v[n]

 # 5.48
def amoeba_cells_after(hours, initial=1):

    if hours < 0 or hours % 3 != 0:
        raise ValueError("hours должно быть >=0 и кратно 3")
    return initial * 2**(hours // 3)

 # 5.49
def bank_amount(principal, months, monthly_rate=0.02):
    return principal * (1 + monthly_rate) ** months

 # 5.50
def task_5_50():
    first = 10.0
    rate = 1.10
    # a)
    d = first
    prints = []
    for day in range(2, 11):
        d = d * rate
        prints.append((day, d))
    # b)
    total7 = 0.0
    d = first
    for day in range(1, 8):
        total7 += d
        d *= rate
    return prints, total7

 # 5.51
def task_5_51():
    area0 = 100.0
    yield0 = 20.0
    area = area0
    yld = yield0
    area_list = {1: area}
    yld_list = {1: yld}
    for year in range(2, 9):
        area *= 1.05
        yld *= 1.02
        area_list[year] = area
        yld_list[year] = yld
    # a)
    yields_2_8 = [(year, yld_list[year]) for year in range(2, 9)]
    # b)
    areas_3_5_7 = [(year, area_list[year]) for year in (3,5,7)]
    # c)
    total_centners = sum(area_list[year] * yld_list[year] for year in range(1, 7))
    total_tonnes = total_centners / 10.0  # 1 тонна = 10 центнеров
    return yields_2_8, areas_3_5_7, total_centners, total_tonnes

 # 5.53
def task_5_53(n):
    s = 0
    for k in range(1, n+1):
        s += 4**k
    s_formula = 4 * (4**n - 1) // 3 if isinstance(n, int) else 4*(4**n - 1)/3
    return s, s_formula

 # 5.54
def powers_without_pow(a, n):
    res = []
    cur = 1.0
    for i in range(1, n+1):
        cur = cur * a if i == 1 else cur * a
        if i == 1:
            cur = a
        else:
            cur = cur * a
        res.append(cur)
    return res

def powers_without_pow2(a, n):
    res = []
    cur = a
    for i in range(1, n+1):
        if i == 1:
            res.append(cur)
        else:
            cur = cur * a
            res.append(cur)
    return res

 # 5.55
def task_5_55(n):
    s = 0
    for k in range(1, n+1):
        term = ((-1) ** (k - 1)) * (k ** 2)
        s += term
    return s

for n in (1, 2, 3, 4, 5, 10):
        print(f"5.55 n={n}: S = {task_5_55(n)}")

#для задач ниже import math
import math

 # 5.64.
def reverse_digits(number: int) -> int:
    s = str(number)
    if s[0] == '-':
        return -int(s[:0:-1])
    return int(s[::-1])

 # 5.65
def square_by_odds(n: int) -> int:
    return sum(2*k - 1 for k in range(1, n+1))

 # 5.66
def sum_squares_1_to_12() -> int:
    total = 0
    square = 0
    for n in range(1, 13):
        square += 2*n - 1
        total += square
    return total

 # 5.67
def cube_by_consecutive_odds(n: int) -> int:
    start = n*n - n + 1
    return sum(start + 2*k for k in range(n))

 # 5.68
def sum_factorials(n: int) -> int:
    total = 0
    fact = 1
    for k in range(1, n+1):
        fact *= k
        total += fact
    return total

 # 5.69
def harmonic_sum(n: int) -> float:
    return sum(1.0 / k for k in range(1, n+1))

 # 5.70
def sum_inverse_factorials(n: int) -> float:
    total = 0.0
    fact = 1
    for k in range(1, n+1):
        fact *= k
        total += 1.0 / fact
    return total

 # 5.71
def sum_square_roots_upto_50() -> float:
    return sum(math.sqrt(k) for k in range(1, 51))










































