nums = list(map(int, input("Please Enter the elements in the Array separated by spaces: ").split()))
smallest = float('+inf')

for num in nums:
    if num < smallest:
        smallest = num

print(f"The Smallest Element Present in the Array {nums} is {smallest}")
    