nums = list(map(int, input("Please enter the Elements in the Array Sparated by Spaces: ").split()))
count = 0
n = len(nums)

for i in range(n):
    if nums[i] > nums[(i + 1) % n]:
        count += 1
if count > 1:
    print(f"The Array {nums} is Not Sorted")
else:
    print(f"The Array {nums} is Sorted")