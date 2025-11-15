from math import sqrt
from typing import List, Tuple

 # 7.162
def max_precip_day(precip: List[float]) -> int:
    if not precip:
        raise ValueError("список пуст")
    mx = max(precip)
    for i in range(len(precip)-1, -1, -1):
        if precip[i] == mx:
            return i+1

 # 7.163
def queue_times(t: List[float]) -> Tuple[List[float], int]:
    if not t:
        return [[], None]
    c = []
    s = 0.0
    for ti in t:
        s += ti
        c.append(s)
    min_t = min(t)
    for i in range(len(t)-1, -1, -1):
        if t[i] == min_t:
            return c, i+1

 # 7.164
def pair_means(pairs: List[Tuple[float, float]]) -> Tuple[int, int]:
    if not pairs:
        raise ValueError("список пуст")
    arith_means = [(a+b)/2.0 for a,b in pairs]
    geom_means = [sqrt(a*b) for a,b in pairs]
    max_ar = max(arith_means)
    idx_max_ar = None
    for i in range(len(arith_means)-1, -1, -1):
        if arith_means[i] == max_ar:
            idx_max_ar = i+1
            break
    min_geom = min(geom_means)
    idx_min_geom = None
    for i in range(len(geom_means)):
        if geom_means[i] == min_geom:
            idx_min_geom = i+1
            break
    return idx_max_ar, idx_min_geom

 # 7.165
def max_average_speed(distances: List[float], times: List[float]) -> int:
    if len(distances) != len(times) or not distances:
        raise ValueError("некорректные входные данные")
    best_idx = 0
    best_speed = None
    for i, (d, t) in enumerate(zip(distances, times)):
        if t == 0:
            raise ValueError(f"время для автомобиля {i+1} равно нулю")
        v = d / t
        if best_speed is None or v > best_speed:
            best_speed = v
            best_idx = i
    return best_idx + 1

 # 7.166
def min_current_index(voltages: List[float], resistances: List[float]) -> int:
    if len(voltages) != len(resistances) or not voltages:
        raise ValueError("некорректные входные данные")
    min_idx = 0
    min_I = None
    for i, (U, R) in enumerate(zip(voltages, resistances)):
        if R == 0:
            raise ValueError(f"сопротивление {i+1} равно нулю")
        I = U / R
        if min_I is None or I < min_I:
            min_I = I
            min_idx = i
    return min_idx + 1

 # 7.167
def first_of_max_or_min(xs: List[int]) -> Tuple[str, int]:
    if not xs:
        raise ValueError("список пуст")
    mx = max(xs)
    mn = min(xs)
    first_mx = xs.index(mx) + 1
    first_mn = xs.index(mn) + 1
    if first_mx < first_mn:
        return "max", first_mx
    else:
        return "min", first_mn

from typing import List, Tuple
import math
import heapq

 # 7.168
def who_earlier_oldest_or_youngest(ages: List[int]) -> Tuple[str, int]:
    if not ages:
        raise ValueError("Список пуст")
    max_age = max(ages)
    min_age = min(ages)
    idx_max = ages.index(max_age) + 1
    idx_min = ages.index(min_age) + 1
    if idx_max < idx_min:
        return ("старший", idx_max)
    else:
        return ("младший", idx_min)

 # 7.169
def won_before_last_stage(times: List[float]) -> bool:
    if not times:
        raise ValueError("Пустой список")
    i_min = times.index(min(times))
    i_max = times.index(max(times))
    return i_min < i_max

 # 7.170
def adjacent_sums_info(nums: List[int]) -> Tuple[int, int, Tuple[int,int], Tuple[int,int]]:
    n = len(nums)
    if n < 2:
        raise ValueError("Нужно как минимум 2 числа")
    max_sum = -math.inf
    min_sum = math.inf
    max_pos = (1,2)
    min_pos = (1,2)
    for i in range(n - 1):
        s = nums[i] + nums[i+1]
        if s > max_sum:
            max_sum = s
            max_pos = (i+1, i+2)
        if s <= min_sum:
            min_sum = s
            min_pos = (i+1, i+2)
    return max_sum, min_sum, max_pos, min_pos

 # 7.171
def two_largest_and_two_smallest(nums: List[int]) -> Tuple[Tuple[int,int], Tuple[int,int]]:
    if len(nums) < 2:
        raise ValueError("Нужно как минимум 2 числа")
    max1, max2 = heapq.nlargest(2, nums)
    min1, min2 = heapq.nsmallest(2, nums)
    return (max1, max2), (min1, min2)

 # 7.172
def first_and_second_place(times: List[float]) -> Tuple[Tuple[float,int], Tuple[float,int]]:
    n = len(times)
    if n < 2:
        raise ValueError("Нужно как минимум 2 результата")
    best = math.inf
    second = math.inf
    idx_best = -1
    idx_second = -1
    for i, t in enumerate(times):
        if t < best:
            second, idx_second = best, idx_best
            best, idx_best = t, i + 1
        elif t < second:
            second, idx_second = t, i + 1
    return (best, idx_best), (second, idx_second)

 # 7.173
