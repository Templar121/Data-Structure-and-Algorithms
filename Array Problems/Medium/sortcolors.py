nums = list(map(int, input("Please Enter the Values in the Array Separated by Spaces: ").split()))
a = nums.copy()

low = mid = 0
high = len(nums) - 1

while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
        
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

print(f"The Array {a} adter Sorting becomes {nums}")