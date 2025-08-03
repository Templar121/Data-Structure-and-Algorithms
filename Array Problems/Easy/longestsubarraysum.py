nums = list(map(int, input("Please Enter the  elements in the array separated by Spaces: ").split()))
a = nums.copy()
n = len(nums)
k = int(input("Please Enter the Target Sum Required: "))
prefix_sum = 0
max_len = 0
prefix_map = {}

for i in range(n):
    prefix_sum += nums[i]
    
    if prefix_sum == k:
        max_len = i + 1
        
    if prefix_sum - k in prefix_map:
        length = i - prefix_map[prefix_sum - k]
        max_len = max(max_len, length)
        
    if prefix_sum not in prefix_map:
        prefix_map[prefix_sum] = i
        
print(f"The Length of the Longest Subarray with K = {k} in the Array {a} is {max_len}")
        
    
