nums = list(map(int, input("Please Enter the Elements in the Array Seperated by Spaces: ").split()))
curr_sum = 0
max_sum = float('-inf')
start = end = s = 0
for i in range(len(nums)):
    curr_sum += nums[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
        start = s
        end = i
    if curr_sum < 0:
        curr_sum = 0
        s = i + 1
    
print(max_sum, start, end)