num = int(input())


def loading_bar(percent):
    x = int(percent / 10)
    loadbar = '[' + '%' * x + '.' * (10 - x) + ']'
    if percent >= 100:
        message = '100% Complete!\n' + loadbar
    if percent < 100:
        message = f'{percent}% {loadbar}\nStill loading...'
    return message


print(loading_bar(num))
