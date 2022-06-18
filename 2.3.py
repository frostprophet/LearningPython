age = int(input("What is your current age? > "))

time_years = 90 - age
time_months1 = round(time_years*12,2)
time_weeks1 = round(time_months1*4,2)
time_days1 = round(time_weeks1*7,2)

time_days2 = round(time_years*365,2)
time_weeks2 = round(time_years*52,2)
time_months2 = round(time_years*12,2)

print(f"If you live until 90 years old you have {time_days1} days, {time_weeks1} weeks or {time_months1} months left.")
print(f"If you live until 90 years old you have {time_days2} days, {time_weeks2} weeks or {time_months2} months left.")