nums = list(map(int, input("Enter an Array Elements for Recursive Bubble Sort Implementation: ").split()))
a = nums.copy()

def recurb(nums, n=None):
    if n is None:
        n = len(nums)
    if n == 1:
        return

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    recurb(nums, n - 1)


recurb(nums)


print(f"The Array {a} after Implementing Recursive Bubble Sort becomes {nums}")
