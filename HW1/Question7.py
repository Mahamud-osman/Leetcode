"""
7. Find the Second Largest Element
Write a function to find the second-largest element in an array without sorting the array. Use indexing to traverse the array twice.
"""

# How to find larrgest
# [1,5,3,9,4,8]       return 2nd largest

# How to find largest
# Keep track of largest, compare every number to largest

def findSecondLargest(nums):

    largest = nums[0]
    
    for n in nums:
        if n > largest:
                largest = n
    
    second_largest = nums[0]
    
    for n in nums:
        if n > second_largest and n != largest:
                second_largest = n
            
    print("second_largest", second_largest)
    return second_largest

"""
This one was a little tricky but realized I could traverse once, find the largest and exclude it from the 2nd traversal
"""



#Manual Testing
result = findSecondLargest( [1,5,3,9,4,8] )
assert result == 8, f'Expcted 8, but got {result}'