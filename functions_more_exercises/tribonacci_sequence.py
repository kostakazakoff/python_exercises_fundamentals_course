def tribonacci(count):
    tribonacci_numbers = [0, 0, 1]
    for i in range(count - 1):
        number = tribonacci_numbers[-1] + tribonacci_numbers[-2] + tribonacci_numbers[-3]
        tribonacci_numbers.append(number)
    return list(filter(lambda x: x != 0, tribonacci_numbers))


count_of_tribonacci_numbers = int(input())
result = tribonacci(count_of_tribonacci_numbers)
print(*result)
