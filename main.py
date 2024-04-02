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

    return user_input.upper()


def show_guessed_letter(completion, user_input):
    print('You guessed the letter!')
    for i in range(len(hidden_word)):
        if hidden_word[i] == user_input:
            completion = completion[:i] + user_input + completion[i + 1:]
    return completion


def play(word):
    word_completion = '_' * len(word)  # string containing _ characters for each letter of the intended word
    guessed = False  # signal mark
    guessed_letters = []  # list of already guessed letters
    guessed_words = []  # list of already guessed words
    tries = 6  # number of attemps

    print("Let's play the game!")

    while True:

        # Show the initial state
        print(display_hangman(tries))
        print(word_completion)

        print('Enter the letter or whole word:')
        user_attemp = input()

        user_attemp = check_input(user_attemp)

        if len(user_attemp) == 1 and user_attemp in guessed_letters:
            print('This letter has already been guessed. Try again.')
            continue
        elif len(user_attemp) > 1 and user_attemp in guessed_words:
            print('This word has already been guessed. Try again.')
            continue

        if len(user_attemp) == 1 and user_attemp in word:
            word_completion = show_guessed_letter(word_completion, user_attemp)
            guessed_letters.append(user_attemp)




        else:
            tries -= 1
            if len(user_attemp) == 1:
                guessed_letters.append(user_attemp)
            elif len(user_attemp) > 1:
                guessed_words.append(user_attemp)


# Start the game
hidden_word = get_word()
print(hidden_word)
play(hidden_word)
