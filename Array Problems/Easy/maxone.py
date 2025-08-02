nums = list(map(int, input("Please Enter the Elements in the Array separated by Spaces: ").split()))
a = nums.copy()
max_one = 0
curr_one = 0
for num in nums:
    if num == 1:
        curr_one += 1
        max_one = max(curr_one, max_one)
    else:
        curr_one = 0
        
print(f"The Maximum number of Ones in the Array {a} is {max_one}")