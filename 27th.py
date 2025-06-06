def isMonotonic(nums):
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing
print(isMonotonic([1,2,2,3]))