age = int(input("What's your age? "))
height = int(input("What's your height (cm)? "))
bill = 0

if height >= 120:
    if age >= 18:
        bill = 12
        print("Youth tickets cost $12.")
    elif age < 12:
        bill = 5
        print("Kids tickets cost $5.")
    else:
        bill = 7
        print("Adult tickets cost $7.")
    
    photo_req = input("Do you want to purchase a photo? Y or N. ")

    if photo_req == "Y":
        bill += 3

    print(f"Your bill is ${bill}")

else:
    print("You are not tall enough for the ride.")