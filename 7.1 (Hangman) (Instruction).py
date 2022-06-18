import random
import HangmanStages
import hangmanwords
import os


def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


word_list = hangmanwords.word_list

chosen_word = random.choice(word_list)

life_count = 6

win_count = 0
display = []
display_string = ""
word_length = len(chosen_word)
guessed_letters = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

# change chosen word in to a list of all underscores to print
for letter in chosen_word:
    display.append(" _ ")
# change underscore list in to string with the same number of underscores
for score in display:
    display_string += score

print(HangmanStages.logo)
print(display_string)

while life_count > 0 and win_count == 0:
    user_guess = input("\nWhat letter would you like to guess?\n\n").lower()
    clearconsole()
    if user_guess in guessed_letters:
        print("\nYou have already guessed this letter.")
    elif user_guess not in letters:
        print("\nPlease enter a valid input.")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == user_guess:
                display[position] = " " + letter + " "
        if user_guess not in chosen_word:
            life_count -= 1
#            print(f"\n{user_guess} is not in the word.")
        guessed_letters += user_guess

    print(f"\n{life_count} lives remaining.\n")

    updated_word_string = ""
    updated_word = display
    for letter in updated_word:
        updated_word_string += letter

    print(updated_word_string)
    print(HangmanStages.stages[life_count])

    if updated_word_string.count(" _ ") == 0:
        win_count += 1
        print("\nCongratulations, you win!\n")

if life_count == 0:
    print(f"\nOut of lives, you lose. The word was {chosen_word}.")

# 214564 - Sasha CA number
