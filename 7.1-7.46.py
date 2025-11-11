from typing import List, Tuple, Iterable

 # 7.1
def sum_10(a: List[float]) -> float:
    if len(a) != 10:
        raise ValueError("Ожидается список длины 10")
    return sum(a)

 # 7.2
def sum_n(a: List[float]) -> float:
    return sum(a)

 # 7.3
def perimeter_12(sides: List[float]) -> float:
    if len(sides) != 12:
        raise ValueError("Ожидается список из 12 сторон")
    return sum(sides)

 # 7.4
def total_mass(masses: List[float]) -> float:
    return sum(masses)

 # 7.5
def total_payroll(salaries: List[float]) -> float:
    return sum(salaries)

 # 7.6
def resistance_series(resistances: List[float]) -> float:
    return sum(resistances)

 # 7.7
def resistance_parallel(resistances: List[float]) -> float:
    if any(r == 0 for r in resistances):
        return 0.0
    recip = sum(1.0 / r for r in resistances)
    if recip == 0:
        raise ValueError("Сумма обратных сопротивлений равна нулю")
    return 1.0 / recip

 # 7.8
def seq_sum_and_count_terminated_by_zero(seq: List[int]) -> Tuple[int, int]:
    if not seq:
        raise ValueError("Последовательность пуста")
    try:
        idx = seq.index(0)
        data = seq[:idx]
    except ValueError:
        data = seq
    return sum(data), len(data)

 # 7.9
def students_scores_sum(scores1: List[int], scores2: List[int]) -> Tuple[int, int]:
    if len(scores1) != 4 or len(scores2) != 4:
        raise ValueError("Ожидаются по 4 оценки для каждого ученика")
    return sum(scores1), sum(scores2)

 # 7.10
def pentathlon_sums(athlete1: List[float], athlete2: List[float]) -> Tuple[float, float]:
    if len(athlete1) != 5 or len(athlete2) != 5:
        raise ValueError("Ожидаются по 5 результатов для каждого спортсмена")
    return sum(athlete1), sum(athlete2)

 # 7.11
def product_n(a: Iterable[float]) -> float:
    prod = 1.0
    had = False
    for x in a:
        had = True
        prod *= x
    if not had:
        return 0.0
    return prod

 # 7.12
def prefix_sums_terminated_by_zero(seq: List[int]) -> List[int]:
    if not seq:
        raise ValueError("Пустая последовательность")
    try:
        idx = seq.index(0)
        data = seq[:idx]
    except ValueError:
        data = seq
    res = []
    acc = 0
    for x in data:
        acc += x
        res.append(acc)
    return res

 # 7.13
def sum_of_squares_10(a: List[float]) -> float:
    if len(a) != 10:
        raise ValueError("Ожидается список длины 10")
    return sum(x*x for x in a)

 # 7.14
def sum_of_squares_n(a: List[float]) -> float:
    return sum(x*x for x in a)

 # 7.15
def sum_exceeds_100_78(a: List[float]) -> bool:
    return sum(a) > 100.78

 # 7.16
def is_sum_negative(b: List[int]) -> bool:
    return sum(b) < 0

 # 7.17
def is_sum_even(a: List[int]) -> bool:
    return (sum(a) % 2) == 0

 # 7.18
def is_sum_divisible_by_b(x: List[int], b: int) -> bool:
    if b == 0:
        raise ValueError("Деление на ноль: b не должно быть 0")
    return sum(x) % b == 0

from typing import Iterable, List, Optional, Tuple
import math

 # 7.19
def compare_february_precip(feb_this: Iterable[float], feb_last: Iterable[float]) -> bool:
    return sum(feb_this) > sum(feb_last)

 # 7.20
def fits_capacity(weights: Iterable[float], capacity: float) -> bool:
    return sum(weights) <= capacity

 # 7.21
def compare_decathlon(scores1: Iterable[float], scores2: Iterable[float]) -> Tuple[str, float, float]:
    t1 = sum(scores1)
    t2 = sum(scores2)
    if t1 > t2:
        who = 'first'
    elif t2 > t1:
        who = 'second'
    else:
        who = 'equal'
    return who, t1, t2

 # 7.22
