"""
6. Rotate an Array by One Position
Write a function that rotates an array to the right by one position (i.e., the last element moves to the first position).
nums = [1,2,3,4,5]
output = [5,1,2,3,4]
"""
# try and switch the first element and last element
#The rotate everything else 
def rotateArray(nums):

    for i in range(len(nums)):
            nums[i] = nums[i + 1]
        
    print('nums', nums)
    

#Manual testcases

result = rotateArray([[1,2,3,4,5]])
assert result == [5,1,2,3,4], f'Expected [5,1,2,3,4] but got {result}'