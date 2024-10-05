""""
9. Insert an Element at a Specific Index
Write a function that inserts a new element at a specific index in the array, shifting the other elements to the right.
"""

def specificIndex(nums, k, val): 
        for _ in range(k, len(nums)):
            nums[k] = val
        last_value = nums[-1]
    
        for i in range(len(nums)):
            current = nums[i]       #Stash our current value
            nums[i] = last_value    #Make our last value = current val 
            last_value = current
        
        print(nums)
        return nums

#Add fake element, BS value, rotate and then add K/val



#manual Testing 
result = specificIndex([1,3,5,7,11], 2, 7)
assert result == [1,3,7,5,7,11], f'Expected [1,3,7,5,7,11], but got {result}'
