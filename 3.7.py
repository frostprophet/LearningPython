age = int(input("What's your age? "))
height = int(input("What's your height (cm)? "))
bill = 0

if height >= 120:
    if age >= 45 and age <= 55:
        print("Mid-life crisis special, zero cost!")
    elif age < 12:
        bill = 5
        print("Kids tickets cost $5.")
    elif age >= 18:
        bill = 12
        print("Youth tickets cost $12.")
    else:
        bill = 7
        print("Adult tickets cost $7.")
    
    photo_req = input("Do you want to purchase a photo? Y or N. ")

    if photo_req == "Y" or photo_req == "y":
        bill += 3
    elif photo_req == "N" or photo_req == "n":
        bill += 0
    else:
        print("Invalid input, no photo default.")

    print(f"Your bill is ${bill}")

else:
    print("You are not tall enough for the ride.")