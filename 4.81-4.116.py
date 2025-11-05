#my function for программ ниже
def choose_form(n, forms):

    n = abs(n)
    if 11 <= n % 100 <= 14:
        return forms[2]
    if n % 10 == 1:
        return forms[0]
    if 2 <= n % 10 <= 4:
        return forms[1]
    return forms[2]

 # 4.81
def triangle_classify(a, b, c, eps=1e-9):

    if not (a + b > c and a + c > b and b + c > a):
        return {"exists": False}

    sides = sorted([a, b, c])
    x, y, z = sides

    sum_sq = x*x + y*y
    z_sq = z*z
    if abs(sum_sq - z_sq) < eps:
        angle_type = "прямоугольный"
    elif sum_sq > z_sq:
        angle_type = "остроугольный"
    else:
        angle_type = "тупоугольный"

    if abs(a - b) < eps and abs(b - c) < eps:
        side_type = "равносторонний"
    elif abs(a - b) < eps or abs(b - c) < eps or abs(a - c) < eps:
        side_type = "равнобедренный"
    else:
        side_type = "разносторонний"

    return {"exists": True, "angle_type": angle_type, "side_type": side_type}

 # 4.82
def age_phrase(n):
    form = choose_form(n, ("год", "года", "лет"))
    return f"Мне {n} {form}"

 # 4.83
def mushrooms_phrase(k):
    form = choose_form(k, ("гриб", "гриба", "грибов"))
    return f"Мы нашли {k} {form} в лесу"

# 4.84
def price_in_rubles(kopecks):
    rub = kopecks // 100
    kop = kopecks % 100
    rub_form = choose_form(rub, ("рубль", "рубля", "рублей"))
    kop_form = choose_form(kop, ("копейка", "копейки", "копеек"))
    if rub == 0:
        return f"{kop} {kop_form}"
    if kop == 0:
        return f"{rub} {rub_form} ровно"
    return f"{rub} {rub_form} {kop} {kop_form}"

 # 4.85
def age_from_months(n):
    years = n // 12
    months = n % 12
    year_form = choose_form(years, ("год", "года", "лет"))
    month_form = choose_form(months, ("месяц", "месяца", "месяцев"))
    if years > 0 and months > 0:
        return f"{years} {year_form} {months} {month_form}"
    elif years > 0 and months == 0:
        return f"{years} {year_form} ровно"
    else:
        return f"{months} {month_form}"

 # 4.86
from datetime import date

def full_years(b_year, b_month, b_day, cur_year, cur_month, cur_day):
    birth = date(b_year, b_month, b_day)
    today = date(cur_year, cur_month, cur_day)
    if today < birth:
        raise ValueError("Дата сегодня раньше даты рождения")
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    return age

 # 4.87
def who_is_older(b1_y, b1_m, b1_d, b2_y, b2_m, b2_d):
    t1 = (b1_y, b1_m, b1_d)
    t2 = (b2_y, b2_m, b2_d)
    if t1 < t2:
        return "Первый старше"
    elif t1 > t2:
        return "Второй старше"
    else:
        return "Одинакового возраста"

 #4.88
def years_and_months_by_months(b_year, b_month, cur_year, cur_month):
    months = (cur_year - b_year) * 12 + (cur_month - b_month)
    if months < 0:
        raise ValueError("Дата рождения позже текущей даты")
    years = months // 12
    rem_months = months % 12

    parts = []
    if years > 0:
        parts.append(f"{years} {choose_form(years, ('год','года','лет'))}")
    if rem_months > 0:
        parts.append(f"{rem_months} {choose_form(rem_months, ('месяц','месяца','месяцев'))}")
    if not parts:
        return "0 месяцев"
    return " ".join(parts)

#my function for программ ниже
def minutes_from_midnight(h, m):
    return h * 60 + m

 # 4.89
def train_on_platform(a, b, c, d, n, m):
    arr = minutes_from_midnight(a, b)
    dep = minutes_from_midnight(c, d)
    t = minutes_from_midnight(n, m)
    if arr <= dep:
        return arr <= t <= dep
    else:
        return t >= arr or t <= dep

 # 4.90
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def prev_day_no_year(m, n):
    if n > 1:
        return m, n - 1
    else:
        prev_m = m - 1
        return prev_m, MONTH_DAYS[prev_m - 1]

def next_day_no_year(m, n):
    days_in_month = MONTH_DAYS[m - 1]
    if n < days_in_month:
        return m, n + 1
    else:
        return m + 1, 1

 # 4.91
def is_leap_year(year):

    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def prev_next_with_year(g, m, n, consider_leap=True):

    mdays = MONTH_DAYS.copy()
    if consider_leap and is_leap_year(g):
        mdays[1] = 29

    if n > 1:
        prev = (g, m, n - 1)
    else:
        if m > 1:
            pm = m - 1
            prev = (g, pm, mdays[pm - 1])
        else:
            prev_year = g - 1
            prev = (prev_year, 12, 31)

    days_this_month = mdays[m - 1]
    if n < days_this_month:
        nxt = (g, m, n + 1)
    else:
        if m < 12:
            nxt = (g, m + 1, 1)
        else:
            nxt = (g + 1, 1, 1)
    return prev, nxt

 # 4.92
