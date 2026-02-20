#Count digit in number

num = int(input("Enter number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Total digit: ", count)