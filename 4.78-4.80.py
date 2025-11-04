 # 4.78

def same_color(a: int, b: int, c: int, d: int) -> bool:
    return (a + b) % 2 == (c + d) % 2

if __name__ == "__main__":
    a, b, c, d = map(int, input("a b c d: ").split())
    print("Да" if same_color(a, b, c, d) else "Нет")

 # 4.79

def is_triangle(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == "__main__":
    a, b, c = map(float, input("a b c: ").split())
    print("Да" if is_triangle(a, b, c) else "Нет")

 # 4.80

import math

def is_triangle(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)

def is_right_triangle(a: float, b: float, c: float, tol=1e-9) -> bool:
    if not is_triangle(a, b, c):
        return False
    x, y, z = sorted([a, b, c])
    return math.isclose(x*x + y*y, z*z, rel_tol=tol, abs_tol=tol)

if __name__ == "__main__":
    a, b, c = map(float, input("a b c: ").split())
    if not is_triangle(a, b, c):
        print("Треугольник не существует")
    else:
        print("Прямоугольный" if is_right_triangle(a, b, c) else "Не прямоугольный")




















