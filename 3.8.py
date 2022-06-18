print("Wlecome to the love calculator.")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

names_combined = str(name1)+str(name2)

true_string = ["t","r","u","e"]
true_count = 0
love_string = ["l","o","v","e"]
love_count = 0

for t in names_combined.lower():
    if t in true_string:
        true_count += 1

for l in names_combined.lower():
    if l in love_string:
        love_count += 1

combined_score = int(str(true_count) + str(love_count))

if combined_score < 10 or combined_score > 90:
    message = ", you go together like coke and mentos."
elif combined_score > 40 and combined_score < 50:
    message = ", you are alright together."
else:
    message = "."

print(f"Your score is {combined_score}%{message}")