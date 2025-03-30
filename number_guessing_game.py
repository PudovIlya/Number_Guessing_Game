from random import randint
from time import sleep, time


# range
MINIMUM = 1
MAXIMUM = 100
# chances
EASY = 10
NORMAL = 7
HARD = 3


def validate_yes_or_no(user_answer):
    while user_answer != 'y' and user_answer != 'n':
        user_answer = input('I don\'t understand you. PLease enter just "y" or "n" : ')
    return user_answer

def welcome():
    flush_print = lambda message: print(message, end='', flush=True)
    print('_' * 61, end='\n\n')
    flush_print('Welcome to the one...')
    sleep(0.5)
    flush_print(' the only...')
    sleep(0.5)
    flush_print(' ...')
    sleep(1)
    print('\n')
    print('NUMBER GUESSING GAME ! ! !'.center(60))
    sleep(0.5)
    print()
    for _ in range(10):
        sleep(0.2)
        flush_print(':D :D ')
    print('\n')

def set_difficulty():
    difficulty_levels = {1: EASY,
                         2: NORMAL,
                         3: HARD}
    print('Please, set difficulty.', end='\n\n')
    sleep(0.5)
    print(f'1. Easy ({EASY} chances)')
    sleep(0.3)
    print(f'2. Normal ({NORMAL} chances)')
    sleep(0.3)
    print(f'3. Hard ({HARD} chances)') 
    sleep(0.3)
    print()
    picked_level = input('Enter the corresponding number [1/2/3]: ')
    while not picked_level.isnumeric() or not 0 < int(picked_level) < 4:
        picked_level = input('PLease, enter "1", "2" or "3": ')
    print('...')
    sleep(0.5)
    print('OK, I got it.')
    print()
    hints_state = input('Do you want to turn hints on? [y/n] : ')
    hints_state = validate_yes_or_no(hints_state)
    return difficulty_levels[int(picked_level)], True if hints_state == 'y' else False

def take_guess(chances):
    guess = input(f'Guess it ({chances} attempts left): ')
    while not guess.isnumeric():
        guess = input('The answer is integer number. Try again: ')
    return int(guess)

def congratulate():
    print('Congratulations!', end=' ', flush=True)
    sleep(0.5)
    print('You won!!!')

def give_hint(answer, guess, hints_state=True):
    print(f'The number is {'less' if answer < guess else 'bigger'} then {guess}')
    if hints_state:
        if answer == 1:
            print('*Hint: I have to leave you ALONE now ;)')
        elif answer == 2:
            print('*Hint: I don\'t EVEN know, how to guess it ;)')
        elif answer == 3:
            print('*Hint: It\'s ODD, to give a hint there ;)')
        else:
            random_number = randint(2, int(answer ** 0.5))
            print(f'*Hint: the number is {'not ' if answer % random_number != 0 else ''}'
                f'devisible by {random_number}')

def lose_announcement(answer):
    print('Oops...', sep=' ', flush=True)
    sleep(1)
    print('You lost!')
    sleep(0.5)
    print(f'The number was {answer}.')

def play_round(chances, hints_state=False):
    answer = randint(MINIMUM, MAXIMUM)
    print()
    print(f'I\'m thinking of a number between {MINIMUM} and {MAXIMUM}.')
    sleep(1.5)
    count_start = time()
    while chances > 0:
        print()
        guess = take_guess(chances)
        sleep(0.15)
        print('...')
        sleep(0.15)
        if answer == guess:
            count_stop = time()
            congratulate()
            print(f'It took you {int(count_stop - count_start)} seconds to guess.')
            victory = True
            break
        chances -= 1
        if chances > 0:
            give_hint(answer, guess, hints_state)
    else:
        print()
        lose_announcement(answer)
        victory = False
    print()
    return victory

def main():
    welcome()
    sleep(0.5)
    chances, hints_state = set_difficulty()
    while True:
        victory = play_round(chances, hints_state)
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
