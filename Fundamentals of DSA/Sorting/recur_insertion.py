nums = list(map(int, input("Enter the Array Elements for Recursive Insertion Sort Implementation: ").split()))
a = nums.copy()

def insesort(nums, start = 0):
    n = len(nums)
    if start >= n - 1:
        return
    insert(nums, start)
    insesort(nums, start + 1)
    return

def insert(nums, start):
    pos = start
    while pos > 0 and (nums[pos] < nums[pos - 1]):
        nums[pos], nums[pos - 1] = nums[pos - 1], nums[pos]
        pos = pos - 1
        
        
insesort(nums)

print(f"The Array {a} after the Impementation of Recusive Insertion Sort becomes {nums}")