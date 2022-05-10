# dnd_roles = ['Priest', 'Warrior', 'Berserker', 'Druid']  

# characters_hp = [
#   {'Marcov': 100},
#   {'Draken': 200},
#   {'Mileena': 180},
#   {'Shyvanna': 120}
# ]

# character_sheet = dict(zip(dnd_roles, characters_hp))

# character_intro = f'This is the starting party for the next adventure!\n\n {character_sheet}.\n\n Start your new journey!'

# #print(character_sheet)

# print(character_intro)

import random

def dnd_dice_generator():
  number = random.randint(0, 20)
  if number > 1 and number < 20:
    print('Your attack hits!')
  elif number == 20:
    print('You score a critical hit!')
  elif number == 0:
    print('Sorry, your attack missed!')
  else:
    print('Nothing happened.')
  
  return number


dnd_dice_generator()

# def char_interaction(name, dnd_dice_generator):
#   interaction = name + str(dnd_dice_generator)
#   print(interaction)

# char_interaction('mileena', dnd_dice_generator())

# Mileena, Your attack hits!