def fastest_car(speeds: List[float]) -> Tuple[float, int]:
    if not speeds:
        raise ValueError("Список пуст")
    max_speed = max(speeds)
    idx = speeds.index(max_speed) + 1
    return max_speed, idx

import sys

def read_nums(count=None, typ=float):
    tokens = []
    while count is None or len(tokens) < count:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue
        parts = line.split()
        for p in parts:
            try:
                tokens.append(typ(p))
            except:
                pass
            if count is not None and len(tokens) >= count:
                break
    return tokens

 # 7.174
def task_7174():
    print("Введите 12 целых чисел — очки 12 команд (в любую разбивку строк):")
    pts = read_nums(12, int)
    if len(pts) < 12:
        print("Недостаточно данных.")
        return
    top3 = sorted(pts, reverse=True)[:3]

 # 7.175
def task_7175():
    print("Введите n (n >= 4):")
    nums = read_nums(1, int)
    if not nums:
        print("Нет n.")
        return
    n = nums[0]
    if n < 4:
        print("n должно быть >= 4")
        return
    print(f"Введите {n} результатов (числа, например 10.23 или 1023 если в сотых долях):")
    vals = read_nums(n, float)
    if len(vals) < n:
        print("Недостаточно данных.")
        return
    indexed = list(enumerate(vals, start=1))
    indexed.sort(key=lambda x: (x[1], x[0]))
    chosen = sorted([idx for idx, v in indexed[:4]])
    print("Индексы четырёх выбранных бегунов (i<j<k<m):")
    print(*chosen)

 # 7.176
def task_7176():
    print("Введите количество дней (обычно 31 для июля). Если не уверены — введи количество:")
    days = read_nums(1, int)
    if not days:
        print("Нет данных.")
        return
    d = days[0]
    print(f"Введите {d} средних температур (по дням):")
    temps = read_nums(d, float)
    if len(temps) < d:
        print("Недостаточно данных.")
        return
    indexed = list(enumerate(temps, start=1))
    indexed.sort(key=lambda x: (x[1], x[0]))
    two = [indexed[0][0], indexed[1][0]]
    two.sort()
    print("Даты двух самых прохладных дней (дни месяца, 1-based):")
    print(*two)

 # 7.177
def task_7177():
    print("Ответы для 7.177:")
    print("При A = 0: 4")
    print("При A = 8: 4")

 # 7.178
def task_7178():
    print("Введите 12 целых чисел s1..s12 (в одну или несколько строк):")
    s = read_nums(12, int)
    if len(s) < 12:
        print("Недостаточно данных.")
        return
    mx = max(s)
    mn = min(s)
    print("Сколько раз встречается максимальное значение, потом минимальное:")
    print(s.count(mx))
    print(s.count(mn))

 # 7.179
def task_7179():
    print("Введите количество квартир n:")
    nlist = read_nums(1, int)
    if not nlist:
        print("Недостаточно данных.")
        return
    n = nlist[0]
    if n <= 0:
        print("n должно быть > 0")
        return
    print(f"Введите {n} целых чисел — количество людей в каждой квартире (№1..№{n}):")
    a = read_nums(n, int)
    if len(a) < n:
        print("Недостаточно данных.")
        return
    mx = max(a)
    indices = [i+1 for i, val in enumerate(a) if val == mx]
    print("Квартиры с наибольшим числом жильцов (номера 1-based):")
    print(*indices)

 # 7.180
def task_7180():
    print("Введите количество дней в месяце m:")
    mlist = read_nums(1, int)
    if not mlist:
        print("Нет данных.")
        return
    m = mlist[0]
    if m <= 0:
        print("m должно быть > 0")
        return
    print(f"Введите {m} значений температур:")
    temps = read_nums(m, float)
    if len(temps) < m:
        print("Недостаточно данных.")
        return
    mn = min(temps)
    cnt = sum(1 for t in temps if t == mn)
    print("Сколько дней была самая низкая температура:")
    print(cnt)

 # 7.181
def valid_tiles(seq):
    i = 0
    n = len(seq)
    while i < n:
        x = seq[i]
        if not (0 <= x <= 66):
            return False
        a = x // 10
        b = x % 10
        if not (0 <= a <= 6 and 0 <= b <= 6):
            return False
        i += 1
    return True

def chain_fixed_orientation(seq):
    if not valid_tiles(seq):
        return False
    n = len(seq)
    i = 0
    while i < n - 1:
        right_i = seq[i] % 10
        left_next = seq[i+1] // 10
        if right_i != left_next:
            return False
        i += 1
    return True

def chain_flexible_orientation(seq):
    if not valid_tiles(seq):
        return False
    n = len(seq)
    if n == 0:
        return True
    starts = set()
    first = seq[0]
    starts.add(first % 10)
    starts.add(first // 10)
    for start_right in starts:
        ok = True
        current_right = start_right
        i = 1
        while i < n:
            a = seq[i] // 10
            b = seq[i] % 10
            if a == current_right:
                current_right = b
            elif b == current_right:
                current_right = a
            else:
                ok = False
                break
            i += 1
        if ok:
            return True
    return False













































