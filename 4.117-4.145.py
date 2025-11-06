 # 4.117
def z(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1

 # 4.118
def f_118(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    else:
        return x**2

 # 4.119
def f_119(y):
    if y > 2:
        return 2
    elif 0 < y <= 2:
        return 0
    else:  # y <= 0
        return -3*y

 # 4.120
 # (а)
def g_a(x):
    if x <= -1:
        return 0
    elif x < 0:
        return x + 1
    else:
        return 1

 # (б)
def g_b(x):
    if x <= -1:
        return 1
    elif x < 1:
        return -x
    else:
        return -1

 # (в)
def g_c(x):
    if abs(x) >= 1:
        return 0
    else:
        return 1 - abs(x)

 # 4.121
x = float(input("Введите x: "))
if x == 1 or x == 5:
    print("Точка на границе (x=1 или x=5).")
elif x < 1:
    print("Область I")
elif x < 5:
    print("Область II")
else:
    print("Область III")

 # 4.122
y = float(input("Введите y: "))

if y == 2.5 or y == 5.0 or y == 0:
    print("Точка на границе (y=0, 2.5 или 5.0).")
elif y > 5.0:
    print("Область I")
elif y > 2.5:
    print("Область II")
elif y > 0:
    print("Область III")
else:
    print("y <= 0 — за пределами рассматриваемой части (или на/ниже оси OX).")

 # 4.123
p = int(input("Введите число очков команды за игру (обычно 3,1 или 0): "))
if p == 3:
    print("Выигрыш")
elif p == 1:
    print("Ничья")
elif p == 0:
    print("Проигрыш")
else:
    print("Некорректное число очков.")

 # 4.124
m = int(input("Возраст Мити: "))
v = int(input("Возраст Васи: "))
if m > v:
    print("Митя старше Васи.")
elif m < v:
    print("Вася старше Мити.")
else:
    print("Одинакового возраста.")

 # 4.125
def category_boxer(weight):
    if weight <= 60:
        return "легкий"
    elif weight <= 64:
        return "первый полусредний"
    elif weight <= 69:
        return "полусредний"
    else:
        return "тяжёлая категория"

 # 4.126
def divisibility(m, n):
    if n != 0 and m % n == 0:
        return "m делится на n"
    if m != 0 and n % m == 0:
        return "n делится на m"
    return "ни одно не делится на другое"

 # 4.127
def extremums_positions(a, b, c):
    nums = [a, b, c]
    max_idx = nums.index(max(nums)) + 1
    min_idx = nums.index(min(nums)) + 1
    for i, v in enumerate(nums, start=1):
        if i != max_idx and i != min_idx:
            mid_idx = i
            break
    return {"max": max_idx, "min": min_idx, "middle": mid_idx}

 # 4.128
def min_max_of_three(x, y, z):
    return min(x, y, z), max(x, y, z)

 # 4.129
def sum_two_largest(a, b, c):
    arr = sorted([a, b, c])
    return arr[1] + arr[2]

 # 4.130
def product_two_smallest(a, b, c):
    arr = sorted([a, b, c])
    return arr[0] * arr[1]

 # 4.131
def mean_of_middles(triple1, triple2):
    mid1 = sorted(triple1)[1]
    mid2 = sorted(triple2)[1]
    return (mid1 + mid2) / 2.0

 # 4.132
def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4
    raise ValueError("координаты должны быть ненулевыми")

 # 4.133
def weekday_name(n):
    names = {
        1: "понедельник",
        2: "вторник",
        3: "среда",
        4: "четверг",
        5: "пятница",
        6: "суббота",
        7: "воскресенье"
    }
    return names.get(n, "некорректный номер дня")

  # 4.134
def month_name(n):
    names = {
        1: "январь",
        2: "февраль",
        3: "март",
        4: "апрель",
        5: "май",
        6: "июнь",
        7: "июль",
        8: "август",
        9: "сентябрь",
        10: "октябрь",
        11: "ноябрь",
        12: "декабрь"
    }
    return names.get(n, "некорректный номер месяца")

 # 4.135
def season_by_month(n):
    if n in (12, 1, 2):
        return "зима"
    if n in (3, 4, 5):
        return "весна"
    if n in (6, 7, 8):
        return "лето"
    if n in (9, 10, 11):
        return "осень"
    return "некорректный номер месяца"

 # 4.136
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month_4136(month, consider_leap=False, year=None):
    if not 1 <= month <= 12:
        raise ValueError("month должен быть от 1 до 12")
    if consider_leap:
        if year is None:
            raise ValueError("нужен параметр year при consider_leap=True")
        leap = is_leap_year(year)
    else:
        leap = False

    days_in_month = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]

 # 4.137
def days_in_month_4137(month):
    if not 1 <= month <= 12:
        raise ValueError("month должен быть от 1 до 12")
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]

 # 4.138
