"""
8. Left Rotation by K Positions
Write a function to rotate an array to the left (-1) by k positions. Use modular arithmetic to handle the array indexing.
nums = [1,3,5,7,11]
output = [5,7,11,1,3]
"""
def rotatebyK(nums, k): 
    #Keep track of current value:
        
        last_value = nums[-1 - k]       #Not sure how to handle for this
    
        for i in range(len(nums)):
            current_index = nums[i]       #Stash our current value
            nums[i] = last_value    #Make our last value = current val 
            last_value = current_index
        
        print(nums)

#Manual testing:
result = rotatebyK([1,3,5,7,11], 2)
assert result ==[5,7,11,1,3], f'Expected [5, 7, 11, 1, 3]. but got {result}'
