all_points = []
for points in range(4):
    coordinates = []
    for point in range(2):
        xy = float(input())
        coordinates.append(xy)
    all_points.append(coordinates)
print(all_points)