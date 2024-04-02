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


hidden_word = get_word()
print(hidden_word)
play(hidden_word)
