#     *
#    **
#   ****
#  ******
# ********

n = int(input("Please enter the number of rows"))

for i in range(1, n + 1):
    if i == 1:
        stars = 1
    else:
        stars = 2 * i - 2
    spaces = n - i
    print(" " * spaces + "*" * stars)