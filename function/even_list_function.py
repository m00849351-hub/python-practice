def show_even(numbers):
    print("Even numbers are:")
    for num in numbers:
        if num % 2 == 0:
            print(num)

n = int(input("Enter how many numbers: "))
nums = []

for i in range(n):
    nums.append(int(input("Enter number: ")))

show_even(nums)