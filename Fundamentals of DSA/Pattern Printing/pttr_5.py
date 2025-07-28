#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

n = int(input("Enter the number of Rows"))

for i in range(1, n + 1):
    num = i
    spaces = n - i
    print(" " * spaces + (str(i) + " ") * i)