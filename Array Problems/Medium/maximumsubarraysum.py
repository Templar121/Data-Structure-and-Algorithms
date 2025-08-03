nums = list(map(int, input("Enter the Elements in the Array separated by Spaces: ").split()))
curr_sum = 0
max_sum = float('-inf')
for num in nums:
    curr_sum += num
    max_sum = max(curr_sum, max_sum)
    
print(max_sum)