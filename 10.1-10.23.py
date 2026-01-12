import random

def inp_int(prompt, default=None):
    s = input(prompt)
    if s.strip() == "" and default is not None:
        return default
    return int(s)

# 10.1
 # a
print("10.1 a) 8 веществ. чисел в [0,1]:")
print([random.uniform(0, 1) for _ in range(8)])

 # b
k = inp_int("10.1 b) Введите k (целое): ")
print([random.random() for _ in range(k)])

 # в
print("10.1 в) 15 веществ. чисел в [25,26):")
print([25 + random.random() for _ in range(15)])

# г
print("10.1 г) 20 веществ. чисел в [0,15):")
print([random.random() * 15 for _ in range(20)])

 # д
a = inp_int("10.1 д) Введите a (натуральное, >=1): ")
if a < 1:
    print("a должно быть >=1, использую a=1")
    a = 1
k = random.randint(1, a)
print(f"сгенерированное k = {k}")
print([random.random() * k for _ in range(k)])

 # e
print("10.1 e) 10 веществ. чисел в [-40,40):")
print([-40 + random.random() * 80 for _ in range(10)])

 # ж
m = inp_int("10.1 ж) Введите m (натуральное, >=1): ")
a = float(input("Введите a (вещественное): "))
b = float(input("Введите b (вещественное, > a): "))
if m < 1:
    m = 1
if b <= a:
    b = a + 1.0
k = random.randint(1, m)
print(f"сгенерированное k = {k}")
print([a + random.random() * (b - a) for _ in range(k)])

# 10.2
 # a
print("10.2 a) 10 целых в [0,10]:")
print([random.randint(0, 10) for _ in range(10)])

 # b
k = inp_int("10.2 b) Введите k (целое): ")
a = inp_int("Введите a (целое, >=0): ")
print([random.randint(0, a) for _ in range(k)])

 # в
print("10.2 в) 20 целых в [10,20]:")
print([random.randint(10, 20) for _ in range(20)])

 # г
k = inp_int("10.2 г) Введите k (целое): ")
a = inp_int("Введите a (целое, >= -10): ")
print([random.randint(-10, a) for _ in range(k)])

 # д
b = inp_int("10.2 д) Введите b (целое, >=0): ")
k = random.randint(1, 15)
print(f"сгенерированное k = {k}")
print([random.randint(0, b) for _ in range(k)])

 # 10.3
a = inp_int("10.3 Введите a (начало диапазона целых): ")
b = inp_int("Введите b (конец диапазона целых): ")
if b < a:
    a, b = b, a
m = random.randint(1, 20)
n = random.randint(1, 20)
print(f"сгенерированные m = {m}, n = {n}")
print(f"{n} целых чисел в [{a},{b}]:")
print([random.randint(a, b) for _ in range(n)])
print(f"{m} положительных вещественных чисел ≤ n (т.е. в (0,{n}]):")
print([random.random() * n for _ in range(m)])

 # 10.4
nums = [random.randint(0, 3) for _ in range(50)]
evens = [x for x in nums if x % 2 == 0]
print("Сгенерированные 50 чисел:", nums)
print("Вывести только четные (включая нули):", evens)

 # 10.5
nums = [random.randint(0, 5) for _ in range(30)]
odds = [x for x in nums if x % 2 == 1]
print("Сгенерированные 30 чисел:", nums)
print("Вывести только нечетные:", odds)

 # 10.6
nums = [random.randint(0, 1) for _ in range(50)]
count_ones = sum(nums)
count_zeros = len(nums) - count_ones
print("Сгенерированные 50 чисел (0/1):", nums)
print(f"Количество единиц: {count_ones}, количество нулей: {count_zeros}")

import random

 # 10.7
 # а
def task_10_7_a():
    a = random.randrange(0, 2)
    b = random.randrange(0, 3)
    while b == a:
        b = random.randrange(0, 3)
    return a, b

 # b
def task_10_7_b():
    while True:
        a = random.randrange(1, 3)
        b = random.randrange(0, 3)
        c = random.randrange(1, 4)
        if a != b and a != c and b != c:
            return a, b, c

 # c
def task_10_7_c():
    lst = [2] * 7 + [3] * 8
    random.shuffle(lst)
    return lst

 # 10.8
def coin_toss():
    return random.randint(0, 1)

def coin_toss_n(n):
    return [coin_toss() for _ in range(n)]

 # 10.9
def relative_frequency(n):
    tosses = coin_toss_n(n)
    count0 = tosses.count(0)
    count1 = tosses.count(1)
    return {'n': n, '0': count0, '1': count1, 'freq0': count0 / n, 'freq1': count1 / n}

 # 10.10
 # a
