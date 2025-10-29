import math

# 2.23
def task_2_23(a, b):
    perimeter = 2 * (a + b)
    area = a * b
    diagonal = math.sqrt(a**2 + b**2)
    return perimeter, area, diagonal


# 2.24
def task_2_24(x, y):
    return x + y, x - y, x * y, x / y if y != 0 else None


# 2.25
def task_2_25(a, b, c):
    volume = a * b * c
    side_area = 2 * c * (a + b)
    return volume, side_area


# 2.26
def task_2_26(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# 2.27
def task_2_27(a, b, h):
    leg = math.sqrt(((b - a) / 2)**2 + h**2)
    perimeter = a + b + 2 * leg
    return perimeter


# 2.28
def task_2_28(a, b, angle_deg):
    angle_rad = math.radians(angle_deg)
    h = (b - a) / 2 * math.tan(angle_rad)
    area = (a + b) / 2 * h
    return area


# 2.29
def task_2_29(x1, y1, x2, y2, x3, y3):
    a = math.dist((x1, y1), (x2, y2))
    b = math.dist((x2, y2), (x3, y3))
    c = math.dist((x3, y3), (x1, y1))
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return perimeter, area


# 2.30
def task_2_30(x1, y1, x2, y2, x3, y3, x4, y4):
    def triangle_area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)
    area = triangle_area(x1, y1, x2, y2, x3, y3) + triangle_area(x1, y1, x3, y3, x4, y4)
    return area


# 2.31
def task_2_31(price_candy, price_cookie, price_apple, x, y, z):
    return price_candy * x + price_cookie * y + price_apple * z


# 2.32
def task_2_32(monitor, system_unit, keyboard, mouse, n):
    price_one = monitor + system_unit + keyboard + mouse
    return price_one * n


# 2.33
def task_2_33(tanya_age, mitya_age, x, y):
    avg = (tanya_age + mitya_age + x + y) / 4
    diff_tanya = abs(tanya_age - avg)
    diff_mitya = abs(mitya_age - avg)
    return avg, diff_tanya, diff_mitya


# 2.34
def task_2_34(v1, v2, s):
    time = s / (v1 + v2)
    return time


# 2.35
def task_2_35(v1, v2, s):
    dist_after_30 = abs(v1 - v2) * 0.5  # 0.5 часа = 30 минут
    time_to_meet = s / (v1 - v2) if v1 > v2 else None
    return dist_after_30, time_to_meet


# 2.36
def task_2_36(celsius):
    fahrenheit = celsius * 1.8 + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

