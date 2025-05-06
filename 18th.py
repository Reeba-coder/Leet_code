def merge(nums1, m, nums2, n):
    # Pointing to the end of actual elements
    i = m - 1
    j = n - 1
    # Pointing to the end of the merged array
    k = m + n - 1

    # Traverse from the end and place the largest value at the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If elements are left in nums2 (nums1 ke to already sahi jagah par hain)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3,5,6]