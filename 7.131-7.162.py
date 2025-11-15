import math
from typing import List, Tuple, Optional

 # 7.131
def task_7_131(a: List[float]) -> int:
    return sum(1 for i in range(1, len(a)) if a[i] == a[i-1])

 # 7.132
def task_7_132(a: List[float]) -> int:
    return len(set(a))

 # 7.133
def task_7_133(a: List[float]) -> int:
    return sum(1 for i in range(1, len(a)) if a[i] == a[i-1])

 # 7.134
def task_7_134(a: List[float]) -> int:
    return len(set(a))

 # 7.135
def task_7_135_max(a: List[float]) -> Optional[float]:
    return max(a) if a else None

def task_7_135_min(a: List[float]) -> Optional[float]:
    return min(a) if a else None

def task_7_135_min_max(a: List[float]) -> Tuple[Optional[float], Optional[float]]:
    if not a:
        return None, None
    mn = mx = a[0]
    for x in a[1:]:
        if x < mn: mn = x
        if x > mx: mx = x
    return mn, mx

 # 7.136
def task_7_136(results: List[float]) -> List[float]:
    bests = []
    cur_best = None
    for t in results:
        if cur_best is None or t < cur_best:
            cur_best = t
        bests.append(cur_best)
    return bests

 # 7.137
def task_7_137(distances: List[float]) -> Tuple[Optional[int], Optional[float]]:
    if not distances:
        return None, None
    mx = max(distances)
    idx = distances.index(mx) + 1
    return idx, mx

 # 7.138
def task_7_138(temps: List[float]) -> Tuple[Optional[float], List[int]]:
    if not temps:
        return None, []
    mx = max(temps)
    days = [i+1 for i, t in enumerate(temps) if t == mx]
    return mx, days

 # 7.139
def task_7_139(speeds: List[float]) -> Tuple[Optional[int], Optional[float]]:
    if not speeds:
        return None, None
    mx = max(speeds)
    idx = speeds.index(mx) + 1
    return idx, mx

 # 7.140
def task_7_140(areas: List[float]) -> Optional[float]:
    if not areas:
        return None
    min_area = min(areas)
    return math.sqrt(min_area / math.pi)

import math
from typing import List, Tuple, Optional

 # 7.140
def min_radius_from_circle_areas(areas: List[float]) -> float:
    if not areas:
        raise ValueError("Список площадей пуст.")
    return min(math.sqrt(a / math.pi) for a in areas)

 # 7.141
def max_diagonal_from_square_areas(areas: List[float]) -> float:
    if not areas:
        raise ValueError("Список площадей пуст.")
    return max(math.sqrt(2 * a) for a in areas)

 # 7.142
def max_density(masses: List[float], volumes: List[float]) -> float:
    if len(masses) != len(volumes):
        raise ValueError("Длины списков масс и объемов должны совпадать.")
    if not masses:
        raise ValueError("Пустые списки.")
    densities = []
    for m, v in zip(masses, volumes):
        if v == 0:
            raise ValueError("Объем не должен быть равен нулю.")
        densities.append(m / v)
    return max(densities)

 # 7.143
def min_population_density(populations: List[float], areas: List[float]) -> Tuple[int, float]:
    if len(populations) != len(areas):
        raise ValueError("Длины списков населения и площадей должны совпадать.")
    if not populations:
        raise ValueError("Пустой список.")
    densities = []
    for p, a in zip(populations, areas):
        if a == 0:
            raise ValueError("Площадь не должна быть равна нулю.")
        densities.append(p / a)
    min_idx = int(min(range(len(densities)), key=lambda i: densities[i]))
    return min_idx, densities[min_idx]

 # 7.144
def max_sum_and_min_product(pairs: List[Tuple[float, float]]) -> Tuple[float, float]:
    if not pairs:
        raise ValueError("Список пар пуст.")
    sums = [a + b for a, b in pairs]
    prods = [a * b for a, b in pairs]
    return max(sums), min(prods)

 # 7.145
def judge_score(scores: List[float]) -> Optional[float]:
    n = len(scores)
    if n <= 2:
        return None
    s = sorted(scores)
    remaining = s[1:-1]
    return sum(remaining) / len(remaining)

from typing import Iterable, Sequence, Tuple, Optional, Any

 # 7.146
def solve_7_146(heights: Sequence[float]) -> float:
    if not heights:
        raise ValueError("Список пуст")
    return max(heights) - min(heights)

 # 7.147
def solve_7_147(class_sizes: Sequence[int]) -> int:
    if not class_sizes:
        raise ValueError("Список пуст")
    return max(class_sizes) - min(class_sizes)

 # 7.148
def solve_7_148(a: Sequence[int]) -> bool:
    if not a:
        raise ValueError("Список пуст")
    return (max(a) - min(a)) <= 25

 # 7.149