def traffic_light_color(t):

    if t < 0:
        raise ValueError("t must be non-negative")
    pos = (t % 6)
    if pos in (0, 1, 2):
        return 'green'
    elif pos == 3:
        return 'yellow'
    else:
        return 'red'

 # 4.93
def day_type_k_given_jan1_is_monday(k):

    if not (1 <= k <= 365):
        raise ValueError("k must be in 1..365")

    weekday = ((1 - 1) + (k - 1)) % 7 + 1
    if weekday == 6:
        return 'Saturday'
    elif weekday == 7:
        return 'Sunday'
    else:
        return 'Workday'

 # 4.94
def digit_4_94(k):

     for num in range(10, 100):
         s = str(num)
         if k <= len(s):
             return s[k - 1]
         k -= len(s)
 # 4.95
def digit_4_95(n):
    nums = [0] + list(range(1, 21))
    for num in nums:
        s = str(num)
        if n <= len(s):
            return s[n-1]
        n -= len(s)
 # 4.96
def digit_4_96(k):
    for num in range(50, 251):
        s = str(num)
        if k <= len(s):
            return s[k-1]
        k -= len(s)

 # 4.97
def digit_4_97(k):
    for num in range(1, 111):
        s = str(num)
        if k <= len(s):
            return s[k-1]
        k -= len(s)

 # 4.98
def sum_parity_4_98(a, n):
    s = 0
    for i in range(a, a + n):
        s += i
    return s % 2 == 0

 # 4.99
def sum_parity_4_98(a, n):
    s = 0
    for i in range(a, a + n):
        s += i
    return s % 2 == 0

 # 4.100
def max_min_4_100_a(x, y):
    mx = x
    mn = x
    if y > mx:
        mx = y
    if y < mn:
        mn = y
    return mx, mn

def max_min_4_100_b(x, y):
    if x < y:
        x, y = y, x
    return x, y

 # 4.101
def max_4_101(x, y, z):
    res = x
    if y > res:
        res = y
    if z > res:
        res = z
    return res

def min_4_101(x, y, z):
    res = x
    if y < res:
        res = y
    if z < res:
        res = z
    return res

 # 4.101
def max_4_101(x, y, z):
    res = x
    if y > res:
        res = y
    if z > res:
        res = z
    return res

def min_4_101(x, y, z):
    res = x
    if y < res:
        res = y
    if z < res:
        res = z
    return res

 # 4.102
def max_4_102(a, b, c, d):
    res = a
    if b > res: res = b
    if c > res: res = c
    if d > res: res = d
    return res

def min_4_102(a, b, c, d):
    res = a
    if b < res: res = b
    if c < res: res = c
    if d < res: res = d
    return res

 # 4.103
def abs_4_103(x):
    if x < 0:
        x = -x
    return x

import math #для прог ниже

 # 4.104
def abs_custom(x):
    return x if x >= 0 else -x

def task_4_104(a, b):

    half_sum = 0.5 * (abs_custom(a) + abs_custom(b))

    product_sqrt = math.sqrt(abs_custom(a) * abs_custom(b))
    return half_sum, product_sqrt

 # 4.105
def task_4_105(a, b):

    if abs_custom(a) > abs_custom(b):
        a = a / 2
    return a

 # 4.106
def task_4_106(a, b):

    if b >= 0 and math.sqrt(b) < a:
        b = b * 3
    return a, b

 # 4.107
def task_4_107(x, y, z):

    evens = [v for v in (x, y, z) if v % 2 == 0]
    return evens

 # 4.108
def task_4_108(x, y, z):

    res = []
    for v in (x, y, z):
        res.append(v * v if v >= 0 else v)
    return tuple(res)

 # 4.109
def task_4_109(x, y, z):

    inside = [v for v in (x, y, z) if 1.6 <= v <= 3.8]
    return inside

 # 4.110
def task_4_110(a, b, c, d):

    count_neg = sum(1 for v in (a, b, c, d) if v < 0)
    return count_neg

 # 4.111
def task_4_111(a, b, c, d):

    count_even = sum(1 for v in (a, b, c, d) if v % 2 == 0)
    return count_even

 # 4.112
def task_4_112(a, b, c):

    s = sum(v for v in (a, b, c) if v > 0)
    return s

 # 4.113
def task_4_113(a, b, c, d):

    s = sum(v for v in (a, b, c, d) if v > 5)
    return s

 # 4.114
def task_4_114(a, b, c, d):

    s = sum(v for v in (a, b, c, d) if v % 3 == 0)
    return s

 # 4.115
def task_4_115(a, b, c, d, e, f):

    s = sum(v for v in (a, b, c, d, e, f) if v > 0)
    return s

 # 4.116
def task_4_116(x):

    if x < -1:
        return -1
    elif x > -1:
        return x
    else:
        return 1
































