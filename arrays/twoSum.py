

#TwoSum-2#

def twoSum(nums,target):
    left = 0
    right = len(nums)-1
    while left < right:
        total = nums[left] + nums[right]
        if total < target:
            left += 1
        elif total > target:
            right-=1
        else:
            return [left+1, right+1]

print(twoSum([2,3,4],6))