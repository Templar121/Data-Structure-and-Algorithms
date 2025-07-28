# *****
# *   *
# *   *
# *   *
# *****

n = int(input("Please Enter the number of Rows"))

for i in range(1, n + 1):
    if i == 1 or i == n:
        stars = 5
        print("*" * stars)
    # elif i % 2 == 0:
    #     space = 5
    #     print(" " * space)
    else:
        space = 3
        print("*" + " " * space + "*")

# Tracing Table
# --------------
# i   *   _
# --------------
# 1   5   0
# 2   0   5
# 3   2   3
# 4   0   5
# 5   2   3
# 6   0   5
# 7   2   3
# 8   0   5
# 9   5   0
