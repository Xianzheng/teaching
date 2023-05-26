# computer generate a random number

# we need to guess random number


import random

random_number = random.randint(1, 1000)
i = 0
chances = 3


def run_guess():
    print('What number do you think it is?')
    answer = int(input())
    if answer == random_number:
        print('Goodjob! You got it right!')
        return True

    elif answer != random_number and random_number < answer:
        print("Oops! That's not right!")
        print('⬇️ The right number is smaller than', answer)
        print(' ')
        return False

    elif answer != random_number and random_number > answer:
        print("Oops! That's not right!")
        print('⬆️ The right number is bigger than', answer)
        print(' ')
        return False

# we have unlimited time to guess until we make a correct
while True:
    if run_guess() == True:
        break

import random
