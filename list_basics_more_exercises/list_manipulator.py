numbers = input()
numbers = list(map(int, numbers.split()))
command = input()


def even_odd(definition, integers):
    output = []
    if definition == 'even':
        output = list(x for x in integers if x % 2 == 0)
    elif definition == 'odd':
        output = list(x for x in integers if x % 2 != 0)
    return output


while command != 'end':
    copy = []
    command = command.split()
    action = command[0]
    if action == 'exchange':
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print('Invalid index')
        else:
            numbers = numbers[(index + 1):] + numbers[:index + 1]

    elif action == 'max' or action == 'min':
        num_type = command[1]
        copy = even_odd(num_type, numbers)
        if len(copy) == 0:
            print('No matches')
        else:
            searched_number = min(copy) if action == 'min' else max(copy)
            numbers.reverse()
            searched_index = numbers.index(searched_number) + 1
            print(len(numbers) - searched_index)
            numbers.reverse()

    elif action == 'first' or action == 'last':
        result = []
        count = int(command[1])
        num_type = command[2]
        if len(numbers) >= count > 0:
            copy = even_odd(num_type, numbers)
            if action == 'first':
                result = [copy[x] for x in range(count) if len(copy) > x]
            elif action == 'last':
                copy.reverse()
                result = [copy[x] for x in range(count) if len(copy) > x]
                result.reverse()
            print(result)
        else:
            print('Invalid count')
    command = input()

print(numbers)
