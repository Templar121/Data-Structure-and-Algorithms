nums = list(map(int, input("Please Enter the Array Elements Separated by Spaces: ").split()))

largest = float("-inf")
sceond_largest = float("-inf")

for num in nums:
    if num > largest:
        sceond_largest = largest
        largest = num
    elif num < largest and num > sceond_largest:
        sceond_largest = num
        
if sceond_largest == float("-inf"):
    print(f"There is No Sceond Largest Element in the array{nums}")
else:
    print(f"The Sceond Largest Element in the Array {nums} is {sceond_largest}")
    