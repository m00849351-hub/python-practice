#Take student data
name = input("Enter name: ")
marks = input("Enter marks: ")

#Save to file
file = open("Student.text", "a")
file.write(name + " - " + marks + "\n")
file.close()

print("Data saved.")