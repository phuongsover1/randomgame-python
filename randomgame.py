from random import randint
import sys


def run_guess(guess, random):
    if (guess < int(sys.argv[1]) or guess > int(sys.argv[2])):
        print(f'hey bozo, I said {sys.argv[1]}~{sys.argv[2]}')
    elif (guess > random):
        print('Too large. Try again!')
    elif (guess < random):
        print('Too small. Try again!')
    else:
        print('Correct! Congratulation.')
        return True


try:
    random = randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            guess = int(
                input(f'guess the number between {sys.argv[1]} and {sys.argv[2]}: '))
        except ValueError:
            print('Please enter valid number!')
            continue
        if (run_guess(guess, random)):
            break

except IndexError:
    print(
        'Please run randomgame.py with the bound [min,max]. Ex: python3 randomgame min max')
except ValueError:
    print('Please enter number or valid range start -> end (not end -> start)')
