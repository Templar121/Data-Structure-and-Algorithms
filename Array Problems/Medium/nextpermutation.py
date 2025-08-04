nums = list(map(int, input("Please Enter the Elements in the Array seperated by Spaces: ").split()))
a = nums.copy()
n = len(nums)

for i in range(n - 2, -1, -1):
    if nums[i] < nums[i + 1]:
        for j in range(n - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        nums[i + 1:] = reversed(nums[i + 1:])
        break
nums.reverse()
print(f"The Next Permutation for the Array {a} is {nums}")