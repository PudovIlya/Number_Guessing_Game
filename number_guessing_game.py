from random import randint

# range
MINIMUM = 1
MAXIMUM = 100
# chances
EASY = 10
NORMAL = 7
HARD = 3


def welcome():
    print('\nWELCOME!\n')

def set_difficulty():
    difficulty_levels = {1: EASY,
                         2: NORMAL,
                         3: HARD}
    print('Please, set difficulty.\n\n'
    f'1. Easy ({EASY} chances)\n'
    f'2. Normal ({NORMAL} chances)\n'
    f'3. Hard ({HARD} chances)\n')
    picked_level = input('Enter the corresponding number: ')
    while not picked_level.isnumeric() or not 0 < int(picked_level) < 4:
        picked_level = input('PLease, enter "1", "2" or "3".\n')
    print()
    print('OK, I got it.')
    return difficulty_levels[int(picked_level)]

def take_guess(chances): # type controll shall be implemented
    guess = input(f'Guess it ({chances} attempts left): ')
    while not guess.isnumeric():
        guess = input('The answer is integer number. Try again: ')
    return int(guess)

def congratulate():
    print('\nYou won!\n')

def give_hint(answer, guess):
    print(f'The number is {'less' if answer < guess else 'bigger'} then {guess}')

def lose_announcement(answer):
    print(f'\nOops... You lost!\nThe number was {answer}.')

def main():
    welcome()
    chances = set_difficulty()
    answer = randint(MINIMUM, MAXIMUM)
    print()
    print(f'I\'m thinking of a number between {MINIMUM} and {MAXIMUM}.')
    while chances > 0:
        print()
        guess = take_guess(chances)
        if answer == guess:
            congratulate()
            break
        chances -= 1
        give_hint(answer, guess)
    else:
        lose_announcement(answer)


if __name__ == '__main__':
    main()