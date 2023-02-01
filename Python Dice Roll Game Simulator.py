import random

min_value = 1
max_value = 6

def roll_dice():
    return random.randint(min_value, max_value)

roll_again = 'Yes'
while roll_again.lower() in ['yes', 'y']:
    print('Rolling the dices...')
    print('The Values are:')
    print(roll_dice(), roll_dice())
    roll_again = input('Roll the dices again? (Yes/No)')
