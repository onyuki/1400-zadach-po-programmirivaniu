 # 8.1
def squares_le(n):
    k = 1
    while k * k <= n:
        print(k * k)
        k += 1

 # 8.2
 # Вариант 1
def first_square_gt_while(n):
    k = 1
    while k * k <= n:
        k += 1
    return k * k

 # Вариант 2:
def first_square_gt_break(n):
    k = 1
    while True:
        val = k * k
        if val > n:
            return val
        k += 1

 # 8.3
import math
def reciprocals_ge(a):
    if not (0 < a < 1):
        raise ValueError("Ожидается 0 < a < 1")
    max_k = int(math.floor(1.0 / a))
    for k in range(1, max_k + 1):
        print(1.0 / k)

 # 8.4
def first_reciprocal_lt(a):
    if not (0 < a < 1):
        raise ValueError("Ожидается 0 < a < 1")
    import math
    k = int(math.floor(1.0 / a)) + 1
    return k, 1.0 / k

 # 8.5
def first_harmonic_ge(a, start_n=1, max_iter=100000):
    if not (1 < a < 1.5):
        pass
    s = 0.0
    for n in range(1, max_iter + 1):
        s += 1.0 / n
        if n >= start_n and s >= a:
            return n, s
    return None

def print_harmonics_ge(a, max_n):
    s = 0.0
    for n in range(1, max_n + 1):
        s += 1.0 / n
        if s >= a:
            print(n, s)

 # 8.6
def harmonics_le(a, max_iter=100000):
    s = 0.0
    res_n = 0
    for n in range(1, max_iter + 1):
        s += 1.0 / n
        if s <= a:
            print(n, s)
            res_n = n
        else:
            break
    return res_n

 # 8.7
def first_harmonic_lt(a, start_n=1, max_iter=100000):
    s = 0.0
    for n in range(1, max_iter + 1):
        s += 1.0 / n
        if n >= start_n and s < a:
            return n, s
    return None

 # 8.8
def first_index_all_ge(a, max_iter=100000):
    return first_harmonic_ge(a, start_n=1, max_iter=max_iter)

import math

 # 8.9
def solve_8_9(a):
    n = 2
    while 1 + 1.0/n >= a:
        n += 1
    return n

 # 8.10
def solve_8_10(a):
    res = []
    if 1.0 < a:
        res.append(1.0)
    n = 2
    while True:
        val = 1.0 + 1.0/n
        if val < a:
            res.append(val)
            n += 1
        else:
            break
    return res

 # 8.11
def solve_8_11(n_val, max_iter=10**7):
    if 1.0 > n_val:
        return 1.0, 1
    k = 2
    while k <= max_iter:
        val = 1.0 + 1.0/k
        if val > n_val:
            return val, k
        k += 1
    raise ValueError("Не найдено в пределах max_iter")

 # 8.12
def solve_8_12(a, max_n=None):
    s = 0.0
    res = []
    n = 1
    if max_n is None:
        while True:
            s += 1.0/n
            if s > a:
                return {"first_n": n, "note": "для всех n >= first_n неравенство выполняется"}
            n += 1
    else:
        while n <= max_n:
            s += 1.0/n
            if s > a:
                res.append(n)
            n += 1
        return res

 # 8.13
def solve_8_13(a):
    s = 0.0
    n = 1
    while True:
        s += 1.0/n
        if s > a:
            return n
        n += 1

 # 8.14
def solve_8_14(a):
    k = 1
    while True:
        val = 1.0/k
        if val < a:
            return val, k
        k += 1

 # 8.15
def solve_8_15(m):
    res = []
    for x in range(1, 101):
        y = (x*x + 100.0) / (x + 200.0)
        if y < m:
            res.append((x, y))
    return res

 # 8.16
def solve_8_16(m):
    if not (0.5 < m < 1.0):
        raise ValueError("m должно быть в (0.5,1)")
    k_max = int(math.floor(m / (1.0 - m)))
    res = []
    for k in range(1, k_max + 1):
        res.append((k, k / (k + 1.0)))
    return res

 # 8.17
def problem_8_17(eps=0.001, max_iter=10000):
    p_prev2, p_prev1 = 1, 2  # p1, p2
    q_prev2, q_prev1 = 1, 1  # q1, q2
    a_prev2 = p_prev2 / q_prev2
    a_prev1 = p_prev1 / q_prev1
    if abs(a_prev1 - a_prev2) <= eps:
        return 2, a_prev1, a_prev2, abs(a_prev1 - a_prev2)
    for n in range(3, max_iter + 1):
        p = p_prev1 + p_prev2
        q = q_prev1 + q_prev2
        a = p / q
        diff = abs(a - a_prev1)
        if diff <= eps:
            return n, a, a_prev1, diff
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
        a_prev2, a_prev1 = a_prev1, a
    raise RuntimeError(f"Не найден член с точностью {eps} за {max_iter} итераций")

 # 8.18
def problem_8_18(a, x, eps, max_iter=100000):
    if a <= 0 or x <= 0 or eps <= 0:
        raise ValueError("a, x, eps должны быть положительными")
    y = a
    for n in range(1, max_iter + 1):
        y = 0.5 * (y + x / y)
        err = abs(y * y - x)
        if err < eps:
            return n, y, err
    raise RuntimeError(f"Не достигнута требуемая точность {eps} за {max_iter} итераций")

 # 8.19
def problem_8_19_sum_upto(limit=1000):
    if limit < 1:
        return 0, []
    fibs = [1, 1]
    while True:
        nxt = fibs[-1] + fibs[-2]
        if nxt > limit:
            break
        fibs.append(nxt)
    return sum(fibs), fibs

def problem_8_19_first_greater(n):
    if n < 1:
        return 1, 1
    f1, f2 = 1, 1
    idx = 2
    if f1 > n:
        return f1, 1
    if f2 > n:
        return f2, 2
    while True:
        f3 = f1 + f2
        idx += 1
        if f3 > n:
            return f3, idx
        f1, f2 = f2, f3









































