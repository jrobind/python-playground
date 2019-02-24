# Random number CLI game - to run, input a number to CLI, and a random number between
# zero and the one provided will be generated. The user must guess the correct number.
import random

base_num = raw_input('Please input a number: ')

def get_guess(base_num, repeat):
    if (repeat == True):
        return raw_input('Wrong! Guess again: ')
    else:
        return raw_input('Please guess a number between 0 and ' + base_num + '. ')

if (base_num == ''): 
    print('Please provide a number: ')
else:
    random_num = random.randint(0, int(base_num))
    guess = int(get_guess(base_num, False))

    # use a while loop
    while (random_num != guess):
        guess = int(get_guess(base_num, True))
    
    print('Well done! You guessed correct.')


