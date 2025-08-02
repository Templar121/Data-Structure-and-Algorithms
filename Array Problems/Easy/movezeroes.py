nums = list(map(int, input("Please Enter the Elements in ths Array seprated by Spaces: ").split()))
a = nums.copy()
n = len(nums)
insert_pos = 0
for i in range(n):
    if nums[i] != 0:
        nums[insert_pos] = nums[i]
        insert_pos += 1
for i in range(insert_pos, n):
    nums[i] = 0
    
print(f"The Array {a} after Moving all Zeroes to the end becomes {nums}")
        