nums = list(map(int, input("Please Enter the elements in the Array: ").split()))

min_profit = float('+inf')
max_profit = 0
for num in nums:
    min_profit = min(min_profit, num)
    max_profit = max(max_profit, num - min_profit)
print(f"The Maximum Porfit gained from Buying and Selling Stocks from the Array {nums}, is {max_profit}")
        
