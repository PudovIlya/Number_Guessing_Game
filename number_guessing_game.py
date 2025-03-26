from random import randint

# range
MINIMUM = 1
MAXIMUM = 100
# chances
EASY = 10
NORMAL = 7
HARD = 3


def welcome():
    print('WELCOME\n')

def set_difficulty():
    print('Please, set difficulty.\n'
    '1. Easy\n'
    '2. Normal\n'
    '3. Hard')
    difficulty_levels = {1: EASY,
                  2: NORMAL,
                  3: HARD}
    picked_level = input('Enter the corresponding number: ')
    while not picked_level.isnumeric() or not 0 < int(picked_level) < 4:
        picked_level = input('PLease, enter "1", "2" or "3".\n')
    return difficulty_levels[int(picked_level)]

def take_guess(): # type controll shall be implemented
    return int(input('Enter your guess: '))

def congratulate():
    print('You won!')

def give_hint(answer, guess):
    print(f'The number is {'less' if answer < guess else 'bigger'} then {guess}')

def lose_announcement():
    print('You lost!')

def main():
    welcome()
    chances = set_difficulty()
    answer = randint(MINIMUM, MAXIMUM)
    while chances > 0:
        guess = int(input(f'Enter your guess ({chances} attemptes lef): '))
        if answer == guess:
            congratulate()
            break
        chances -= 1
        give_hint(answer, guess)
    else:
        lose_announcement()


if __name__ == '__main__':
    main()
