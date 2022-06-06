def filter_numbers(num, command):
    if command == 'even':
        for n in num:
            if n % 2 == 0:
                output.append(n)
    elif command == 'odd':
        for n in num:
            if n % 2 != 0:
                output.append(n)
    elif command == 'negative':
        for n in num:
            if n < 0:
                output.append(n)
    elif command == 'positive':
        for n in num:
            if n >= 0:
                output.append(n)
    return(output)


lines = int(input())
num = []
output = []

for i in range(lines):
    n = int(input())
    num.append(n)

command = input()

print(filter_numbers(num, command))
