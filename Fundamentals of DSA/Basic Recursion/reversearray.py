arr = list(map(int, input("Enter the elements in the array sperated by spaces").split()))
n = len(arr)
print(arr, n)

def reverse(arr):
    n = len(arr)
    def helper(left, right):
        if left >= right:
            return
        arr[left], arr[right] = arr[right], arr[left]
        helper(left + 1, right - 1)
        
    helper(0, n - 1)
    return arr

print(f"The reversed array is {reverse(arr)}")