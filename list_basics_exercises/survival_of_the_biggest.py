numbers = list(map(int, input().split()))
remove_count = int(input())

numbers_copy = numbers.copy()
numbers_copy.sort()
edited_list = numbers_copy[remove_count:]
numbers = [str(x) for x in numbers if x in edited_list]
numbers = ', '.join(numbers)
print(numbers)
