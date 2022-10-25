import collections

import pypokedex
import requests
from opposite_types import opposite_types, all_evolutions


class PokemonInfo:
    def __init__(self, name):
        self.pokemon = pypokedex.get(name=name)
        self.name = name
        self.number = self.pokemon.dex
        self.image = self.pokemon.sprites.front["default"]
        self.type = self.pokemon.types

    def get_pokemon_description(self):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.name.lower()}")
        description = response.json().get("flavor_text_entries")[1]["flavor_text"].replace("\n", " ").replace("", " ")
        return description

    def get_pokemon_attacks(self):
        pkmn_moves = {move.level: move.name.replace("-", " ") for move in self.pokemon.moves["red-blue"] if move.level}
        sorted_pokemon_dict = collections.OrderedDict(sorted(pkmn_moves.items()))
        sorted_dict = {}
        for k, v in sorted_pokemon_dict.items():
            if v not in sorted_dict.values():
                sorted_dict[k] = v
        return sorted_dict

    def get_vulnerability(self):
        enemies_list = [opposite_types[pkmn_type] for pkmn_type in self.pokemon.types]
        parsed_enemy_list = [elem for elem in enemies_list if type(elem) != list]
        for elem in enemies_list:
            if type(elem) == list:
                for item in elem:
                    parsed_enemy_list.append(item)
        return parsed_enemy_list

    def get_stats(self):
        pokemon_stats = {"Atk": self.pokemon.base_stats.attack, "Def": self.pokemon.base_stats.defense,
                         "Speed": self.pokemon.base_stats.speed, "Hp": self.pokemon.base_stats.hp}
        return pokemon_stats

    def get_height_and_weight(self):
        height_and_weight = [round(self.pokemon.height * 0.1, 2), round(self.pokemon.weight * 0.1, 2)]
        return height_and_weight

    def get_evolutions(self):
        for elem in all_evolutions:
            if self.pokemon.name in elem:
                return elem

    def get_evolutions_pictures(self):
        new_list = []
        for elem in all_evolutions:
            if self.pokemon.name in elem:
                pokemons_evolution = elem
                for pkmns in pokemons_evolution:
                    new_list.append(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pypokedex.get(name=pkmns).dex}.png")
        return new_list


def main():
    name = input("Name: ")


if __name__ == '__main__':
    main()
