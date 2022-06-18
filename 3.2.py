age = int(input("What's your age? "))
height = int(input("What's your height (cm)? "))

#if height >= 120:
#    if age >= 18:
#        print("Ticket will cost $12.")
#    else:
#        print("Ticket will cost $7.")
#else:
#    print("You are not tall enough for the ride.")

if height >= 120:
    if age >= 18:
        print("Ticket will cost $12.")
    elif age < 12:
        print("Ticket will cost $5.")
    else:
        print("Ticket will cost $7.")
else:
    print("You are not tall enough for the ride.")