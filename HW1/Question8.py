"""
8. Left Rotation by K Positions
Write a function to rotate an array to the left by k positions. Use modular arithmetic to handle the array indexing.
"""
def rotatebyK(nums, k): 
    for i in range(len(nums)- 1):
        while i < len(nums):        #Trying to handle out of bound error
            nums[i] = nums[i -k]
        
    print('nums', nums)

    # pass


#Manual testing:
result = rotatebyK([1,3,5,7,11], 2)
assert result == [1,3,5,7,11], f'Expected [1,3,5,7,11]. but got {result}'
