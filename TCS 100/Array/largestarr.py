nums = list(map(int, input("Please ENter the elements in the Array Separated by Spaces: ").split()))
largest = float('-inf')
for num in nums:
    if num > largest:
        largest = num
    
print(f"The Largest Element Present in the Array {nums} is {largest}")