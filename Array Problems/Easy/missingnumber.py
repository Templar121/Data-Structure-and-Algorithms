nums = list(map(int, input("Please Enter the Elements in the Array Separated by Spaces: ").split()))
a = nums.copy()

nums = set(nums)
n = len(nums)

for i in range(n + 1):
    if i not in nums:
        print(f"The Missing Number in the Array {a} is {i}")
        break