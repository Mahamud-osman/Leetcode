""""
11. Find the Index of a Target Element
Write a function that searches for a specific element in an array and returns its index. If the element is not found, return -1.
"""

def findTarget(nums, target):

    for i in range(len(nums)):
        if nums[i] == target:
            print(target)
            return target
    
    print(-1)
    return -1






#Manual Testing 

result = findTarget([3,4,5,6,2], 2)
assert result == 2, f'Expected 2 but got {result}'

result = findTarget([3,4,5,6,8], 2)
assert result == -1, f'Expected -1 but got {result}'


result = findTarget([14,76,33,-1,99,15], 99)
assert result == 99, f'Expected 99 but got {result}'
