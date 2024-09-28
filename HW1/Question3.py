""""
3. Find the Minimum and Maximum Index
Write a function that finds the index of the minimum and maximum elements in an array.
nums = [3,1,5,0,8,12]
output = [3,5]
"""

def minAndMax(nums):
    #Handle edge case
    if len(nums) == 0:
        return - 1

    current_max_index = 0
    current_min_index = 0
    
    #Index Comparison
    for i in range(len(nums)):
        if nums[i] > nums[current_max_index]:
            current_max_index = i
    
    #Calculate max
    for i in range(len(nums)):
        if nums[i] < nums[current_min_index]:
            current_min_index = i
            
    print("Output", [current_min_index,current_max_index ])


# Keep tracker of min index, keep tracker of max index

# Manual tesing:
result = minAndMax([3,1,5,0,8,12])
result == [3,5], f'expected [3,5] but got {result}'