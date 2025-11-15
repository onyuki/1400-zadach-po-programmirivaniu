from typing import List, Optional, Tuple

def safe_mean(xs: List[float]) -> Optional[float]:
    if not xs:
        return None
    return sum(xs) / len(xs)

# 7.106
def p7_106(c: List[float]) -> Optional[float]:
    return safe_mean([x for x in c if x > 20])

 # 7.107
def p7_107(x: int, a: List[int]) -> Optional[float]:
    return safe_mean([ai for ai in a if ai > x])

 # 7.108
def p7_108(b: List[int], n: int) -> Optional[float]:
    if n == 0:
        raise ValueError("n не должен быть 0")
    return safe_mean([bi for bi in b if bi % n == 0])

 # 7.109
def p7_109(a: List[int]) -> Tuple[Optional[float], Optional[float]]:
    ev = [x for x in a if x % 2 == 0]
    od = [x for x in a if x % 2 != 0]
    return safe_mean(ev), safe_mean(od)

 # 7.110
def p7_110(weights: List[float]) -> Tuple[Optional[float], Optional[float]]:
    full = [w for w in weights if w > 100]
    other = [w for w in weights if w <= 100]
    return safe_mean(full), safe_mean(other)

 # 7.111
def p7_111(heights: List[int]) -> Tuple[Optional[float], Optional[float]]:
    boys = [abs(h) for h in heights if h < 0]
    girls = [h for h in heights if h > 0]
    return safe_mean(boys), safe_mean(girls)

 # 7.112
def p7_112(b: List[float]) -> Optional[float]:
    return safe_mean([x for x in b if x > 10])

 # 7.113
def p7_113(n: int, a: List[int]) -> Optional[float]:
    return safe_mean([ai for ai in a if ai > n])

 # 7.114
def p7_114(d: List[int]) -> Optional[float]:
    ev = [x for x in d if x % 2 == 0]
    return safe_mean(ev)

 # 7.115
def p7_115(a: List[int], n: int) -> Optional[float]:
    if n == 0:
        raise ValueError("n не должен быть 0")
    return safe_mean([ai for ai in a if ai % n == 0])

 # 7.116
def p7_116(cars: List[float], motos: List[float]) -> Tuple[Optional[bool], Optional[bool]]:
    if cars and motos:
        mean_cars = safe_mean(cars)
        mean_motos = safe_mean(motos)
        cond1 = mean_cars > 3 * mean_motos
    else:
        cond1 = None
    if not motos:
        cond2 = None
    else:
        cars_gt5000 = [c for c in cars if c > 5000]
        if not cars_gt5000:
            cond2 = None
        else:
            max_moto = max(motos)
            exists = any(c > max_moto for c in cars_gt5000)
            cond2 = exists
    return cond1, cond2

 # 7.117
def avg_boys_more_than_girls_by_10(heights):
    boys = [abs(h) for h in heights if h < 0]
    girls = [h for h in heights if h > 0]
    if not boys or not girls:
        return None
    return (sum(boys) / len(boys)) > (sum(girls) / len(girls) + 10.0)

 # 7.118
def first_and_last_index_of_10(arr):
    n = len(arr)
    first = None
    last = None
    for i, v in enumerate(arr):
        if v == 10:
            if first is None:
                first = i + 1
            last = i + 1
    return first, last

 # 7.119
def last_index_greater_than_100(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > 100:
            return i + 1
    return None

 # 7.120
def last_index_equal_25(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 25:
            return i + 1
    return None

 # 7.121
def last_index_negative(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < 0:
            return i + 1
    return None

 # 7.122
def last_index_ending_with_12(arr):
    for i in range(len(arr) - 1, -1, -1):
        if abs(arr[i]) % 100 == 12:
            return i + 1
    return None

 # 7.123
def position_in_descending_heights(heights_desc, new_height):
    n = len(heights_desc)
    for i, h in enumerate(heights_desc):
        if new_height > h:
            return i + 1
    return n + 1

 # 7.124
def position_of_team_with_N(points_desc, N):
    for i, p in enumerate(points_desc):
        if p == N:
            return i + 1
    return None

 # 7.125a
import bisect
arr = list(map(float, input().split()))
while len(arr) < 16:
    arr += list(map(float, input().split()))
y = arr[:15]
n = arr[15]
k = bisect.bisect_left(y, n)
print(sum(y[:k]))

 # 7.125b
import bisect
arr = list(map(float, input().split()))
while len(arr) < 16:
    arr += list(map(float, input().split()))
y = arr[:15]
n = arr[15]
k = bisect.bisect_left(y, n)
idx1, idx2 = k, k+1
val1, val2 = y[k-1], y[k]
print(idx1, val1)
print(idx2, val2)

 # 7.126
a = list(map(float, input().split()))
while len(a) < 15:
    a += list(map(float, input().split()))
ans = None
for i in range(13):
    if a[i] < 0 and a[i+1] < 0 and a[i+2] < 0:
        ans = i+1
        break
if ans is None:
    print("NO")
else:
    print(ans)

 # 7.127
idx = 0
found = None
while True:
    try:
        x = int(input().strip())
    except EOFError:
        break
    idx += 1
    if found is None and x == 666:
        found = idx
    if x == 100:
        break
if found is None:
    print("NO")
else:
    print(found)

 # 7.128
b = list(map(int, input().split()))
while len(b) < 12:
    b += list(map(int, input().split()))
ans = None
for i, val in enumerate(b):
    if abs(val) % 10 == 7:
        ans = i+1
        break
if ans is None:
    print("NO")
else:
    print(ans)

 # 7.129
idx = 0
found = None
while True:
    try:
        x = int(input().strip())
    except EOFError:
        break
    idx += 1
    if found is None and x % 7 == 0:
        found = idx
    if x == 1:
        break
if found is None:
    print("NO")
else:
    print(found)

 # 7.130
arr = list(map(int, input().split()))
while len(arr) < 20:
    arr += list(map(int, input().split()))
rep_val = None
for i in range(19):
    if arr[i] == arr[i+1]:
        rep_val = arr[i]
        break
if rep_val is None:
    print(0)
else:
    count = arr.count(rep_val)
    print(count)













































