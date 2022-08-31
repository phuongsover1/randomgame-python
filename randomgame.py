from random import randint
import sys


def run_guess(guess, answer, min, max):
    if (guess < int(min) or guess > int(max)):
        print(f'hey bozo, I said {min}~{max}')
    elif (guess > answer):
        print('Too large. Try again!')
    elif (guess < answer):
        print('Too small. Try again!')
    else:
        print('Correct! Congratulation.')
        return True
    return False


try:
    random = randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            guess = int(
                input(f'guess the number between {sys.argv[1]} and {sys.argv[2]}: '))
        except ValueError:
            print('Please enter valid number!')
            continue
        if (run_guess(guess, random, sys.argv[1], sys.argv[2])):
            break

except IndexError:
    print(
        'Please run randomgame.py with the bound [min,max]. Ex: python3 randomgame min max')
except ValueError:
    print('Please enter number or valid range start -> end (not end -> start)')
