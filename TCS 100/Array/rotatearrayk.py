nums = list(map(int, input("Please Enter the Elements of the Array Separated by Spaces: ").split()))
n = len(nums)
k = int(input("Please Enter the Value of k: "))
k = k % n
nums[:] = nums[-k:] + nums[:-k]
print(nums)