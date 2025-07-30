s = str(input("Enter a String to check whther it is palindrome or Not: "))

def recursive(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return recursive(s[1: -1])

if recursive(s): print(f"{s} is a Palindromic String")
else: print(f"{s} is not a Palindromic String")