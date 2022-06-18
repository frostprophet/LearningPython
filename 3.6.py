#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#
#Pepperoni on Small: +$2
#Pepperoni on Medium or Large: +$3
#
#Extra cheese: $1

size = input("What size pizza do you want? S, M or L?\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want to add extra cheese? Y or N\n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Not a valid size.")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill comes to ${bill}.")
    
