#have the function ask to choose rock, paper, or scissors
#have it iterate over the choices at random
#tell if you win, lose or tie


import random

my_choices = ['r', 'p', 's']

question = input('Welcome! What is your choice? ')

def rock_paper_scissors(r, p, s):
  stored_value = random.choice(my_choices)
  if stored_value == r:
    print('you win!')
  elif stored_value == p:
    print('you lose!')
  else:
    print('its a draw!')

    return stored_value


rock_paper_scissors('r', 'p', 's')