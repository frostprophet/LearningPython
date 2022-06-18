print("Welcome to the tip calculator.")

bill_total = float(input("What was the total of the bill?\n"))

num_people = int(input("How many people are splitting the bill?\n"))

tip_percent = int(input("What percentage tip would you like you leave? 10, 15 or 20\n"))

payment = "{:.2f}".format(round((bill_total * (1+(tip_percent/100)))/num_people,2))

print(f"If the bill was ${bill_total}, split between {num_people}, with a {tip_percent}% tip.\nEach person should pay ${payment}")