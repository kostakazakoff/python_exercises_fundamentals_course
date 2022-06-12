int_1 = int(input())
int_2 = int(input())


def factorial_division(a, b):
    factorial_1 = 1
    factorial_2 = 1
    for x in range(1, a + 1):
        factorial_1 *= x
    for y in range(1, b + 1):
        factorial_2 *= y
    return factorial_1 / factorial_2


print(f'{factorial_division(int_1, int_2):.2f}')
