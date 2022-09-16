#####################
# Python Hangman 
#####################

# Import necessary packages
import random
import time
import os

# read in words_list.txt file
# ensure all lower case
with open('words_list.txt') as file:
    read_file = file.read()
    words_list = list(read_file.lower().split('\n'))
    
# use list to keep ascii hangman art
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

# choose a random word from word list
# could also use random.choice(words_list)
word_index = random.randint(0,len(words_list)-1)
word = words_list[word_index]

# generate blank list of word length
word_length = len(word)
guess_list = ["_"] * word_length

# create a function to check guess and replace blanks
# in guess list with the letter if correct
def check_replace(guess, random_word = word):
    # create variable to keep count of how many times
    # the letter appears in the word
    count = 0
    # use enumerate to keep track of index positions and values
    # if guess is a letter in the word, replace this in the guess list
    for i,v in enumerate(word):
        if user_guess == v:
            guess_list[i] = v
            count +=1
    if count == 0:
        print('\n\nNo luck, try again!')
        return False
    elif count == 1:
        print("\n\nGood guess!")
        return True
    else:
        print(f'\n\nGreat guess, your letter appeared {count} times in the word')
        return True
print('------------------------------------------------')    
print('\n\nWelcome to Hangman\n')
print(f'Your word has {word_length} characters \n\n')
print('------------------------------------------------') 

lives = 6
tries = 0
hangman_index = -1
guesses = []

while True:
    # take in a user guess and append to guesses list
    user_guess = input('Guess a letter:\n').lower()
        
    # check if user has already guessed letter
    if user_guess in guesses:
        # if guessed already print below message and start loop again
        print("You already guessed this letter")
        continue
    else:
        # else check if letter is in word
        guesses.append(user_guess)
        check = check_replace(user_guess)
    # if check returns False
    # guess was not in random word
    # subtract life and print new hangman picture    
    if check == False:
        lives -= 1
        hangman_index -= 1
    # added time to sleep before clearing screen for next round
    time.sleep(1)
    os.system('clear')
    print(f'\n\n{" ".join(guess_list)}')
    tries += 1
    print(f'\nYou have {lives} lives remaining\n')
    print(f'\n\n{stages[hangman_index]}')
     
    # if all "-" have been replaced by letters
    # word is completely guessed and user wins
    # print congrats and in how many attempts they won   
    if "_" not in guess_list:
        print('***********************************************')
        print(f"Congrats you won in {tries} attempts")
        print('***********************************************')
        break
    # if user lives == 0, they lose
    elif lives == 0:
        print('Hang Man!\nBetter luck next time!')
        break
    else:
        # if user has not won or lost, move to next round
        continue
        
    
    



