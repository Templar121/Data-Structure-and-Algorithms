nums = list(map(int, input("Please Enter an Array to Implement Selection Sort: ").split()))

def selecsort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
        
print(f"The Array {nums} after Implementing Selection Sort is {selecsort(nums)}")
                 