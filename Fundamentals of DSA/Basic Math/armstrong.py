n = int(input("Enter a number to check whether it is Armstrong Number or Not: "))

digits = str(n)
power = len(digits)

total = sum(int(d) ** power for d in digits)
if total == n:
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")