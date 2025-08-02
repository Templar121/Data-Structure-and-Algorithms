nums = list(map(int, input("Please enter the Elements in the Array sperated by Spaces: ").split()))
a = nums.copy()

n = len(nums)
temp = nums[0]

for i in range(0, n - 1):
    nums[i] = nums[i + 1]
    
    
nums[-1] = temp

print(f"The Array {a} when Rotated by 1 Steps to the Left or Right becomes {nums}")