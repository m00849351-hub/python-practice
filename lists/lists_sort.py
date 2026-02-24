nums = []

n = int(input("How many numbers: "))

for i in range(n): 
    nums.append(int(input("Enter number: ")))

nums.sort()

print("Sorted lists: ", nums)