def game_once():
    choice = input("Выберите: 1 — четное, 2 — нечетное: ").strip()
    if choice not in ('1', '2'):
        print("Неверный ввод.")
        return
    player_choice = int(choice)
    comp = random.choice([1, 2])
    print(f"Вы: {player_choice}, Компьютер: {comp}")
    if player_choice == comp:
        print("Вы выиграли!")
    else:
        print("Вы проиграли.")

 # b
def game_n_times(n):
    score_player = 0
    score_comp = 0
    for i in range(n):
        choice = input(f"Раунд {i+1}. Введите 1 (чет) или 2 (нечет): ").strip()
        if choice not in ('1', '2'):
            print("Неверный ввод, этот раунд засчитывается как неверный.")
            score_comp += 1
            continue
        player_choice = int(choice)
        comp = random.choice([1, 2])
        if player_choice == comp:
            score_player += 1
        else:
            score_comp += 1
    print(f"Счет {score_player}:{score_comp}", end=' ')
    if score_player > score_comp:
        print("в вашу пользу. Вы выиграли!")
    elif score_player < score_comp:
        print("в пользу компьютера. Вы проиграли!")
    else:
        print("ничья.")

 # c
def game_until_stop():
    score_player = 0
    score_comp = 0
    while True:
        choice = input("Введите 1 (чет) или 2 (нечет): ").strip()
        if choice in ('1', '2'):
            player_choice = int(choice)
            comp = random.choice([1, 2])
            if player_choice == comp:
                score_player += 1
                print("Верно.")
            else:
                score_comp += 1
                print("Неверно.")
        else:
            print("Неверный ввод — этот ход пропускается.")
        cont = input("Продолжить еще раз? (Да/Нет): ").strip().lower()
        if cont in ('нет', 'n', 'no'):
            break
    print(f"Игра окончена. Правильных: {score_player}, Неправильных: {score_comp}")

 # 10.11
def roll_die():
    return random.randint(1, 6)

 # 10.12
def two_players_roll():
    p1 = roll_die()
    p2 = roll_die()
    if p1 > p2:
        winner = 'Игрок 1'
    elif p2 > p1:
        winner = 'Игрок 2'
    else:
        winner = 'Ничья'
    return {'p1': p1, 'p2': p2, 'winner': winner}

 # 10.13
import random

def play_one_game_two_rolls():
    a = random.randint(1,6) + random.randint(1,6)
    b = random.randint(1,6) + random.randint(1,6)
    print(f"Игрок 1: {a}, Игрок 2: {b}")
    if a > b:
        print("Победил игрок 1")
    elif b > a:
        print("Победил игрок 2")
    else:
        print("Ничья")

def play_many_games(n=1000):
    wins1 = wins2 = ties = 0
    for _ in range(n):
        a = random.randint(1,6) + random.randint(1,6)
        b = random.randint(1,6) + random.randint(1,6)
        if a > b:
            wins1 += 1
        elif b > a:
            wins2 += 1
        else:
            ties += 1
    print(f"Из {n} игр: игрок1={wins1}, игрок2={wins2}, ничьи={ties}")

 # 10.14
import random

def competition_k_players(k=5, n=3):
    totals = []
    for i in range(k):
        total = sum(random.randint(1, 6) for _ in range(n))
        totals.append(total)
        print(f"Игрок {i + 1}: сумма = {total}")
    max_sum = max(totals)
    winners = [i + 1 for i, s in enumerate(totals) if s == max_sum]
    if len(winners) == 1:
        print(f"Победил игрок {winners[0]} с суммой {max_sum}")
    else:
        print(f"Ничья между игроками {winners} с суммой {max_sum}")

 # 10.15
import random
from collections import Counter

def relative_frequencies(trials=100):
    counts = Counter(random.randint(1,6) for _ in range(trials))
    print(f"Всего бросков: {trials}")
    for face in range(1,7):
        freq = counts[face] / trials
        print(f"{face}: {counts[face]} ({freq:.3f})")

 # 10.16
import random
def pick_one_domino():
    tiles = [(i,j) for i in range(7) for j in range(i,7)]
    a, b = random.choice(tiles)
    if random.choice([True, False]):
        a, b = b, a
    print(f"Выбрана кость {a}-{b}")

 # 10.17
import random
def pick_two_domino_and_check():
    tiles = [(i,j) for i in range(7) for j in range(i,7)]
    a = random.choice(tiles)
    b = random.choice(tiles)
    while b == a:
        b = random.choice(tiles)
    print(f"Кость 1: {a[0]}-{a[1]}")
    print(f"Кость 2: {b[0]}-{b[1]}")
    if set(a) & set(b):
        print("Можно приставить (есть совпадающая грань)")
    else:
        print("Нельзя приставить (нет совпадающих граней)")

 # 10.18
