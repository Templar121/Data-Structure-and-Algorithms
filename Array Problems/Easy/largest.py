nums =list(map(int, input("Enter the Elements in the Array Separated by a Space: ").split()))

largest = float("-inf")

for num in nums:
    if num > largest:
        largest = num

print(f"The Largest Element in the Array {nums} is {largest}")