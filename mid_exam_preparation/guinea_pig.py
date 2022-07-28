food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000


def enough(f, h, c):
    return f > 0 and h > 0 and c > 0


for day in range(1, 31):
    food -= 300
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= pig_weight / 3
    if not enough(food, hay, cover):
        print('Merry must go to the pet store!')
        break
else:
    print(f'Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f},'
          f' Cover: {cover / 1000:.2f}.')
