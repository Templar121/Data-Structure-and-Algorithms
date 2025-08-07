num = str(input("Please Enter a Number to Check Whether it is palindrome or not: "))

if num == num[::-1]: print(f"{num} is a Palindrome Number") 
else: print(f"{num} is not a Palindrome Number")