
#def prime_checker(number):
#    if number % 2 == 0 or (number % 3 == 0 and number != 3) or (number % 5 == 0 and number != 5) or (number % 7 == 0 and number != 7):
#        print("The number is not prime.")
#    else:
#        print("The number is prime.")
#
#
#n = int(input("Check this number: "))
#
#prime_checker(number=n)


def prime_checker2(number):
    check = 0
    for a in range(2,9):
        if number % a == 0 and number != a:
            check += 1
    if check >= 1:
        print("This number is not prime.")
    else:
        print("This number is prime.")


n = int(input("Check this number: "))

prime_checker2(number=n)
