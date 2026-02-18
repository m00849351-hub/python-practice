numbers = []

for i in range(4):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Even numbers are: ")

for n in numbers:
    if n % 2 == 0:
        print(n)
