n = int(input("Enter a Number to Check Plaindrome or not"))

if str(n) == str(n)[::-1]:
    print("Number is Plaindrome")
else:
    print("Number is Not Palindrome")