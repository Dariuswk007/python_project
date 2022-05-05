dnd_roles = ['Priest', 'Warrior', 'Berserker', 'Druid']  

characters_hp = [
  {'Marcov': 100},
  {'Draken': 200},
  {'Mileena': 180},
  {'Shyvanna': 120}
]

character_sheet = dict(zip(dnd_roles, characters_hp))

character_intro = f'This is the starting party for the next adventure!\n\n {character_sheet}.\n\n Start your new journey!'

#print(character_sheet)

print(character_intro)