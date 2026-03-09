

#Squares of a Sorted Array#

def squareSortedArray(nums):
    left = 0
    right = len(nums)-1
    res = [0] * len(nums)
    pos = len(nums)-1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] * nums[left]
            left += 1
        else:
            res[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1
    return res

print(squareSortedArray([-4,-1,0,3,10]))