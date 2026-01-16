import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = poss_values[len(poss_values) // 2]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if current_val > next_val:
        temp = 'l'
    else:
        temp = 'h'

    if temp == user_input:
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    temp = None
    for i in range(len(word)):
        if letter == word[i]:
            print("Well done! '",letter, "' is in the word")
            board[i] = letter
            temp = 1
        
    print("Sorry,'", letter, "'is not in the word")
    if temp == 1:
        return True
    else:
        return False



