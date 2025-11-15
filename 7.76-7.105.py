 # 7.76
cnt = {1: 0, 2: 0}
time_sum = {1: 0, 2: 0}

for _ in range(24):
    try:
        parts = input().split()
    except EOFError:
        break
    if not parts:
        continue
    team = int(parts[0])
    if len(parts) > 1:
        t = int(parts[1])
    else:
        t = int(input().strip())
    if team in (1, 2):
        cnt[team] += 1
        time_sum[team] += t

 # 7.77
cnt = {1: 0, 2: 0}
time_sum = {1: 0, 2: 0}

while True:
    try:
        parts = input().split()
    except EOFError:
        break
    if not parts:
        continue
    team = int(parts[0])
    if team == 0:
        break
    if len(parts) > 1:
        t = int(parts[1])
    else:
        t = int(input().strip())
    if team in (1, 2):
        cnt[team] += 1
        time_sum[team] += t

 # 7.78
count = {5: 0, 4: 0, 3: 0, 2: 0}
while True:
    try:
        x = int(input().strip())
    except EOFError:
        break
    if x == 0:
        break
    if x in count:
        count[x] += 1

 # 7.79
wins = draws = losses = 0
while True:
    try:
        x = int(input().strip())
    except EOFError:
        break
    if x == 0 and wins + draws + losses == 0:
        break
    if x == 3:
        wins += 1
    elif x == 1:
        draws += 1
    elif x == 0:
        losses += 1
    else:
        pass

 # 7.80
games = 20
wins = draws = losses = 0
diff_greater_3 = diff_equal_3 = diff_less_3 = 0
points = 0
for i in range(1, games + 1):
    while True:
        try:
            parts = input().split()
        except EOFError:
            parts = []
        if parts:
            break
    if len(parts) >= 2:
        scored = int(parts[0])
        conceded = int(parts[1])
    else:
        scored = int(parts[0])
        conceded = int(input().strip())
    diff = scored - conceded
    if diff > 0:
        result = "выигрыш"
        wins += 1
        points += 3
    elif diff == 0:
        result = "ничья"
        draws += 1
        points += 1
    else:
        result = "поражение"
        losses += 1
    if diff > 3:
        diff_greater_3 += 1
    elif diff == 3:
        diff_equal_3 += 1
    elif diff < 3:
        diff_less_3 += 1

 # 7.81
def analyze_matches(results, single_as_scored=True):
    wins = draws = losses = 0
    for x in results:
        if x >= 10:
            scored = x // 10
            conceded = x % 10
        else:
            if single_as_scored:
                scored = x
                conceded = 0
            else:
                scored = 0
                conceded = x
        if scored > conceded:
            wins += 1
        elif scored == conceded:
            draws += 1
        else:
            losses += 1
    return wins, draws, losses

 # 7.82
def count_adjacent_pairs(arr):
    eq = bz = be = b5 = 0
    for i in range(len(arr) - 1):
        x, y = arr[i], arr[i+1]
        if x == y:
            eq += 1
        if x == 0 and y == 0:
            bz += 1
        if x % 2 == 0 and y % 2 == 0:
            be += 1
        if abs(x) % 10 == 5 and abs(y) % 10 == 5:
            b5 += 1
    return {'equal': eq, 'both_zero': bz, 'both_even': be, 'both_end_with_5': b5}

 # 7.83
def has_even(arr):
    return any(x % 2 == 0 for x in arr)

 # 7.84
def positives_at_most_five(arr):
    return sum(1 for x in arr if x > 0) <= 5

 # 7.85
def count_leq_33_2_is_multiple_of_4(arr):
    cnt = sum(1 for x in arr if x <= 33.2)
    return cnt % 4 == 0, cnt

 # 7.86
def count_less_than_20_equal_5(arr):
    return sum(1 for x in arr if x < 20) == 5

 # 7.87
def positive_count_multiple_of_3(arr):
    return sum(1 for x in arr if x > 0) % 3 == 0

 # 7.88
def negative_count_greater_than_k(arr, k):
    return sum(1 for x in arr if x < 0) > k

 # 7.89
def count_greater_m_is_multiple_of_p(arr, m, p):
    if p == 0:
        raise ValueError("p должен быть ненулевым целым")
    cnt = sum(1 for x in arr if x > m)
    return cnt % p == 0, cnt

 # 7.90
def no_threes(grades):
    return 3 not in grades

 # 7.91
def exactly_ten_no_rain(days):
    return days.count(0) == 10

 # 7.92
def has_two(grades):
    return 2 in grades

 # 7.93
def has_power_over(powers, threshold=200):
    return any(p > threshold for p in powers)

 # 7.94
def count_strict_local_maxima(seq):
    if len(seq) < 3:
        return 0
    cnt = 0
    for i in range(1, len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            cnt += 1
    return cnt

 # 7.95
def count_sign_changes(seq):
    if not seq:
        return 0
    cnt = 0
    for i in range(1, len(seq)):
        if seq[i] * seq[i-1] < 0:
            cnt += 1
    return cnt

 # 7.96
def first_adjacent_equal_index(seq):
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            return i
    return None

 # 7.97
def first_adjacent_equal_index_terminating(seq):
    n = len(seq)
    for i in range(1, n):
        if seq[i] == seq[i-1]:
            return i
    return None

 # 7.98
def first_adjacent_odds_index(seq):
    for i in range(1, len(seq)):
        if seq[i] % 2 == 1 and seq[i-1] % 2 == 1:
            return i
    return None

 # 7.99
def first_adjacent_even(seq):
    for i in range(1, len(seq)):
        if seq[i-1] % 2 == 0 and seq[i] % 2 == 0:
            return True, i
    return False, None

 # 7.100
def is_sorted_non_decreasing(seq):
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            return False, i+0
    return True, None

 # 7.101
def is_sorted_non_decreasing_until_marker(seq, marker=10000):
    return is_sorted_non_decreasing(seq)

 # 7.102
def is_sorted_non_increasing(seq):
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            return False, i+0
    return True, None

 # 7.103
def teams_order_by_points(seq):
    return is_sorted_non_increasing(seq)

 # 7.104
def all_equal(seq):
    if not seq:
        return True
    first = seq[0]
    for x in seq:
        if x != first:
            return False
    return True

 # 7.105
def all_equal_until_negative(seq):
    return all_equal(seq)















































