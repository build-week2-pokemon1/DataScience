"""
We will explore the API at: https://pokeapi.co/docs/v2.html/
using the python library: https://github.com/PokeAPI/pokebase

The idea is to gather information that will help us select
the next best Pokemon. So basically we're ranking Pokemon.

moves have points associated with them, so we can:
- Get a list of move/point pairs for a pokemon
- Add up all the move_points for that pokemon
- The pokemon with the largest move_points is the best.
- We also have to consider the Total points from
this table: https://www.kaggle.com/abcsds/pokemon

Unfortunately, after getting this information, I found out that
half of the moves are not associated with any points. So, adding
up the move points will not give us the true picture.
I could assign points to those moves myself, but I'm not that
pokemon literate. Here are the moves that are missing points for
Bulbasaur:
swords-dance, growl, leech-seed, growth, poison-powder,
sleep-powder, string-shot, toxic, mimic, double-team, defense-curl,
light-screen, reflect, bide, amnesia, flash, rest, substitute,
curse, protect, endure, charm, swagger, attract, sleep-talk, return,
frustration, safeguard, sweet-scent, synthesis, sunny-day, ... etc.

Some pokemon have more than 150 moves. If half are without points,
it's no use trying to put points on them.

c = pb.pokemon('bulbasaur')
c.abilities - abilities: [{ ability: { name: "battle-bond", url: "" } }]
c.abilities.ability.name = "battle-bond"

c.base_experience - base experience: 239

c.forms - forms: [{ name: "greninja-battle-bond", url: "" }]

c.game_indices: []

c.height - height: 15

c.held_items - held_items: []

c.id - id: 10116

c.is_default - is_default: false

c.moves - moves: [ { move: { name: "pound"},
             version_group_details: [
                { level_learned_at: 1,
                  move_learn_method: { name: "level-up" }
                  version_group: { name: "ultra-sun-ultra-moon" } },
                { level_learned_at: 1,
                  move_learn_method: { name: "level-up" }
                  version_group: { name: "sun-moon" } },
                ... ]
c.moves[0].move.name = "pound"
c.moves[0].version_group_details[0]['level_learned_at'] = 1
c.moves[0].version_group_details[0]['move_learn_method']['name'] = "level-up"

c.name - name: "greninja-battle-bond"

c.order - order: 760

c.species.name - species: { name: "greninja" }

- sprites: { back_default: null, back_female: null, back_shiny: null, ... }

c.stats- stats: [ { base_stat: 122, effort: 3,
             stat: { "name: "speed" } },
           { base_stat: 71,
             effort: 0,
             stat: { name: "special-defense" }},
           ... ]
c.stats[0].base_stat = 122
c.stats[0].effort
c.stats[0].stat['name']

- types: [ {type: { name: "dark" }, {type: {name: "water"}}, ... ]
c.weight - weight: 400
"""
import pokebase as pb
import pandas as pd


def pokemon_info(pokemon_name, pokemon, f):
    """Get move data for this pokemon"""
    if pokemon is None:
        return

    for move in pokemon.moves:

        s = ''
        if move.move.power is None:
            s = pokemon_name + ',' + move.move.name + ','
        else:
            s = pokemon_name + ',' + \
                  move.move.name + ',' + \
                  str(move.move.power)
        print(s)
        f.write(s + '\n')


def pokemon_moves(names):
    """For each pokemon in our list, get the move data"""

    with open('./pokemon_moves.csv', 'w') as f:
        for name in names:
            try:
                pokemon_info(name, pb.pokemon(name.lower()), f)
            except ValueError as err:
                print(err)


df = pd.read_csv('./Pokemon_cleaned.csv', header=0)
pokemon_moves(df.Name.values)
