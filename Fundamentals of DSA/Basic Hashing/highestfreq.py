from collections import Counter
n = list(map(int, input("Please Enter an array of Integers: ").split()))

freq = Counter(n)
maxx = 0
max_key = None
for key, val in freq.items():
    if val > maxx:
        maxx = val
        max_key = key
    elif val == maxx:
        if max_key is None or key < max_key:
            max_key = key
    
    
print(f" The Element with maximum frequency in the Array {n} is {max_key}")
