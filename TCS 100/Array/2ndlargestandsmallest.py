nums = list(map(int, input("Please Enter the Elements in the Array Separted by Spaces: ").split()))
nums.sort()

print(f"The 2nd Largest and 2nd Smallest Element Present in the array is {nums[-2]} and {nums[1]} respectively")