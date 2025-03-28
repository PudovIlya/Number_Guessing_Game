from random import randint
from time import sleep


# range
MINIMUM = 1
MAXIMUM = 100
# chances
EASY = 10
NORMAL = 7
HARD = 3


def welcome():
    flush_print = lambda message: print(message, end='', flush=True)
    print('_' * 61, end='\n\n')
    flush_print('Welcome to the one...')
    sleep(1)
    flush_print(' the only...')
    sleep(1)
    flush_print(' ...')
    sleep(1.5)
    print('\n')
    print('NUMBER GUESSING GAME ! ! !'.center(60))
    sleep(0.5)
    print()
    for _ in range(21):
        sleep(0.01)
        flush_print(':D ')
    print('\n')

def set_difficulty():
    difficulty_levels = {1: EASY,
                         2: NORMAL,
                         3: HARD}
    print('Please, set difficulty.', end='\n\n')
    sleep(1.5)
    print(f'1. Easy ({EASY} chances)\n'
    f'2. Normal ({NORMAL} chances)\n'
    f'3. Hard ({HARD} chances)\n') # make them pop one by one
    picked_level = input('Enter the corresponding number [1/2/3]: ')
    while not picked_level.isnumeric() or not 0 < int(picked_level) < 4:
        picked_level = input('PLease, enter "1", "2" or "3": ')
    print('...')
    sleep(0.5)
    print('OK, I got it.')
    return difficulty_levels[int(picked_level)]

def take_guess(chances):
    guess = input(f'Guess it ({chances} attempts left): ')
    while not guess.isnumeric():
        guess = input('The answer is integer number. Try again: ')
    return int(guess)

def congratulate():
    print('Congratulations!', end=' ', flush=True)
    sleep(0.5)
    print('You won!!!')

def give_hint(answer, guess):
    print(f'The number is {'less' if answer < guess else 'bigger'} then {guess}')

def lose_announcement(answer):
    print('Oops...', sep=' ', flush=True)
    sleep(1)
    print('You lost!')
    sleep(0.5)
    print(f'The number was {answer}.')

def play_round(chances):
    answer = randint(MINIMUM, MAXIMUM)
    print()
    print(f'I\'m thinking of a number between {MINIMUM} and {MAXIMUM}.')
    sleep(1.5)
    while chances > 0:
        print()
        guess = take_guess(chances)
        sleep(0.15)
        print('...')
        sleep(0.15)
        if answer == guess:
            congratulate()
            victory = True
            break
        chances -= 1
        print()
        give_hint(answer, guess) # no need for hint, when you are out of chances
    else:
        print()
        lose_announcement(answer)
        victory = False
    print()
    return victory

def main():
    welcome()
    sleep(1)
    chances = set_difficulty()
    while True:
        victory = play_round(chances)
        victory_message = 'You are amazing! It was SO fun. Play again?'
        lose_message = 'Cheer up! You almost did it. Try again?'
        message = victory_message if victory else lose_message
        answer = input(message + ' [y/n] : ')
        while answer != 'y' and answer != 'n':
            answer = input('I don\'t understand you. PLease enter just "y" or "n" : ')
        if answer == 'n':
            print()
            print('Well, it was fun!',  flush=True, end=' ')
            sleep(0.5)
            print('Bye!',  flush=True, end=' ')
            sleep(0.5)
            print('\n')
            break
if __name__ == '__main__':
    main()