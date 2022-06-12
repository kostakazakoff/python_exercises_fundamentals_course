x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def longer_line(l1_x1, l1_y1, l1_x2, l1_y2, l2_x1, l2_y1, l2_x2, l2_y2):
    import math

    # Define the points coordinates
    p1 = [l1_x1, l1_y1]
    p2 = [l1_x2, l1_y2]
    p3 = [l2_x1, l2_y1]
    p4 = [l2_x2, l2_y2]

    # Measure the points distance from the center:
    point1_distance = abs(p1[0]) ** 2 + abs(p1[1]) ** 2
    point2_distance = abs(p2[0]) ** 2 + abs(p2[1]) ** 2

    # Creating a vector lines (nearest to the center point is the start point):
    if point2_distance < point1_distance:
        line_1 = [p2, p1]
    else:
        line_1 = [p1, p2]

    point3_distance = abs(p3[0]) ** 2 + abs(p3[1]) ** 2
    point4_distance = abs(p4[0]) ** 2 + abs(p4[1]) ** 2
    if point4_distance < point3_distance:
        line_2 = [p4, p3]
    else:
        line_2 = [p3, p4]

    # Measure the length of the lines:
    l1_length = (line_1[1][0] - line_1[0][0]) ** 2 + (line_1[1][1] - line_1[0][1]) ** 2
    l2_length = (line_2[1][0] - line_2[0][0]) ** 2 + (line_2[1][1] - line_2[0][1]) ** 2

    # Compare the length of the lines - the result is the longer line):
    if l2_length > l1_length:
        result = line_2
    else:
        result = line_1

    # Prepare the output:
    p1_output = tuple(math.floor(x) for x in result[0])
    p2_output = tuple(math.floor(x) for x in result[1])
    output = f'{str(p1_output)}{str(p2_output)}'
    return output


print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
