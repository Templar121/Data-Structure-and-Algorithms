# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input("Please enter the number of Rows"))
for i in range(1, n + 1):
    m = (n + 1) // 2
    if i <= m:
        print("* " * i)
    else:
        stars = (n + 1) - i
        print("* " * stars)
        
# Tracing Table
# --------------
# i   *   
# --------------  * = i
# 1   1          
# 2   2   
# 3   3   
# 4   4   
# 5   5   
# ============== m = (n + 1) // 2
# 6   4          * = (n + 1) - i
# 7   3          
# 8   2   
# 9   1   