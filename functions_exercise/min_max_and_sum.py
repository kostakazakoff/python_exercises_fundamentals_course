numbers = list(map(int, input().split()))


def min_max_sum(list_of_integers):
    print(f'The minimum number is {min(list_of_integers)}')
    print(f'The maximum number is {max(list_of_integers)}')
    print(f'The sum number is: {sum(list_of_integers)}')


min_max_sum(numbers)
