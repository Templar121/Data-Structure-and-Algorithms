nums = list(map(int, input("Please Enter an Array for the impementation of Merge Sort: ").split()))

def mergesort(nums):
    n = len(nums)
    if n <= 1 :
        return nums
    m = n // 2
    left = mergesort(nums[:m])
    right = mergesort(nums[m:])
    
    sorted_array = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

print(f"The Array {nums} after Implementing Merge Sort Becomes {mergesort(nums)}")