def cheaper_set(costs1: Iterable[float], costs2: Iterable[float]) -> Tuple[str, float, float]:
    t1 = sum(costs1)
    t2 = sum(costs2)
    if t1 < t2:
        which = 'first'
    elif t2 < t1:
        which = 'second'
    else:
        which = 'equal'
    return which, t1, t2

 # 7.23
def product_less_than_10000(nums: Iterable[float]) -> bool:
    prod = math.prod(nums)
    return prod < 10000

 # 7.24
def product_greater_than(nums: Iterable[float], S: float) -> bool:
    prod = math.prod(nums)
    return prod > S

 # 7.25, 7.26, 7.27, 7.28, 7.29, 7.30 (среднее арифметическое)
def mean(values: Iterable[float]) -> Optional[float]:
    vals = list(values)
    if not vals:
        return None
    return sum(vals) / len(vals)

 # 7.31
def mean_until_negative(seq: Iterable[float]) -> Optional[float]:
    total = 0.0
    count = 0
    for x in seq:
        if x < 0:
            break
        total += x
        count += 1
    if count == 0:
        return None
    return total / count

 # 7.32
def mean_two_classes(class1: Iterable[float], class2: Iterable[float]) -> Tuple[Optional[float], Optional[float]]:
    return mean(class1), mean(class2)

 # 7.33
def mean_precip_for_month(days_precip: Iterable[float]) -> Optional[float]:
    return mean(days_precip)

 # 7.34
def mean_two_equal_classes(class1: Iterable[float], class2: Iterable[float]) -> Tuple[Optional[float], Optional[float]]:
    return mean(class1), mean(class2)

from typing import List, Tuple
import math
import functools
import operator

 # 7.35
def task_7_35(class1: List[float], class2: List[float]) -> Tuple[float, float]:
    assert len(class1) == len(class2) and len(class1) > 0
    return sum(class1) / len(class1), sum(class2) / len(class2)

 # 7.36
def task_7_36(s: List[float], y: List[float]) -> Tuple[float, float]:
    assert len(s) == len(y) and len(s) == 10
    production = sum(si * yi for si, yi in zip(s, y))
    total_area = sum(s)
    avg_yield = production / total_area if total_area != 0 else 0.0
    return production, avg_yield

 # 7.37
def task_7_37(pop: List[float], area: List[float]) -> float:
    assert len(pop) == len(area) == 12
    total_pop = sum(pop)
    total_area = sum(area)
    return total_pop / total_area if total_area != 0 else 0.0

 # 7.38
def task_7_38(pop: List[float], density: List[float]) -> float:
    assert len(pop) == len(density) == 12
    areas = [p / d if d != 0 else 0.0 for p, d in zip(pop, density)]
    return sum(areas)

 # 7.39
def task_7_39(a: List[float]) -> Tuple[float, float, float, float]:
    n = len(a)
    sum_abs = sum(abs(x) for x in a)
    prod_abs = 1.0
    for x in a:
        prod_abs *= abs(x)
    sum_all = sum(a)
    alt_sum = sum(a[i] if i % 2 == 0 else -a[i] for i in range(n))
    return sum_abs, prod_abs, sum_all, alt_sum

 # 7.40
def task_7_40(arr: List[float]) -> float:
    assert len(arr) == 12
    return sum(x for x in arr if x > 10.75)

 # 7.41
def task_7_41(b: List[float]) -> float:
    if not b:
        return 0.0
    first = b[0]
    return sum(x for x in b if x > first)

 # 7.42
def task_7_42(a: List[int]) -> int:
    return sum(x for x in a if x % 2 == 0)

 # 7.43
def task_7_43(a: List[int]) -> int:
    assert len(a) == 10
    return sum(x for x in a if x % 10 == 0)

 # 7.44
def task_7_44(a: List[float]) -> float:
    return sum(a)

 # 7.45
def task_7_45(c: List[float]) -> float:
    assert len(c) == 15
    return sum(c[i] if i % 2 == 0 else -c[i] for i in range(15))

 # 7.46
def task_7_46(a: List[int]) -> List[int]:
    n = len(a)
    res = []
    for i in range(n // 2):
        res.append(a[i] + a[n - 1 - i])
    return res






































