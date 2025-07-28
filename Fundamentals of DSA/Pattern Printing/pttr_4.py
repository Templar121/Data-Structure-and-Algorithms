#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Please Enter the number of rows"))

for i in range(1, n + 1):
    m = (n + 1) // 2
    if i <= m:
        stars = 2 * i - 1
        spaces = m - i
        print(" " * spaces + "*" * stars)
    else:
        stars = 2 * ((n + 1) - i) - 1
        spaces = i - m
        print(" " * spaces + "*" * stars)
        
# Tracing Table
# --------------
# i   *   __
# --------------  * = 2 * i - 1
# 1   1   4       _ = m - i
# 2   3   3
# 3   5   2
# 4   7   1
# 5   9   0
# ============== m = (n + 1) // 2
# 6   7   1      * = 2 * ((n + 1) - i) - 1
# 7   5   2      _ = i - m
# 8   3   3
# 9   1   4