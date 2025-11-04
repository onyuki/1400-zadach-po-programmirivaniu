# 3.39
n = int(input("Введите n (трёхзначное число, полученное как a c b): "))
a = n // 100
c = (n // 10) % 10
b = n % 10
x = 100*a + 10*b + c
print(x)

# 3.40
x = 456
print(x)

# 3.41
n = int(input("Введите n (1..999), последняя цифра n не равна 0: "))
c = n // 100
b = (n // 10) % 10
a = n % 10
x = 100*a + 10*b + c
print(x)

# 3.42
a2, a1, b = map(int, input("Введите a2 a1 b через пробел: ").split())
s = a2*10 + a1 + b
tens = s // 10
units = s % 10
print(tens, units)

# 3.43
a2, a1, b2, b1 = map(int, input("Введите a2 a1 b2 b1 через пробел: ").split())
s = (a2*10 + a1) + (b2*10 + b1)
tens = s // 10
units = s % 10
print(tens, units)

# 3.44
a3, a2, a1, b2, b1 = map(int, input("Введите a3 a2 a1 b2 b1 через пробел: ").split())
s = (a3*100 + a2*10 + a1) + (b2*10 + b1)
hundreds = s // 100
tens = (s // 10) % 10
units = s % 10
print(hundreds, tens, units)

import math

#3.45
def solve_3_45(k):
    pair_index = (k + 1) // 2
    number = 9 + pair_index
    if k % 2 == 1:
        digit = number // 10
    else:
        digit = number % 10
    return pair_index, number, digit

#3.46
def solve_3_46(k):

    triple_index = (k + 2) // 3
    number = 100 + triple_index
    r = k % 3
    if r == 1:
        digit = number // 100
    elif r == 2:
        digit = (number // 10) % 10
    else:
        digit = number % 10
    return triple_index, number, digit


#3.47
def hour_hand_angle(h, m, s):
    angle = (h % 12) * 30.0 + m * 0.5 + s * (0.5 / 60.0)
    return angle

#3.48
def hours_minutes_from_hour_angle(y):
    eps = 1e-9
    full_hours = int(math.floor((y + eps) / 30.0))
    rem = y - full_hours * 30.0
    if rem < 0:
        rem = 0.0
    full_minutes = int(math.floor((rem + eps) / 0.5))
    if full_minutes >= 60:
        full_minutes = 59
    return full_hours, full_minutes

#3.49
def minute_angle_and_full_time_from_hour_angle(alpha_rad):
    deg = alpha_rad * 180.0 / math.pi
    deg = deg % 360.0

    full_hours = int(math.floor(deg / 30.0 + 1e-12))
    rem_deg = deg - full_hours * 30.0
    if rem_deg < 0:
        rem_deg = 0.0

    full_minutes = int(math.floor(2.0 * rem_deg + 1e-12))

    minute_angle = 12.0 * rem_deg

    minute_angle = minute_angle % 360.0
    return minute_angle, full_hours, full_minutes

#3.50
import math

def min_minutes_until_events(h, m):

    D = 11/2 * m - 30 * h

    def find_min_t_for_targets(targets):
        best = None
        for target in targets:
            for k in range(0, 12):
                t = 2 * (target + 360 * k - D) / 11
                if t >= 0:
                    if best is None or t < best:
                        best = t
        return best

    t_coincide = find_min_t_for_targets([0])
    t_perp = find_min_t_for_targets([90, 270])

    full_minutes_coincide = int(math.floor(t_coincide + 1e-12))
    full_minutes_perp = int(math.floor(t_perp + 1e-12))

    return {
        't_coincide_minutes_real': t_coincide,
        't_perp_minutes_real': t_perp,
        't_coincide_full_minutes': full_minutes_coincide,
        't_perp_full_minutes': full_minutes_perp
    }

#3.51
def divisibility_flag(a, b):
    cond = (b != 0 and a % b == 0) or (a != 0 and b % a == 0)
    return 1 + (not cond)  







