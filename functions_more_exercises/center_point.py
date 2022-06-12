import math

f1 = float(input())
f2 = float(input())
s1 = float(input())
s2 = float(input())


def nearest_to_center(x1, y1, x2, y2):
    point1_result = tuple(math.floor(x) for x in [x1, y1])
    point2_result = tuple(math.floor(x) for x in [x2, y2])
    point1_distance = abs(x1) ** 2 + abs(y1) ** 2
    point2_distance = abs(x2) ** 2 + abs(y2) ** 2
    if point2_distance < point1_distance:
        result = point2_result
    else:
        result = point1_result
    return result


print(nearest_to_center(f1, f2, s1, s2))
