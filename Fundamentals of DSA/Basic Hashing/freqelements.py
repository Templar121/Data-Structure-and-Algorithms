from collections import Counter
nums = list(map(int, input("Please Enter a array of elements separated by spaces: ").split()))

counter = Counter(nums)
print(f" The Frequency list of {nums} is {[[num, cnt] for num, cnt in counter.items()]}")
