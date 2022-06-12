n1 = int(input())
n2 = int(input())
n3 = int(input())


def multiplication_sign(a, b, c):
    numbers = [n1, n2, n3]
    zero = numbers.count(0) > 0
    negative_numbers = list(filter(lambda x: x < 0, numbers))
    negative = len(negative_numbers) % 2 != 0 and not zero

    if negative:
        sign = 'negative'
    elif zero:
        sign = 'zero'
    else:
        sign = 'positive'

    return sign


print(multiplication_sign(n1, n2, n3))
