def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
    
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
avg = total / n

grade = calculate_grade(avg)

print("\nStudent: ", name)
print("Total: ", total)
print("Average: ", avg)
print("Grade: ", grade)
