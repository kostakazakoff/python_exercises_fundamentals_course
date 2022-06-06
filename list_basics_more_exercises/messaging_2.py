numbers = input().split()
source = input()


def message_encode(strings_of_numbers, source_message):
    source_message = [x for x in source_message]
    message = ''
    for code in strings_of_numbers:
        i = sum(int(x) for x in code)
        if i > len(source_message):
            i %= len(source_message)
        message += source_message.pop(i)
    return message


print(message_encode(numbers, source))
