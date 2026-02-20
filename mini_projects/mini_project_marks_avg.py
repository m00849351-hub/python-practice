def average(marks):
    total = sum(marks)
    avg = total/len(marks)
    print("Average = ", avg)

n = int(input("enter number of subjects: "))
marks = []

for i in range(n):
    marks.append(int(input("Enter marks: ")))

average(marks)