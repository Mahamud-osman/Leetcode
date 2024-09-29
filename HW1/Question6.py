"""
6. Rotate an Array by One Position
Write a function that rotates an array to the right by one position (i.e., the last element moves to the first position).
nums = [1,2,3,4,5]
output = [5,1,2,3,4]
"""

# This was my inital thoughr process:
# try and switch the first element and last element
#The rotate everything else 

# def rotateArray(nums):

#     for i in range(len(nums)):
#             nums[i] = nums[i + 1]
        
#     print('nums', nums)
    
 # Search online on how to handle out of range error and saw this    
 # https://stackoverflow.com/questions/73505064/right-rotate-the-array-by-one-index
 # Start from the end of the array, have last element = nums[0]
 # start iterating from end of the array, shift index one position 
def rotateArray(nums):
    
    # last_index = len(nums) - 1
    # last_index = nums[0]    
    # This how I solve it, shift the index by one but not sure how to solve for out of bound error
    
    for i in range(len(nums)- 1, -1, -1):   #Traverese an array backwards
        # while i < len(nums):        #Trying to handle out of bound error
            nums[i] = nums[i + 1]
        
    print('nums', nums)

    # pass

#Manual testcases

result = rotateArray([1,2,3,4,5])
assert result == [5,1,2,3,4], f'Expected [5,1,2,3,4] but got {result}'