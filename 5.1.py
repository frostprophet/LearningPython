# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#if len(student_heights) == 0:
#    print("No values entered")
#else:
#    average_height = round(sum(student_heights)/len(student_heights))
#    print(f"The average student height is {average_height}cm.")


total_heights = 0
student_count = 0

for height in student_heights:
    total_heights += height
    student_count += 1

if student_count == 0:
    print("No data entered.")
else:
    average_height = round(total_heights/student_count)
    print(f"The average student height is {average_height}cm.")