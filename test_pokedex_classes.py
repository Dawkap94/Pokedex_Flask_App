from pokedex_classes import PokemonInfo
import pytest

pokemons = ["bulbasaur", "ivysaur", "venusaur", "pidgey", "pidgeotto", "pidgeot"]


@pytest.mark.parametrize("created_class", pokemons)
def test_create_class(created_class):
    object = PokemonInfo(created_class)
    assert "class" in str(type(object))


@pytest.mark.parametrize("created_class", pokemons)
def test_pokemon_name(created_class):
    object = PokemonInfo(created_class)
    name = object.pokemon.name.upper()
    assert name == created_class.upper()


@pytest.mark.parametrize("created_class", ["bulbasaur", "ivysaur", "venusaur"])
def test_pokemon_number(created_class):
    object = PokemonInfo(created_class)
    number = object.pokemon.dex
    assert number in [1, 2, 3]


@pytest.mark.parametrize("created_class", ["bulbasaur", "ivysaur", "venusaur"])
def test_grass_poison_pokemons(created_class):
    object = PokemonInfo(created_class)
    type = object.type
    assert type == ['grass', 'poison']


@pytest.mark.parametrize("created_class", ["pidgey", "pidgeotto", "pidgeot"])
def test_flying_type_pokemons(created_class):
    object = PokemonInfo(created_class)
    type = object.type
    assert "flying" in type


@pytest.mark.parametrize("created_class", pokemons)
def test_vulnerabilities(created_class):
    object = PokemonInfo(created_class)
    vulnerabilities = object.get_vulnerability()
    assert type(vulnerabilities) is list


@pytest.mark.parametrize("created_class", pokemons)
def test_height_and_weight(created_class):
    object = PokemonInfo(created_class)
    height_and_weight = object.get_height_and_weight()
    assert type(height_and_weight) == list and type(height_and_weight[0]) == float or int


@pytest.mark.parametrize("created_class", pokemons)
def test_description_is_not_empty(created_class):
    object = PokemonInfo(created_class)
    description = object.get_pokemon_description()
    assert len(description) > 10 and type(description) == str


@pytest.mark.parametrize("created_class", pokemons)
def test_pokemon_has_attacks(created_class):
    object = PokemonInfo(created_class)
    attacks = object.get_pokemon_attacks()
    assert type(attacks) == dict and len(attacks) > 0
