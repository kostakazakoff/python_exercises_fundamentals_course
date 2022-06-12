def perfect_number(number):
    result = sum(n for n in range(1, number) if number % n == 0)
    if result == number:
        output = 'We have a perfect number!'
    else:
        output = "It's not so perfect."
    return output


num = int(input())
print(perfect_number(num))