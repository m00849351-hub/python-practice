while True:
    print("\n1.Add record 2.View record 3.Exit")
    ch = input("Choose: ")

    if ch == "1":
        name = input("Name: ")
        marks = input("Marks: ")

        f = open("students.txt", "a")
        f.write(name + " " + marks + "\n")
        f.close()

    elif ch == "2":
        f = open("students.txt", "r")
        data = f.read()
        print("\nRecords:\n", data)
        f.close()

    elif ch == "3":
        break