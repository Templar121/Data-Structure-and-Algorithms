num = int(input("Please Enter a Number to Check Whether it is prime or Not: "))

if num == 1: print(f"{num} is Neither prime nor Composite")
if num == 2: print(f"{num} is Prime Number")
for i in range(3, int(num ** 0.5)):
    if num % i ==0:
        print(f"{num} is Composite Number")
        break
    else:
        print(f"{num} is Prime Number")
        break