nums1 = list(map(int, input("Please Enter the Elements of the First Array separated by Spaces ").split()))
nums2 = list(map(int, input("Please Enter the Elements of the Second Array separated by Spaces ").split()))

nums1 = set(nums1)
nums2 = set(nums2)

print(f"The Union of the Two Arrays is {nums1.union(nums2)}")