import random
def quiz_once():
    a = random.randint(1,9)
    b = random.randint(1,9)
    ans = input(f"Чему равно произведение {a}×{b}? ")
    try:
        if int(ans) == a*b:
            print("Правильно")
        else:
            print(f"Неправильно. Правильный ответ: {a*b}")
    except ValueError:
        print("Неверный ввод")

def quiz_n_times(n=20):
    correct = wrong = 0
    for _ in range(n):
        a = random.randint(1,9)
        b = random.randint(1,9)
        try:
            ans = int(input(f"Чему равно произведение {a}×{b}? "))
            if ans == a*b:
                correct += 1
            else:
                wrong += 1
        except ValueError:
            print("Неверный ввод, считаю как неверный ответ")
            wrong += 1
    print(f"Правильных: {correct}, Неправильных: {wrong}")

def quiz_until_zero():
    while True:
        a = random.randint(1,9)
        b = random.randint(1,9)
        try:
            ans = int(input(f"Чему равно произведение {a}×{b}? (введите 0 для выхода) "))
            if ans == 0:
                print("Выход.")
                break
            if ans == a*b:
                print("Правильно")
            else:
                print(f"Неправильно. Правильный ответ: {a*b}")
        except ValueError:
            print("Неверный ввод, попробуйте ещё раз или введите 0 для выхода")

 # 10.18
import random

def question_once():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    ans = input(f"Чему равно произведение {a}×{b}? Введите ответ: ")
    try:
        if int(ans) == a * b:
            print("Верно!")
        else:
            print(f"Неверно. Правильный ответ: {a * b}")
    except ValueError:
        print("Неверный ввод")

def question_20_times():
    correct = 0
    incorrect = 0
    for i in range(20):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        try:
            ans = int(input(f"{i+1}. Чему равно произведение {a}×{b}? "))
            if ans == a * b:
                correct += 1
            else:
                incorrect += 1
        except ValueError:
            print("Неверный ввод, считается как неправильный ответ")
            incorrect += 1
    print(f"Правильных ответов: {correct}, Неправильных: {incorrect}")

def question_until_zero():
    while True:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        try:
            ans = int(input(f"Чему равно произведение {a}×{b}? (Ввод 0 завершает) "))
            if ans == 0:
                print("Завершение по 0.")
                break
            if ans == a * b:
                print("Верно!")
            else:
                print(f"Неверно. Правильный ответ: {a * b}")
        except ValueError:
            print("Неверный ввод")

 # 10.19
import random

ranks = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

card = random.choice(ranks)
print(f"Выбрано достоинство карты: {card}")

 # 10.20
import random

ranks = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пики', 'трефы', 'бубны', 'червы']

rank = random.choice(ranks)
suit = random.choice(suits)
print(f"Выбрана карта: {rank} {suit}")

 # 10.21
import random

ranks = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пики', 'трефы', 'бубны', 'червы']

def draw_card():
    return random.choice(ranks), random.choice(suits)

def card_value(card):
    rank, suit = card
    return (ranks.index(rank), suits.index(suit))

 # 10.22
ranks = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пики', 'трефы', 'бубны', 'червы']

def draw_card():
    return random.choice(ranks), random.choice(suits)

def value(card):
    r, s = card
    return (ranks.index(r), suits.index(s))

def play_rounds(n):
    wins1 = wins2 = draws = 0
    for i in range(n):
        c1 = draw_card()
        c2 = draw_card()
        v1 = value(c1)
        v2 = value(c2)
        if v1[0] > v2[0] or (v1[0] == v2[0] and v1[1] > v2[1]):
            wins1 += 1
        elif v1[0] < v2[0] or (v1[0] == v2[0] and v1[1] < v2[1]):
            wins2 += 1
        else:
            draws += 1
    return wins1, wins2, draws

 # 10.23
import random

ranks = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пики', 'трефы', 'бубны', 'червы']

def draw_card():
    return random.choice(ranks), random.choice(suits)

def compare_with_trump(c1, c2, trump):
    r1, s1 = c1
    r2, s2 = c2
    t1 = (s1 == trump)
    t2 = (s2 == trump)
    if t1 and not t2:
        return 1
    if t2 and not t1:
        return 2
    if ranks.index(r1) > ranks.index(r2):
        return 1
    if ranks.index(r1) < ranks.index(r2):
        return 2
    if suits.index(s1) > suits.index(s2):
        return 1
    if suits.index(s1) < suits.index(s2):
        return 2
    return 0

















