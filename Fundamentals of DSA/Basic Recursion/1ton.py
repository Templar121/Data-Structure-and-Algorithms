n = int(input("Please Enter the value of N: "))

def recursion(i, n):
    if i > n:
        return
    print(i)
    recursion(i + 1, n)
    
recursion(1, n)    

def recursion2(n):
    def helper(i):
        if i > n:
            return
        print(i)
        helper(i + 1)
    helper(1)
    
recursion2(n)