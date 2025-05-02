def largestPerimeter(nums):
    nums.sort(reverse=True)  # Descending sort
    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:  # triangle possible
            return nums[i] + nums[i+1] + nums[i+2]
    return 0
print(largestPerimeter([2,1,2]))
print(largestPerimeter([1,2,1,10]))