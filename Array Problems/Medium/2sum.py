nums = list(map(int, input("Please Enter the elements in the Array Separated by Spaces: ").split()))
a = nums.copy()
target = int(input("Please Enter the Target Sum: "))

h = {}
for i in range(len(nums)):
    y = target - nums[i]
    if y in h:
        idx = [h[y], i]
    h[nums[i]] = i

print(f"The Indices of the Two numbers that add up to the target {target} in the Array {a} is {idx}")