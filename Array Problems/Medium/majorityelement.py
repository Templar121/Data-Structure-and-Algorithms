from collections import Counter
nums = list(map(int, input("Please Enter the Elements in the Array separated by Array: ").split()))
n = len(nums)
counter = Counter(nums)
for key, val in counter.items():
    if val >= n / 2:
        print(f"the Majority Element for the Array {nums} is {key}")
        break