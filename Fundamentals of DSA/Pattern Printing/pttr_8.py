# *       *
# **     **
# ***   ***
# **** ****
# *********
# **** ****
# ***   ***
# **     **
# *       *

n = int(input("Enter the number of Rows"))

rows = 2 * n - 1

for i in range(1, rows + 1):
    stars = i if i <= n else 2 * n - i
    spaces = 2 * (n - stars)
    left = "*" * stars
    middle = " " * spaces
    right = "*" * stars
    print(left + middle + right)
        

# Tracing Table
# -------------- n = 9
# i   *   _
# -------------- * = 2 * i
# 1   2   8      _ = 2 * m - *
# 2   4   6
# 3   6   4
# 4   8   2
# 5   10  0
# --------------  m = (n + 1) // 2
# 6   8   2       _ = 2 * i - (n + 1) 
# 7   6   4       * = (n + 1) - *
# 8   4   6
# 9   2   8