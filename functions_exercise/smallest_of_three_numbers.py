def min_integer(int_1, int_2, int_3):
    numbers = (int_1, int_2, int_3)
    min_int = min(numbers)
    return min_int


x = int(input())
y = int(input())
z = int(input())

print(min_integer(x, y, z))
