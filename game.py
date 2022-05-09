#have the function ask to choose rock, paper, or scissors
#have it iterate over the choices at random
#tell if you win, lose or tie


import random

my_choices = ['r', 'p', 's']
my_answers = ['you win!', 'you lose!', 'its a draw!']

question = input('Welcome! What is your choice? ')

def rock_paper_scissors(r, p, s):
  stored_value = random.choice(my_choices)
  if stored_value == r:
    print('you win!')
  elif stored_value == p:
    print('you lose!')
  elif stored_value == s:
    print('its a draw!')


rock_paper_scissors('r', 'p', 's')