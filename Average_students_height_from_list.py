

# Input should be space-separated numbers (e.g., "156 160 170")
student_heights = input("Input a list of student heights (space-separated): ").split()

# Convert each input to an integer
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)


total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

student_number = 0
for student_num in student_heights:
    student_number += 1
print(student_number)


Average_height = round(total_heights / student_number)
print(Average_height)