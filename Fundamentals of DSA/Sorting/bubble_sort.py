n = list(map(int, input("Please Enter an Array of integers for Sorting using Bubble Sort: ").split()))

def bbsort(n):
    a = len(n)
    flag = True
    while flag:
        flag = False
        for i in range(1, a):
          if n[i - 1] > n[i]:
              flag = True
              n[i - 1], n[i] = n[i], n[i - 1]
        return n
              

print(f"The Array {n} after Bubble Sorting becomes {bbsort(n)}")  