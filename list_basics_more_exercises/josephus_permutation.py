content = input().split()
step = int(input())

index = 0
result = []
finished = False

while not finished:
    index += step - 1
    if index >= len(content):
        index %= len(content)
    result.append(content.pop(index))
    finished = len(content) == 0

separator = ','
print(f'[{separator.join(result)}]')
