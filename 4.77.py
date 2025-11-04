 # 4.77
def on_board(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

def sign(x):
    return (x > 0) - (x < 0)

def is_between_strict(a, b, c, d, e, f):

    dx1 = e - a
    dy1 = f - b
    dx2 = c - a
    dy2 = d - b

    if dx1 == 0 and dx2 == 0:

        return (min(b, f) < d < max(b, f))
    if dy1 == 0 and dy2 == 0:

        return (min(a, e) < c < max(a, e))
    if abs(dx1) == abs(dy1) and abs(dx2) == abs(dy2) and sign(dx1) == sign(dx2) and sign(dy1) == sign(dy2):

        return (abs(dx2) < abs(dx1))
    return False

def black_attacks_square(pb, c, d, e, f):

    if not on_board(e, f) or (c == e and d == f):

        return False
    dx = abs(e - c)
    dy = abs(f - d)
    if pb == 'R':
        return (c == e or d == f)
    if pb == 'B':
        return (dx == dy and dx != 0)
    if pb == 'Q':
        return (c == e or d == f or dx == dy)
    if pb == 'N':
        return (dx, dy) in ((1, 2), (2, 1))
    if pb == 'K':
        return max(dx, dy) == 1 and not (dx == 0 and dy == 0)
    raise ValueError("Unknown piece for black: " + str(pb))

def white_can_move_and_be_safe(pw, a, b, c, d, e, f):

    if not (on_board(a, b) and on_board(c, d) and on_board(e, f)):
        return False
    if a == e and b == f:
        return False
    capturing = (e == c and f == d)
    dx = abs(e - a)
    dy = abs(f - b)

    legal = False
    if pw == 'R':
        if a == e or b == f:

            if is_between_strict(a, b, c, d, e, f):
                legal = False
            else:
                legal = True
    elif pw == 'B':
        if dx == dy and dx != 0:
            if is_between_strict(a, b, c, d, e, f):
                legal = False
            else:
                legal = True
    elif pw == 'Q':
        if (a == e or b == f) or (dx == dy and dx != 0):
            if is_between_strict(a, b, c, d, e, f):
                legal = False
            else:
                legal = True
    elif pw == 'N':
        legal = (dx, dy) in ((1, 2), (2, 1))
    elif pw == 'K':
        legal = max(dx, dy) == 1
    else:
        raise ValueError("Unknown piece for white: " + str(pw))

    if not legal:
        return False

    if capturing:
        return True

    return not black_attacks_square(pb=c_piece, c=c, d=d, e=e, f=f)

def can_white_move_safely(pw, pb, a, b, c, d, e, f):
    global c_piece
    c_piece = pb
    return white_can_move_and_be_safe(pw, a, b, c, d, e, f)

















