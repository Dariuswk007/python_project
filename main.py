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

def flex_dice():
  greeting = input('What is your name? ')
  player = input(f'Hello, {greeting}! What side die would you like? Please choose 1-100: ')
  print(f'You chose a {player} sided die, roll for initiative!')
  player_roll = random.randrange(1, int(player))
  while True:
    action = input('enter r to roll: ')
    if action == 'r':
      print(f'You rolled {player_roll}!')
      return False
    else:
      print('Please roll again.')
  


flex_dice()


#create a class that determine whether an attack is super effective, not very effective, has no effect, or normal damage.



class Pokemon:

  def __init__(self, poke_one, poke_two):
    self.poke_one = poke_one
    self.poke_two = poke_two


  def introduction(self):
    intro = input(f'You sent out {self.poke_one}! Your opponent sends out {self.poke_two}!')
    action = input("What do you do?  \n 'Water Gun', 'Steel Claw', 'Earthquake', 'Faint Attack'\n\n ")
    if action == 'Water Gun':
      print("It's super effective!")
    elif action == 'Steel Claw':
      print("It's not very effective...")
    elif action == 'Earthquake':
      print("It has no effect!")
    else:
      print('A direct hit!')
      return action


entry_one = Pokemon('Blastoise', 'Moltres')
print(entry_one.introduction())