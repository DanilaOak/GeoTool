from math import pi, sqrt
from math import atan, cos, sin, degrees, radians

# Перевод угловых градусов минут и секунд в градусы
def angle(grad, min, sec):
    return grad * pi / 180 + min * pi / (180 * 60) + sec * pi / (180 * 60 * 60)

# Перевод градусов в угловые градусы минуты и секунды
def grad(angle):
    gr = int(angle)
    min = int(angle%1*60)
    sec = round(angle%1*60%1*60)
    return {"g":gr, "m":min, "sec":sec}

def direct_pr(grad, min, sec, x_a, y_a, d):
    a = angle(grad, min, sec)
    delta_x = round(d * cos(a), 2)
    delta_y = round(d * sin(a), 2)
    x_b = round(x_a + delta_x, 2)
    y_b = round(y_a + delta_y, 2)
    return {"delta_x":delta_x, "delta_y":delta_y, "x_b":x_b, "y_b":y_b}



# Обратная геодезическая задача
def inverse_pr(x_a, y_a, x_b, y_b):
    d_x = x_b - x_a
    d_y = y_b - y_a
    r = round(abs(degrees(atan(d_y/d_x))), 6)
    if d_x > 0 and d_y > 0:
        a = r
    elif d_x < 0 and d_y > 0:
        a = 180 - r
    elif d_x < 0 and d_y < 0:
        a = r + 180
    else:
        a = 360 - r
    d1 = round(d_x/cos(radians(a)), 2)
    d2 = round(d_y/sin(radians(a)), 2)
    d3 = round(sqrt(d_x**2 + d_y**2), 2)
    return {"d_x":d_x, "d_y":d_y, "r":r, "a":a, "d1":d1, "d2":d2, "d3":d3}


# print(inverse_pr(247.32, 870.54, 705.65, -567.83))
# print(grad(22.9868))
# x = direct_pr(grad=217, min=14, sec=23, x_a=25, y_a=140, d=124)
# print(x)
# print(x["delta_x"])
