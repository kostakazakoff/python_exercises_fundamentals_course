import sys

x = int(input())
y = int(input())
z = int(input())


def min_integer(n1, n2, n3):
    numbers = [n1, n2, n3]
    min_int = sys.maxsize
    for i in range(3):
        if numbers[i] < min_int:
            min_int = numbers[i]
    return min_int


print(min_integer(x, y, z))
