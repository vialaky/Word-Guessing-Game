import string
from random import choice


def get_word():
    """
    Reads a list of words from a text file and selects one word from it randomly.
    """
    with open('word_list.txt', 'r') as file:
        word_list = [line.strip() for line in file]
    return choice(word_list).upper()


def display_hangman(tries):
    """
    Getting the current state.
    """
    stages = [  # final state: head, torso, both arms, both legs
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # head, torso, both arms, one leg
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # head, torso, both arms
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # head, torso and one arm
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # head and torso
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # head
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # initial state
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def check_input(user_input):
    while not user_input.isalpha():
        print("It's not a text. Try again.")
        user_input = input()
    if len(user_input) == 1:
        while user_input not in string.ascii_letters:
            print('Please check the keyboard layout and try again:')
            user_input = input()
    elif len(user_input) > 1:
        while True:
            for ch in user_input:
                if ch not in string.ascii_letters:
                    print('Please check the keyboard layout and try again:')
                    user_input = input()
                    break
            else:
                break

    print(f'You entered: {user_input.upper()}')


def play(word):
    word_completion = '_' * len(word)  # string containing _ characters for each letter of the intended word
    guessed = False  # signal mark
    guessed_letters = []  # list of already guessed letters
    guessed_words = []  # list of already guessed words
    tries = 6  # number of attemps

    print("Let's play the game!")

    # Show the initial state
    print(display_hangman(tries))
    print(word_completion)

    while True:
        print('Enter the letter or whole word:')
        user_attemp = input()
        check_input(user_attemp)
        break


hidden_word = get_word()
print(hidden_word)
play(hidden_word)
