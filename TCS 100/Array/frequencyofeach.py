from  collections import Counter

nums = list(map(int, input("Please Enter the lements in the Array Separated by Spaces: ").split()))
freq = Counter(nums)

print(f"The Frequency of Each Element in the Array {nums} is {freq}")