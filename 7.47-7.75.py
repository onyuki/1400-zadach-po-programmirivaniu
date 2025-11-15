from typing import List

 # 7.47
def sum_priced_over(prices: List[float], threshold: float = 1000.0) -> float:
    return sum(p for p in prices if p > threshold)

 # 7.48
def sum_magazine_pages(pages: List[int], newspaper_max: int = 16) -> int:
    return sum(p for p in pages if p > newspaper_max)

 # 7.49
def sum_even_days(rainfall: List[float]) -> float:
    return sum(rainfall[i] for i in range(1, len(rainfall), 2))

 # 7.50
def sum_in_odd_classes(counts: List[int]) -> int:
    return sum(counts[i] for i in range(0, len(counts), 2))

 # 7.51
def sum_initial_odds(seq: List[int]) -> int:
    s = 0
    for x in seq:
        if x % 2 != 0:
            s += x
        else:
            break
    return s

 # 7.52
def check_b52(bs: List[int]) -> (bool, bool):
    s_gt20 = sum(x for x in bs if x > 20)
    s_lt50 = sum(x for x in bs if x < 50)
    return (s_gt20 > 100, s_lt50 % 2 == 0)

 # 7.53
def check_b53(ms: List[int]) -> (bool, bool):
    s_lt_25_5 = sum(x for x in ms if x < 25.5)
    s_le_20 = sum(x for x in ms if x <= 20)
    return (s_lt_25_5 <= 50, s_le_20 % 3 == 0)

 # 7.54
def check_b54(ds: List[float], p: float) -> bool:
    return sum(x for x in ds if x > 20.5) < p

 # 7.55
def check_b55(as_list: List[int], t: int, q: int) -> bool:
    return sum(x for x in as_list if x <= t) <= q

 # 7.56
def check_b56(cs: List[int], m: int, p: int) -> bool:
    if p == 0:
        raise ValueError("p (делитель) не должен быть равен 0")
    return sum(x for x in cs if x <= m) % p == 0

from typing import List, Tuple

 # 7.57
def more_precip_on_even_days(precip: List[float]) -> bool:
    sum_odd = 0.0
    sum_even = 0.0
    for i, v in enumerate(precip):
        if (i + 1) % 2 == 0:
            sum_even += v
        else:
            sum_odd += v
    return sum_even > sum_odd

 # 7.58
def which_side_more_residents(residents: List[int]) -> str:
    sum_odd = 0
    sum_even = 0
    for i, v in enumerate(residents):
        if (i + 1) % 2 == 0:
            sum_even += v
        else:
            sum_odd += v
    if sum_odd > sum_even:
        return 'odd'
    if sum_even > sum_odd:
        return 'even'
    return 'equal'

 # 7.59
def count_fives(grades: List[int]) -> int:
    cnt = 0
    for g in grades:
        if g == 5:
            cnt += 1
    return cnt

 # 7.60
def count_below_zero(temps: List[float]) -> int:
    cnt = 0
    for t in temps:
        if t < 0:
            cnt += 1
    return cnt

 # 7.61
def count_height_less_than_165(heights: List[float]) -> int:
    cnt = 0
    for h in heights:
        if h < 165:
            cnt += 1
    return cnt

 # 7.62
def stats_vs_p_and_k(arr: List[int], p: int, k: int) -> Tuple[int, int, int]:
    greater_p = 0
    ending_5 = 0
    divisible_k = 0
    for a in arr:
        if a > p:
            greater_p += 1
        if abs(a) % 10 == 5:
            ending_5 += 1
        if k != 0 and a % k == 0:
            divisible_k += 1
    return greater_p, ending_5, divisible_k

 # 7.63
def count_5_and_2(chem_grades: List[int]) -> Tuple[int, int]:
    cnt5 = 0
    cnt2 = 0
    for g in chem_grades:
        if g == 5:
            cnt5 += 1
        elif g == 2:
            cnt2 += 1
    return cnt5, cnt2

 # 7.64
def count_birth_years(years: List[int]) -> Tuple[int, int]:
    before_1990 = 0
    after_2000 = 0
    for y in years:
        if y < 1990:
            before_1990 += 1
        if y > 2000:
            after_2000 += 1
    return before_1990, after_2000

 # 7.65
def count_teams_more_wins(records: List[Tuple[int, int]]) -> int:
    cnt = 0
    for wins, losses in records:
        if wins > losses:
            cnt += 1
    return cnt

 # 7.66
def count_initial_negative_numbers(seq: List[float]) -> int:
    cnt = 0
    for x in seq:
        if x < 0:
            cnt += 1
        else:
            break
    return cnt

 # 7.67
def count_before_first_zero(seq: List[float]) -> int:
        cnt = 0
        for x in seq:
            if x == 0:
                break
            cnt += 1
        return cnt

 # 7.68
def count_initial_equal_elements(seq: List[int]) -> int:
        if not seq:
            return 0
        first = seq[0]
        cnt = 0
        for x in seq:
            if x == first:
                cnt += 1
            else:
                break
        return cnt

import math

 # 7.69
def count_fives_prefix(grades, case2=False):
    n = len(grades)
    i = 0
    while i < n and grades[i] == 5:
        i += 1
    return i

 # 7.70
def count_initial_no_rain(rains, case2=False):
    n = len(rains)
    i = 0
    while i < n and rains[i] == 0:
        i += 1
    return i

 # 7.72
def count_pos_neg(a):
    pos = 0
    neg = 0
    for x in a:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
    return pos, neg

 # 7.73
def count_multiples(xs):
    cnt3 = 0
    cnt7 = 0
    for x in xs:
        if x % 3 == 0:
            cnt3 += 1
        if x % 7 == 0:
            cnt7 += 1
    return cnt3, cnt7

 # 7.74
def count_triangles(triples):
    cnt = 0
    for a, b, c in triples:
        if a + b > c:
            cnt += 1
    return cnt

 # 7.75
def percent_hits(pairs, R, H, P, g=9.8):
    hits = 0
    total = len(pairs)
    for alpha_deg, v0 in pairs:
        alpha = math.radians(alpha_deg)
        cos_a = math.cos(alpha)
        if v0 * cos_a == 0:
            continue
        t = R / (v0 * cos_a)
        if t < 0:
            continue
        y = v0 * t * math.sin(alpha) - 0.5 * g * t * t
        if H <= y <= H + P:
            hits += 1
    return (hits / total * 100) if total > 0 else 0.0








































