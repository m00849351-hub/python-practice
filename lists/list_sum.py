# Take 5 numbers from user and store in list
numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

# calculate sum
total = sum(numbers)

print("Sum of list =", total)
