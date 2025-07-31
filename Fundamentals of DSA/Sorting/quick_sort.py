nums = list(map(int, input("Enter an Array Elements for the Implementation of Quick Sort: ").split()))
a = nums.copy()

def qsort(nums):
    if len(nums) <= 1:
        return nums
    p = nums[-1]
    l = [x for x in nums[:-1] if x <= p]
    r = [x for x in nums[:-1] if x > p]
    
    L = qsort(l)
    R = qsort(r)
    
    return L + [p] + R

print(f"The Array {a} after Implementing QuickSort Becomes {qsort(nums)}")
