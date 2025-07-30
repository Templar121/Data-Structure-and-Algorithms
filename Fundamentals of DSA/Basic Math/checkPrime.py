n = int(input("Please Enter a Number to Check whether it is Prime or not: "))

if n == 1: print(f"{n} is Neither Prime nor Composite")
elif n == 2: print(f"{n} is Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is Composite")
            break
        else:
            print(f"{n} is Prime") 
            break