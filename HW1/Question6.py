"""
6. Rotate an Array by One Position
Write a function that rotates an array to the right by one position (i.e., the last element moves to the first position).
nums = [1,2,3,4,5]
output = [5,1,2,3,4]

For all the three problems the trick is in using an extra variable that holds the value of an element which you are moving.
You don't want to overwrite an array element without saving it first. If you want to put value X in position a[i], first save the value of a[i] in the variable,
let's call it buffer, buffer = a[i]. Now you can put anything in a[i] since you copied the value, so you can do a[i] = X. 
Since X has now been placed in its place, you don't need its value, you can now overwrite X = buffer, since buffer has the value that must be moved to the next position: i+1. T

the pseudocode is like this:

X = ? # think what should X be equal to initially
for i: 0..n-2:
  buffer = a[i]
  a[i] = X
  X = buffer
"""

def rotateArray(nums):
    
    last_value = nums[-1]
    
    for i in range(len(nums)):
        current = nums[i]       #Stash our current value
        nums[i] = last_value    #Make our last value = current val 
        last_value = current
    
    print(nums)
    return nums


    # pass

#Manual testcases

result = rotateArray([1,2,3,4,5])
assert result == [5,1,2,3,4], f'Expected [5,1,2,3,4] but got {result}'

result = rotateArray([1,2])
assert result == [2,1], f'Expected [2,1] but got {result}'