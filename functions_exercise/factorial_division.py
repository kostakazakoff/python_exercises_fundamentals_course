def factorial_number(integer):
    for n in range(1, integer):
        integer *= n
    return integer


int_1 = int(input())
int_2 = int(input())
division = factorial_number(int_1) / factorial_number(int_2)
print(f'{division:.2f}')
