#Armstrong number check

num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == temp:
    print("Armstrong number: ")
else:
    print("Not Armstrong")