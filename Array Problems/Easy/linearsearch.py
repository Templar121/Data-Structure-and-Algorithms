nums = list(map(int, input("Please Enter the Elements in the Array Separated by Spaces: ").split()))
target = int(input("Please Enter the Element to be Searched: "))

flag = False
idx = None
for i in range(len(nums)):
    if nums[i] == target:
        flag = True
        idx = i
        break
   
        
        
if flag:
    print(f"The Target Element {target} is found in the Array {nums} at Position {idx}")
else:
        print(f"The Target Element {target} is not present in the Array {nums}")