n = int(input("Please Enter the Range to Check for Prime Numbers: "))
p_nums = []

for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        p_nums.append(i)

print(p_nums)