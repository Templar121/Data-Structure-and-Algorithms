nums = list(map(int, input("Please Enter the Elemenst in the array separted by Spaces: ").split()))
nums.sort()
result = []
i= 0
j = len(nums) - 1

while i <= j:
    if i == j:
        result.append(nums[i])
    else:
        result.append(nums[i])
        result.append(nums[j])
    i += 1
    j -= 1 
    
print(f"The Rearranged array {nums} becomes {result}")