nums = list(map(int, input("Please Enter the elements in the Array separated by Spaces: ").split()))
n = len(nums)

leaders = []
max_from_right = float('-inf')

for i in range(n - 1, -1, -1):
    if nums[i] >= max_from_right:
        leaders.append(nums[i])
        max_from_right = nums[i]

leaders.reverse()
print("Leader elements:", leaders)
