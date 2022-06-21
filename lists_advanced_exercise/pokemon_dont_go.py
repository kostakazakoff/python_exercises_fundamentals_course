def bigger_or_smaller(pokemon, removed_value):
    if pokemon <= removed_value:
        pokemon += removed_value
    else:
        pokemon -= removed_value
    return pokemon


def pokemon_catch(pokemons, index):
    if index < 0:
        pokemons[0] = pokemons[-1]
        removed_pokemon = pokemons[0]
    elif index >= len(pokemons):
        pokemons[-1] = pokemons[0]
        removed_pokemon = pokemons[-1]
    else:
        removed_pokemon = pokemons.pop(index)
    pokemons = [bigger_or_smaller(indexed_pokemon, removed_pokemon) for indexed_pokemon in pokemons]
    return removed_pokemon, pokemons


list_of_pokemons = list(map(int, input().split()))
total = 0

while len(list_of_pokemons) > 0:
    i = int(input())
    removed, list_of_pokemons = pokemon_catch(list_of_pokemons, i)
    total += removed

print(total)
