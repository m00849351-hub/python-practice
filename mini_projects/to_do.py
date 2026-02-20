tasks = []

while True:
    print("\n1. Add Task, 2. View, 3. Save, 4. Exit")
    ch = input("Choose task: ")

    if ch == "1":
        t = input("Enter task: ")
        tasks.append(t)

    elif ch == "2":
        for i in tasks:
            print("-", i)

    elif ch == "3":
        f = open("tasks.txt", "w")
        for i in tasks:
            f.write(i + "\n")
            f.close()
            print("Saved to file")

    elif ch == "4":
        break
