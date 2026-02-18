#Function to add
def add(a, b):
    return a + b

#Function to subtract
def subtract(a, b):
    return a - b

#Function to multipliply
def multiply(a, b):
    return a * b

#Function to divide
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

#Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1.Add, 2.Subtract, 3.Multiply, 4.Divide")
choice = input("Choose operation: ")

if choice == "1":
    print("Result=", add(num1, num2))
elif choice == "2":
    print("Result=", subtract(num1, num2))
elif choice == "3":
    print("Result=", multiply(num1, num2))
elif choice == "4":
    print("Result=", divide(num1, num2))
else:
    print("Invaild choice")
