"""
Sum of Elements in an Array
Write a function that computes the sum of all elements in an array using array indexing.
nums = [0,1,2,3,4]
"""
def sumElements(nums):
    
    if len(nums) == 0:
        return -1
    currSum = 0
    
    for i in range(len(nums)):
        currSum += nums[i]
    print('Sum:', currSum)
    
    return currSum
    
    # Loop through all the elemets using index
    # Add the element into the array
    

result = sumElements([10,20,30,40,50])
assert result == 150, f'excpected 150 but got {result}'


result = sumElements([0,1,2,3,4])
assert result == 10, f'excpected 10 but got {result}'