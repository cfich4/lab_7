#SDM: make a hangman game where each part of the game is written as a function, and the main game loop is run inside
#of a function which calls all the other smaller functions. Give every function on a docstring which explains all the inputs, 
#the general purpose of the function, and any outputs. If the secret word to guess is "apple", then the initial blanks shown to 
#the player should appear like "_ _ _ _ _", and then the player will be given the option to put in single letter guess. If the
#guess is correct, the blanks will be updated, like so "_ p p _ _" for the initial guess "p", else, if the user is wring, then 1
#life point will be subtracted from the initial 5, and the game will display a win message if the player completely guesses the enitre word
#before running out of life points, else, the game will display a lose message if the player runs out of life points first.



#e.g.
#playing = True
#while playing
#def run_game_loop():
#   print_welcome_message():
#   random_word = generate_random_word()
#   blanks = generare_blanks(random_word)
#   display_current_blanks(blanks)
#   answer = get_user_answer()
#   dnswer_valid = check_validity(random_word, answer)
#   if (answer_valid):
#       blanks = update_blanks(random_word, blanks, answer)
    # else: 
#       lives = lives - 1
#   if(lives == 0):
    #display_game_lost_message()
    #playing = False
#run_game_loop()

import random

def print_welcome_message():
    '''No inputs or outputs. This function simply prints a welcome message to greet the player.'''
    print("Welcome to hangman 👤🪓🩸")


def generate_random_word():
    '''No inputs. This function simply gets a random word choice from a list of words and returns it.'''
    words_list = ["bubbles", "monster", "zebra", "saxophone", "clarinet", "pickles", "procrastinate", "bat"]
    return random.choice(words_list)

def generate_blanks(word_input):
    '''This function takes in the secret word and generates a new string that has as many underscores as the 
    the scret word has letters and then returns this new string.'''
    new_blanks = ""
    for char in word_input:
        new_blanks += ("_")
    return new_blanks

def display_current_blanks(blanks_input):
    '''This function takes in the string of underscores representing the player's in-game progress on guessing the secret word, 
    and displays the chas spread out each by one space to the command line. This function does not return anything.'''
    blanks_display = ""
    for char in blanks_input:
        blanks_display += char + " "
    print(f"Current blanks: {blanks_input}")

def get_user_answer():
    '''This function takes no inputs. It promts the player to enter in a letter guess, and the function then reutrns that letter.'''
    letter_guess = input("Please enter a letter guess: ")
    return letter_guess

def check_validity(secret_word, letter_guess):
    '''Takes in the secret word and the player's letter guess and returns True if the letter guess is in the secret word'''
    return letter_guess in secret_word

def update_blanks(secret_word, current_blanks, letter_guess):
    '''Takes in the secret word, the current blanks, and the player's letter guess. This function creates new blanks by rebuilding the blanks via
    either in the old banks or new letter guess if it appears in the secret word at a given position.'''
    new_blanks = ""
    #We look at each letter of the secret word
    #if a given letter is the same as the letter guess then we update the current index of the word we are looking at
    #else, we do nothing, & go on to look at the next letter
    for index in range(len(secret_word)):
        if(secret_word[index] == letter_guess):
            new_blanks += letter_guess
        else:
            new_blanks
    return new_blanks

def display_game_won_message():
    '''This function takes no inputs and returns no outputs. It simply prints a messasge tot he player indicating they've won'''
    print("Yay, you won! You do not have blood on your hands (not too much at least).")

def display_game_lost_message():
    '''This function takes no inputs and returns no outputs. It simply prints a messasge tot he player indicating they've won'''
    print("You loose. Dang, you really killed him like that, huh?")

def run_game_loop():
    playing = True
    while playing:
        print_welcome_message()
        lives = 5
        random_word = generate_random_word()
        blanks = generate_blanks(random_word)
        display_current_blanks(blanks)
        answer = get_user_answer()
        answer_valid = check_validity(random_word, answer)
    if (answer_valid):
      blanks = update_blanks(random_word, blanks, answer)
    else: 
        lives = lives - 1
        print(f"You have {lives} lives remaining")
    if(lives == 0):
        display_game_lost_message()
        playing = False


#   line 93, in <module>
#     run_game_loop()
#   line 81, in run_game_loop
#     display_current_blanks(blanks)
#   line 54, in display_current_blanks
#     for char in blanks_input:
# TypeError: 'function' object is not iterable



#Zybooks version:
#word = "onomatopoeia"
# num_guesses = 10

# hidden_word = "-" * len(word)

# guess = 1

# while guess <= num_guesses and "-" in hidden_word:
#     print(hidden_word)
#     user_input = input(f"Enter a character (guess #{guess}): ")

#     if len(user_input) == 1:
#         # Count the number of times the character occurs in the word
#         num_occurrences = word.count(user_input)

#         # Replace the appropriate position(s) in hidden_word with the actual character.
#         position = -1
#         for occurrence in range(num_occurrences):
#             position = word.find(user_input, position +
#                                  1)  # Find the position of the next occurrence
#             hidden_word = (hidden_word[:position] + user_input +
#                            hidden_word[position + 1:]
#                            )  # Rebuild the hidden word string

#         guess += 1

# if not "-" in hidden_word:
#     print("Winner!", end=" ")
# else:
#     print("Loser!", end=" ")

# print(f"The word was {word}.")