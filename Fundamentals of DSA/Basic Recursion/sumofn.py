n = int(input("Please Enter the value of N for the range of Sum you want to get: "))

def summ(n):
    def helper(i):
        if i > n:
            return 0
        return i + helper(i + 1)
    return helper(1)

print(f"Sum of {n} numbers is {summ(n)}")