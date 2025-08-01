nums = list(map(int, input("Please Enter the elements in the Array Sperated by Space: ").split()))
n = len(nums)

if not nums:
    print(0)
else:
    i = 0
    for j in range(1, n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            
print(f"Number of Unique elements in the array {nums} is {i + 1}")
print(f"Modified Array with unique elements is {nums[:i + 1]}")