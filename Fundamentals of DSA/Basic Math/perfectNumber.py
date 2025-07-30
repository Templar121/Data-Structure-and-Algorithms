n = int(input("Please Enter a Number to Check Whether it is Perfect Number or not: "))
div = []
for i in range(1, n):
    if n % i == 0:
        div.append(i)
        
summ = sum(div)

if n == summ: print(f"{n} is a Perfect Number")
else: print(f"{n} is not a Perfect Number")