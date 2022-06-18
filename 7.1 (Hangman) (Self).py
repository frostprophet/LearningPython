import random

word_list = ["aardvark", "baboon", "camel", "apple", "caramel", "baobei"]

chosen_word = random.choice(word_list)

life_count = 6

win_count = 0
underscore_word = []
underscore_word_string = ""

# change chosen word in to a list of all underscores to print
for letter in chosen_word:
    underscore_word.append(" _ ")
# change underscore list in to string with the same number of underscores
for score in underscore_word:
    underscore_word_string += score

print(underscore_word_string)

while life_count > 0 and win_count == 0:
    user_guess = input("\nWhat letter would you like to guess?\n\n").lower()
    correct_count = 0
    replace_letter_count = 0
    for i in chosen_word:
        if i == user_guess:
            underscore_word[replace_letter_count] = " "+i+" "
            replace_letter_count += 1
            correct_count += 1
        else:
            replace_letter_count += 1
    if correct_count == 0:
        life_count -= 1

    print(f"\n{life_count} lives remaining.\n")

    updated_word_string = ""
    updated_word = underscore_word
    for letter in updated_word:
        updated_word_string += letter

    print(updated_word_string)

    if updated_word_string.count(" _ ") == 0:
        win_count += 1
        print("\nCongratulations, you win!\n")

if life_count == 0:
    print("\nOut of lives, you lose.")
