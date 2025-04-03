from random import randint
from time import sleep, time


# range
MINIMUM = 1
MAXIMUM = 100
# chances
DIFFICULTIES = {'Easy': 10,
                'Normal': 7,
                'Hard': 3}


def validate_yes_or_no(user_answer: object) -> str:
    '''Ask input until it equal to 'y' or 'n'.'''
    while user_answer != 'y' and user_answer != 'n':
        user_answer = input('I don\'t understand you. PLease enter just "y" or "n" : ')
    return user_answer

def welcome() -> None:
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

def set_difficulty() -> tuple[str, bool]:
    '''To choose difficulty level and whether extended hints are on.
    Depends on DIFFICULTIES constant.'''
    print('Please, set difficulty.', end='\n\n')
    sleep(0.5)
    for counter, (level, chances) in enumerate(DIFFICULTIES.items(), 1):
        print(f'{counter}. {level} ({chances} chances)')
        sleep(0.3)
    print()
    picked_level = input(f'Enter the corresponding number [{'/'.join(str(num) for num in range(1, counter + 1))}]: ')
    while not picked_level.isnumeric() or not int(picked_level) in range(1, counter + 1):
        picked_level = input(f'PLease, enter one of these - {', '.join(str(num) for num in range(1, counter + 1))}: ')
    picked_level = list(DIFFICULTIES)[int(picked_level) - 1]
    print('...')
    sleep(0.5)
    print('OK, I got it.')
    print()
    hints_state = input('Do you want to turn hints on? [y/n] : ')
    hints_state = True if validate_yes_or_no(hints_state) == 'y' else False
    return picked_level, hints_state

def take_guess(chances:int) -> int:
    '''Return the guess number'''
    guess = input(f'Guess it ({chances} attempts left): ')
    while not guess.isnumeric():
        guess = input('The answer is integer number. Try again: ')
    return int(guess)

def congratulate() -> None:
    print('Congratulations!', end=' ', flush=True)
    sleep(0.5)
    print('You won!!!')

def give_hint(answer: int, guess: int, hints_state: bool = True) -> None:
    '''Give standard (lower/bigger) or extended hint depending on hints_state.'''
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

def lose_announcement(answer: int) -> None:
    print('Oops...', sep=' ', flush=True)
    sleep(1)
    print('You lost!')
    sleep(0.5)
    print(f'The number was {answer}.')

def play_round(difficulty: str, hints_state: bool = False) -> tuple[bool, int, int]:
    '''One number to guess with the difficulty difficulty level and standard or extended hints. 
    Returns whether user won or not, chances left (-1 if lost), time elapsed (-1 if lost).
    Depends on MINIMUM, MAXIMUM and DIFFICULTIES constants.'''
    answer = randint(MINIMUM, MAXIMUM)
    print()
    print(f'I\'m thinking of a number between {MINIMUM} and {MAXIMUM}.')
    sleep(1.5)
    count_start = time()
    chances = DIFFICULTIES[difficulty]
    while chances > 0:
        print()
        guess = take_guess(chances)
        sleep(0.15)
        print('...')
        sleep(0.15)
        if answer == guess:
            count_stop = time()
            elapsed_time = int(count_stop - count_start)
            congratulate()
            print(f'It took you {elapsed_time} seconds to guess.')
            victory = True
            break
        chances -= 1
        if chances > 0:
            give_hint(answer, guess, hints_state)
    else:
        print()
        lose_announcement(answer)
        victory = False
        elapsed_time = -1
    print()
    return victory, chances - 1, elapsed_time

def update_statistics(new_difficulty:str, new_hints:bool,
                      new_chances:int, new_time:int) -> bool:
    '''Write results in file_name file if they are better then written.
    Better results = more chances left or chances are same but new time is less. 
    Creates new file if it doesn't exist (in the program directory). 
    Compare results with the same difficulty level and hints state. 
    Returns wheather the results were updated.
    Results is written in the form: "difficulty hints chances time\\n" '''

    file_name = '_statistics(NGG).txt'

    def new_results_better(old_chances, old_time, new_cahnces, new_time):
        return old_chances < new_cahnces or (old_chances == new_chances and
                                             old_time > new_time)
    
    new_hints = int(new_hints) # easier to store bool in txt as int

    results_updated = False
    try:
        with open(file_name, 'r') as file_object:
            records = [line.strip().split() for line in file_object]
    except FileNotFoundError: 
        with open(file_name, 'w') as file_object:
            file_object.write(' '.join( (str(new_difficulty),
                                         str(new_hints),
                                         str(new_chances),
                                         str(new_time)) ) + '\n')
        results_updated = True
    else:
        for idx, (difficulty, hints, chances, time) in enumerate(records):
            if (difficulty, int(hints)) == (new_difficulty, new_hints):
                if new_results_better(int(chances), int(time),
                                       new_chances, new_time):
                    records[idx] = [difficulty, hints, str(new_chances), str(new_time)]
                    results_updated = True
                break
        else:
            records.append([new_difficulty, str(new_hints),
                            str(new_chances), str(new_time)])
            results_updated = True
        
        if results_updated:
            with open(file_name, 'w') as file_object:
                for record in records:
                    file_object.write(' '.join(record) + '\n')
    return results_updated

def main():
    welcome()
    sleep(0.5)
    difficulty, hints_state = set_difficulty()
    while True:
        victory, chances_left, time_elapsed = play_round(difficulty, hints_state)
        if victory:
            statistics_updated = update_statistics(difficulty, hints_state,
                                                   chances_left, time_elapsed)
            if statistics_updated:
                print('Wow! It\'s your new best:\n'
                    f'Difficulty:{difficulty:.>30}\n'
                    f'Hints used:{'Yes' if hints_state else 'No':.>30}\n'
                    f'Chances left:{chances_left:.>30}\n'
                    f'Time:{time_elapsed:.>30}\n')
        victory_message = 'You are amazing! It was SO fun. Play again?'
        lose_message = 'Cheer up! You almost did it. Try again?'
        message = victory_message if victory else lose_message
        answer = input(message + ' [y/n] : ')
        answer = validate_yes_or_no(answer)
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