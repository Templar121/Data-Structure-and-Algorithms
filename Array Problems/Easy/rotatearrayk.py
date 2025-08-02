nums = list(map(int, input("Enter the Elements in the Array separted by Spaces: ").split()))
a = nums.copy()
k = int(input("Enter the Value of K which will decide the number of Rotations: "))
n = len(nums)
k = k % n

nums[:] = nums[-k:] + nums[:-k]

print(f"The Array {a} when Rotated by {k} times becomes {nums}")