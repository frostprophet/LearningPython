rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

options = [rock,paper,scissors,"Invalid Input."]

user_choice = int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice not in [0,1,2]:
    user_choice = 3

user_end = options[user_choice]

comp_number = random.randint(0,2)

comp_choice = options[comp_number]

print(f"You chose:\n{user_end}")

print("\n******************************************\n")

print(f"Computer chose:\n{comp_choice}")

win_status = 0

if user_end == rock and comp_choice == scissors:
    win_status = 2
elif user_end == scissors and comp_choice == paper:
    win_status = 2
elif user_end == paper and comp_choice == rock:
    win_status = 2
elif user_end == comp_choice:
    win_status = 1

if win_status == 2:
    print("You win!")
elif win_status == 1:
    print("It's a draw.")
else:
    print("You loose.")

