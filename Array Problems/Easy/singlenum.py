nums = list(map(int, input("Please Enter the Elements in the Array separated by Spaces: ").split()))
a = nums.copy()
ans = 0
for num in nums:
    ans ^= num

print(f"The Element that Appears once in the Array {a} is {ans}")