def solve_7_149(masses: Sequence[float]) -> bool:
    if not masses:
        raise ValueError("Список пуст")
    mn = min(masses)
    mx = max(masses)
    if mn <= 0:
        return mx == 0
    return mx <= 2 * mn

 # 7.150
def solve_7_150(a: Sequence[int]) -> int:
    best = cur = 0
    for x in a:
        if x % 2 == 0:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return best

 # 7.151
def solve_7_151(bits: Sequence[int]) -> int:
    best = cur = 0
    for b in bits:
        if b == 0:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return best

 # 7.152
def solve_7_152(seq: Sequence[float], x: float) -> Tuple[int, float]:
    if not seq:
        raise ValueError("Список пуст")
    best_idx = 0
    best_dist = abs(seq[0] - x)
    for i, val in enumerate(seq):
        d = abs(val - x)
        if d < best_dist:
            best_dist = d
            best_idx = i
    return best_idx + 1, seq[best_idx]

 # 7.153
def solve_7_153(a: Sequence[int]) -> Optional[int]:
    evens = [x for x in a if x % 2 == 0]
    return max(evens) if evens else None

 # 7.154
def solve_7_154(a: Sequence[Any]) -> int:
    if not a:
        return 0
    best = cur = 1
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1
    return best

 # 7.155
def solve_7_155(a: Sequence[float]) -> int:
    if not a:
        return 0
    best = cur = 1
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1
    return best

 # 7.156
def longest_monotonic_stream(iterable):
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        raise ValueError("Пустая последовательность")
    maxlen = 1
    cur_len = 1
    trend = 0
    for x in it:
        if trend == 0:
            if x > prev:
                trend = 1
                cur_len += 1
            elif x < prev:
                trend = -1
                cur_len += 1
        else:
            if trend == 1:
                if x > prev:
                    cur_len += 1
                else:
                    trend = -1
                    cur_len = 2
            else:
                if x < prev:
                    cur_len += 1
                else:
                    trend = 1
                    cur_len = 2
        if cur_len > maxlen:
            maxlen = cur_len
        prev = x
    return maxlen

def longest_monotonic_list(a):
    if not a:
        raise ValueError("Пустая последовательность")
    n = len(a)
    if n == 1:
        return 1
    maxlen = 1
    cur_len = 1
    trend = 0
    for i in range(1, n):
        if trend == 0:
            if a[i] > a[i-1]:
                trend = 1
                cur_len += 1
            elif a[i] < a[i-1]:
                trend = -1
                cur_len += 1
        else:
            if trend == 1:
                if a[i] > a[i-1]:
                    cur_len += 1
                else:
                    trend = -1
                    cur_len = 2
            else:
                if a[i] < a[i-1]:
                    cur_len += 1
                else:
                    trend = 1
                    cur_len = 2
        if cur_len > maxlen:
            maxlen = cur_len
    return maxlen

 # 7.157
def task_7_157(a):
    if not a:
        raise ValueError("Пустая последовательность")
    max_val = a[0]
    idx_max = 1
    min_val = a[0]
    idx_min = 1
    for i, v in enumerate(a, start=1):
        if v >= max_val:
            max_val = v
            idx_max = i
        if v < min_val:
            min_val = v
            idx_min = i
    return idx_max, idx_min

# 7.158
def task_7_158(d):
    if not d:
        raise ValueError("Пустая последовательность")
    max_val = d[0]
    idx_max = 1
    min_val = d[0]
    idx_min = 1
    for i, v in enumerate(d, start=1):
        if v >= max_val:
            max_val = v
            idx_max = i
        if v <= min_val:
            min_val = v
            idx_min = i
    return idx_max, idx_min

# 7.159
def task_7_159(residents):
    if not residents:
        raise ValueError("Пустая последовательность")
    max_val = residents[0]
    idx = 1
    for i, v in enumerate(residents, start=1):
        if v >= max_val:
            max_val = v
            idx = i
    return idx

# 7.160
def task_7_160(times):
    if not times:
        raise ValueError("Пустая последовательность")
    best = times[0]
    idx = 1
    for i, t in enumerate(times, start=1):
        if t <= best:
            best = t
            idx = i
    return idx

# 7.161
def task_7_161(points):
    if not points:
        raise ValueError("Пустая последовательность")
    minv = points[0]
    idx = 1
    for i, p in enumerate(points, start=1):
        if p < minv:
            minv = p
            idx = i
    return idx

# 7.162
def task_7_162(precip):
    if not precip:
        raise ValueError("Пустая последовательность")
    maxv = precip[0]
    idx = 1
    for i, v in enumerate(precip, start=1):
        if v >= maxv:
            maxv = v
            idx = i
    return idx













































