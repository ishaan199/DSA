

#Shortest Unsorted Continuous Subarray#

def shortestUnsortedSubarray(nums):
    sorted_nums = sorted(nums)
    left = 0
    right = len(nums)-1
    while left < len(nums) and nums[left] == sorted_nums[left]:
        left += 1
    while right > left and nums[right] == sorted_nums[right]:
        right -= 1

    return 0 if left == len(nums) else right - left + 1

print(shortestUnsortedSubarray([2,6,4,8,10,9,15]))