n = int(input("Please Enter a number to print all its divisors: "))
divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        
print(divisors)