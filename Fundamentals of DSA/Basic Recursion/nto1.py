n = int(input("Please Enter the value of N"))

def recursion(n):
    def helper(i):
        if i == 0:
            return
        print(i)
        helper(i - 1)
    helper(n)
    
recursion(n)