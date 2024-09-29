"""
5. Double Each Element in an Array
Write a function that modifies an array in-place to double the value of each element.
nums = [2,3,4,5]
nums = [4,6,8,10]
"""
# How to appraoch problem, in place means not create another array
# Loop thorugh every element, and multiply it by 2

def doubleElement(nums):
    
    # I'm not sure why this doesnt work
    # for n in nums:
    #     n = n * 2
    # print('nums:', nums)
    # return nums
    #Handle edge case
    if len(nums) == 0:
        return - 1

    
    for i in range(len(nums)):
        nums[i] = nums[i] * 2
    
    print('nums', nums)
    return nums
        

#Manual testing:
result = doubleElement([2,3,4,5])
assert result == [4,6,8,10], f'expected [4,6,8,10], but got {result}'

result = doubleElement([1,2,10,20])
assert result == [2,4,20,40], f'expected [4,6,8,10], but got {result}'
