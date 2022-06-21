pokemons = list(map(int, input().split()))

pokemons[0] = pokemons.pop(-1)

print(pokemons)