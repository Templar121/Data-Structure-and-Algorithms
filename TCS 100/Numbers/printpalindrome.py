n = int(input("Please Enter the Range between where we need to print palindrome Number: "))
palin = []

for i in range(1, n + 1):
    if str(i) == str(i)[::-1]:
        palin.append(i)

print(f"The palindrome Numbers Between {1} to {n} are {palin}")