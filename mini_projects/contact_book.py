def  save_contact(name, phone):
    file = open("Contacts.txt", "a")
    file.write(name + ":" + phone + "\n")
    file.close()

def view_contact():
    file = open("Contacts.txt", "r")
    data = file.read()
    print(data)
    file.close()

while True:
    print("\n1.Save contact")
    print("2.View contact")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        save_contact(name, phone)

    elif choice == "2":
        view_contact()

    elif choice == "3":
        break
