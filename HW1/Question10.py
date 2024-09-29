""""
10. Find the Peak Element
Write a function that finds a "peak element" in an array, where a peak element is one that is greater than its neighbors. Use array indexing to compare elements.
nums = [0,3,6,9,11,12]

Human intuition:
tracking to indecies, from position 0 and 1, if both indices subtracted = 1, return j
"""


def peakElement(nums):
    
    if len(nums) < 2:
        return - 1
    
    peak_index = 1 # since we want to subtract number before
    
    for i in range(len(nums)):
        if nums[peak_index] - nums[i] == 1:
            print('Peak Index',nums[peak_index] )
            return nums[peak_index]
        peak_index += 1     #Increment the peak index after for loop
 

""""
I think the track for me here was figuring out to start the peak_index search at 1
"""





#Manual testing
result = peakElement([0,3,6,9,11,12,14])
assert result == 12, f'Expected 12, but got {result}'

result = peakElement([10,20,30,55,56,99])
assert result == 56, f'Expected 56, but got {result}'