n = int(input("Enter the value of N to get the factorial: "))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of {n} numbers is {factorial(n)}")
