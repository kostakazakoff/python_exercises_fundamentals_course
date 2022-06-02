integers_count = int(input())
integers = [int(input()) for _ in range(integers_count)]
command = input()
result = []

for i in integers:
    filter_integers = (
        (command == 'even' and i % 2 == 0),
        (command == 'odd' and i % 2 != 0),
        (command == 'positive' and i >= 0),
        (command == 'negative' and i < 0)
    )
    if any(filter_integers):
        result.append(i)

print(result)
