def count_nums(numbers):
    pos = 0
    neg = 0
    zero = 0

    for num in numbers:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else: 
            zero += 1

    print("Positive: ", pos)
    print("Negative: ", neg)
    print("Zero: ", zero)

n = int(input("Enter count: "))
nums = []

for i in range(n):
    nums.append(int(input("Enter number: ")))

count_nums(nums)
