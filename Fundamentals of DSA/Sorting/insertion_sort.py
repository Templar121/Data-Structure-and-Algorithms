nums = list(map(int, input("Please Enter an Array for the Implementation of Insertion Sort: ").split()))

def insersort(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:
                break
    return nums

print(f"The Array {nums} after Implementing Insertion Sort is {insersort(nums)}")
   