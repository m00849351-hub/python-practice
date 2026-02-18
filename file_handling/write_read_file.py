#write data into file
file = open("data.text", "w")
file.write("Hello, this is my first file.\n")
file.write("Python file handling practice.")
file.close()

#read data from file
file = open("data.text", "r")
content = file.read()
print(content)
file.close()
