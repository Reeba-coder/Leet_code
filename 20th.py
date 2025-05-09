def removeDuplication(nums):
    k=1
    for i in range(1, len(nums)):
        if nums[i]!=nums[k-1]:
            nums[k]=nums[i]
            k+=1
    return k
nums=[1,1,2]
k=removeDuplication(nums)
print("k=", k)
print("nums", nums[:k] )