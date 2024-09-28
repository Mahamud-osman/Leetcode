
"""
1. Find the Maximum Element
Write a function that iterates over an array and returns the maximum element. Use simple array indexing to access each element.

"""
def maxNums(nums):
    if len(nums) == 0:
        return -1

    current_max = nums[0]
    
    for n in nums:
        if n > current_max:
            current_max = n

    print('current_max:', current_max)  

    return current_max

# Manual tests using assertions
result = maxNums([1, 5, 3, 7, 2])
assert result == 7, f"Expected 7, but got {result}"

result = maxNums([10])
assert result == 10, f"Expected 10, but got {result}"

result = maxNums([-10, -20, -30, -5])
assert result == -5, f"Expected -5, but got {result}"

result = maxNums([-10, 5, 0, 100, -50])
assert result == 100, f"Expected 100, but got {result}"

result = maxNums([3, 3, 3, 3])
assert result == 3, f"Expected 3, but got {result}"

print("All tests passed!")
