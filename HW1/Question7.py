"""
7. Find the Second Largest Element
Write a function to find the second-largest element in an array without sorting the array. Use indexing to traverse the array twice.
"""

# How to find larrgest
# [1,5,3,9,4,8]       return 2nd largest

# How to find largest
# Keep track of largest, compare every number to largest

def findSecondLargest(nums):
    if len(nums) == 0:
          return -1

    largest = nums[0]
    
    for i  in range(len(nums)):
        if nums[i] > largest:
                largest = nums[i]
    
    second_largest = nums[0]
    
    for i  in range(len(nums)):
        if nums[i] > second_largest and nums[i] != largest:
                second_largest = nums[i]
            
    print("second_largest", second_largest)
    return second_largest

"""
This one was a little tricky but realized I could traverse once, find the largest and exclude it from the 2nd traversal
"""



#Manual Testing
result = findSecondLargest( [1,5,3,9,4,8] )
assert result == 8, f'Expcted 8, but got {result}'

result = findSecondLargest( [10,11,12,16,22,100] )
assert result == 22, f'Expcted 22, but got {result}'

result = findSecondLargest( [15,30,75,22,76,12] )
assert result == 75, f'Expcted 75, but got {result}'