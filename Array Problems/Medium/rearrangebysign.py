nums = list(map(int, input("Please enter the elements in the array separated by spaces: ").split()))
a = nums.copy()
n = len(nums)
# for i in range(1, n):
#     if i == n - 1:
#         break
#     if nums[i] > 0 or nums[i] < 0:
#         if nums[i + 1] > 0 or nums[i + 1] < 0:
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#             i += 1
            
pos = []
neg = []
final = []
for num in nums:
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)
        
for a, b in zip(pos, neg):
    final.append(a)
    final.append(b)
    
if len(pos) > len(neg):
    final.extend(pos[len(neg):])
else:
    final.extend(neg[(len(pos)):])

print(f"After rearranging the Array {nums}, becomes {final}")