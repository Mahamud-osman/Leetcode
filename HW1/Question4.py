"""
4. Count Negative Numbers
Write a function that iterates over an array and counts how many negative numbers it contains.
nums = [1,3,-1,0,-4,5]
output = 2
"""

def countNegatives(nums):
    # How to appraoch the problem
    #Increment and have a check to if number is less than zero
    # if number is less than zero increment negative counter
    # return counter
    #Handle edge case
    if len(nums) == 0:
        return - 1

    negative_counter = 0
    
    for i in range(len(nums)):
        if nums[i] < 0:
            negative_counter += 1
    
    print("Negative counter:", negative_counter)
    return negative_counter

#Manual Testing

result = countNegatives([1,3,-1,0,-4,5])
assert result == 2, f'expected 2 but got {result}'

result = countNegatives([-1,-3,-1,0,-4,-5])
assert result == 5, f'expected 5 but got {result}'

result = countNegatives([1,3,1,5])
assert result == 0, f'expected 0 but got {result}'