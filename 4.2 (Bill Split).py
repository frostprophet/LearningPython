# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

paying_index = random.randint(0,len(names)-1)

paying_name = names[paying_index]

print(f"{paying_name} is paying for the bill.")