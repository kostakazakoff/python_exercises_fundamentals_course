count_of_numbers = int(input())


def tribonacci(count):
    tribonacci_numbers = [0, 0, 1]
    for i in range(count - 1):
        number = tribonacci_numbers[i] + tribonacci_numbers[i + 1] + tribonacci_numbers[i + 2]
        tribonacci_numbers.append(number)
    tribonacci_numbers = list(filter(lambda x: x != 0, tribonacci_numbers))
    return tribonacci_numbers


result = tribonacci(count_of_numbers)
print(*result)
