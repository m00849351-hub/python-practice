f = open("data.txt", "a")
f.write("Hello\n")
f.close()

f = open("data.txt", "r")
print(f.read())
f.close()
