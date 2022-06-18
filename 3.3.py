height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight / height**2,2)

if BMI < 18.5:
    interp = "underweight"
elif BMI < 25:
    interp = "normal weight"
elif BMI < 30:
    interp = "overweight"
elif BMI < 35:
    interp = "obese"
else:
    interp = "clinically obese"

print(f"Your BMI is {BMI} and this is considered {interp}.")