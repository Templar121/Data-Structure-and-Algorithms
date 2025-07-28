# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Please Enter the no. of Rows"))

for i in range(1, n + 1):
    spaces = i - 1
    stars = (11 - 2 * i)
    print(" " * spaces + "*" * stars)
    