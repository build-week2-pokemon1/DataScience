"""
c.abilities - abilities: [{ ability: { name: "battle-bond", url: "" } }]
c.abilities.ability.name = "battle-bond"

c.base_experience - base experience: 239

c.forms - forms: [{ name: "greninja-battle-bond", url: "" }]

- game_indices: []

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
    if pokemon == None:
        return

    for move in pokemon.moves:

        s = ''
        if move.move.power == None:
            s = pokemon_name + ',' + move.move.name + ','
        else:
            s = pokemon_name + ',' + \
                  move.move.name + ',' + \
                  str(move.move.power)
        print(s)
        f.write(s + '\n')

df = pd.read_csv('./Pokemon_cleaned.csv', header=0)
names = df.Name.values

def print_info(info):
    print(info._1, ',', info._2, ',', info._3)

with open('./pokemon_moves.csv', 'w') as f:
    for name in names:
        try:
            f.write('name,move,move_points')
            pokemon_info(name, pb.pokemon(name.lower()), f)
        except ValueError as err:
            print(err)
