n = int(input("Enter a number to Reverse"))

if n < 0:
    print("-" + str(abs(n))[::-1])
else:
    print(str(n)[::-1])