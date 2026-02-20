students = {}

while True:
    print("\n1. Add student, 2. View all, 3. Average, 4. Exit")
    ch = input("Choose: ")

    if ch == "1":
        name = input("Student name: ")
        marks = int(input("Marks: "))
        students[name] = marks

    elif ch == "2":
        for k, v in students.items():
            print(k, ":", v)

    elif ch == "3":
        total = sum(students.values())
        count = len(students)
        if count > 0:
            print("Average: ", total/count)

    elif ch == "4":
        break