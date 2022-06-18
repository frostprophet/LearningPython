print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

decision1 = input("You follow a path to a dock and can see an island\nin the distance, do you wait for a boat or swim\nto the island? 'stay' or 'swim'\n")

if decision1.lower() == "swim":
  print("You drowned.")
else:
  decision2 = input("You arrive at the island and find a cave.\nStepping in to the cave you can see it forks left and right.\nDo you want to take the left or the right path?\n'Left' or 'Right'\n")
  if decision2.lower() == "left":
    print("You fell in a hole and died.")
  else:
    decision3 = input("You come to a room with three doors,\na red, green and blue door. Which do you open?\n'Red', 'Green' or 'Blue'\n")
    if decision3.lower() == 'red':
      print("You were engulfed in flames and burned to death.")
    elif decision3.lower() == 'green':
      print("You were melted alive by poisonous gas.")
    else:
      print("Congratulations, you found the treasure.")
