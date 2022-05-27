year = int(input())
a_happy_year = False

while not a_happy_year:
    year += 1
    # the set doesn't content an equal elements in the string
    # so, we can use it to check out if all the elements in the string are different:
    a_happy_year = len(set(str(year))) >= len(str(year))

print(year)