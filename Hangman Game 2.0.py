import random

# Hangman stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Hangman logo
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# Reduced word list with hints
word_list = [
    ('abruptly', 'Sudden or unexpected change'),
    ('absurd', 'Wildly unreasonable'),
    ('avenue', 'A wide street in a city'),
    ('awkward', 'Lacking grace or ease'),
    ('bikini', 'A two-piece swimsuit'),
    ('cobweb', 'A spider’s web'),
    ('fuchsia', 'A bright pinkish-purple color'),
    ('galaxy', 'A system of stars, planets, and dust'),
    ('gizmo', 'A small mechanical device'),
    ('haiku', 'A form of Japanese poetry'),
    ('jelly', 'A sweet spread made from fruit'),
    ('kayak', 'A small narrow watercraft'),
    ('lucky', 'Fortunate or blessed'),
    ('microwave', 'An appliance for heating food'),
    ('onyx', 'A black gemstone'),
    ('pajama', 'Loose-fitting clothes for sleeping'),
    ('quiz', 'A test of knowledge'),
    ('vortex', 'A whirling mass of fluid'),
    ('wizard', 'A person with magical powers'),
    ('zodiac', 'A circle of twelve signs') 
]

chosen_word, hint = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Provide the hint at the start
print(f"Hint: {hint}")

# Create blanks
display = ['_'] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was '{chosen_word}'.")

    # Join all the elements in the list and turn it into a string.
    print(' '.join(display))

    # Check if user has got all letters
    if '_' not in display:
        end_of_game = True
        print("You win.")

    # Print the hangman stage
    print(stages[lives])