def suit_name_4138(m):
    suits = {1: "пики", 2: "трефы", 3: "бубны", 4: "червы"}
    return suits.get(m, "неизвестная масть")

 # 4.139
def rank_name_4139(k):
    mapping = {
        6: "шестерка", 7: "семерка", 8: "восьмерка", 9: "девятка", 10: "десятка",
        11: "валет", 12: "дама", 13: "король", 14: "туз"
    }
    return mapping.get(k, "неизвестное достоинство")

 # 4.140
def full_card_name_4140(m, k):
    suits_for_full = {1: "пик", 2: "треф", 3: "бубен", 4: "червей"}
    rank = rank_name_4139(k)
    suit = suits_for_full.get(m)
    if suit is None or rank.startswith("неизвестное"):
        return "некорректные входные данные"
    return f"{rank.capitalize()} {suit}"

 # 4.141
def weekday_name_from_index(idx):
    names = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    return names[idx % 7]

 # a)
def weekday_on_k_a(k):
    if not 1 <= k <= 365:
        raise ValueError("k должен быть в диапазоне 1..365")
    idx = (k - 1) % 7
    return weekday_name_from_index(idx)

 # б)
def weekday_on_k_b(k, d):
    if not 1 <= k <= 365:
        raise ValueError("k должен быть в диапазоне 1..365")
    if not 1 <= d <= 7:
        raise ValueError("d должен быть в диапазоне 1..7")
    idx = (d - 1 + (k - 1)) % 7
    return weekday_name_from_index(idx)

 # 4.142
def month_name_4142(m, n):
    if m < 0:
        raise ValueError("m неотрицателен")
    month_names = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
    month_lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m > 11:
        raise ValueError("m должен быть в диапазоне 0..11 для одного года (или используйте календарное смещение)")

    day_of_year = sum(month_lengths[:m]) + n
    if not 1 <= day_of_year <= 365:
        raise ValueError("введённые m и n приводят к дню вне 2010 года")
    cum = 0
    for i, L in enumerate(month_lengths):
        cum += L
        if day_of_year <= cum:
            return month_names[i]
    return None

 # 4.143
def days_in_month_non_leap():
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def prev_day_non_leap(m, n):
    dim = days_in_month_non_leap()
    if n > 1:
        return m, n - 1
    else:
        prev_m = m - 1
        prev_day = dim[prev_m - 1]
        return prev_m, prev_day

def next_day_non_leap(m, n):
    dim = days_in_month_non_leap()
    if n < dim[m - 1]:
        return m, n + 1
    else:
        next_m = m + 1
        return next_m, 1

# 4.144
def is_leap(g):
    return (g % 400 == 0) or (g % 4 == 0 and g % 100 != 0)

def days_in_month(g):
    if is_leap(g):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

 # Случай 1
def prev_date_non_leap(g, m, n):
    dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if n > 1:
        return g, m, n - 1
    else:
        if m > 1:
            prev_m = m - 1
            prev_day = dim[prev_m - 1]
            return g, prev_m, prev_day
        else:
            return g - 1, 12, 31

def next_date_non_leap(g, m, n):
    dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if n < dim[m - 1]:
        return g, m, n + 1
    else:
        if m < 12:
            return g, m + 1, 1
        else:
            return g + 1, 1, 1

 # Случай 2
def prev_date_with_leap(g, m, n):
    dim = days_in_month(g)
    if n > 1:
        return g, m, n - 1
    else:
        if m > 1:
            prev_m = m - 1
            prev_day = dim[prev_m - 1]
            return g, prev_m, prev_day
        else:

            return g - 1, 12, 31

def next_date_with_leap(g, m, n):
    dim = days_in_month(g)
    if n < dim[m - 1]:
        return g, m, n + 1
    else:
        if m < 12:
            return g, m + 1, 1
        else:
            return g + 1, 1, 1

 # 4.145
animals = ['Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца',
           'Обезьяна', 'Петух', 'Собака', 'Свинья']
colors = ['Зеленый', 'Красный', 'Желтый', 'Белый', 'Черный']

def sexagenary_name(year):
    base = 1984
    offset = year - base
    animal = animals[offset % 12]
    color = colors[(offset % 10) // 2]
    return f"{animal}, {color}"














































