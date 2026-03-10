


#Longest Mountain in Array#

def longestMountain(arr):
    n = len(arr)
    longest = 0
    i = 1
    while i < n-1:
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            left = i
            right = i
            while left > 0 and arr[left]>arr[left -1]:
                left -= 1
            while right <n-1 and arr[right]>arr[right + 1]:
                right += 1

            longest = max(longest,right -left + 1)
            i = right
        else:
            i += 1
    return longest

print(longestMountain([2,1,4,7,3,2,5]))