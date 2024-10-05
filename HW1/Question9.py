""""
9. Insert an Element at a Specific Index
Write a function that inserts a new element at a specific index in the array, shifting the other elements to the right.
"""

def specificIndex(nums, k, val): 
        nums.append(0)  #Increase size of array

        last_value = nums[-1]
    
        for i in range(k, len(nums)):
            current = nums[i]       #Stash our current value
            nums[i] = last_value    #Make our last value = current val 
            last_value = current
        
        
        nums[k] = val           #Assign value at K to val
        
        print(nums)
        return nums

#Add fake element, BS value, rotate and then add K/val



#manual Testing 
result = specificIndex([1,3,5,7,11], 2, 7)
assert result == [1,3,7,5,7,11], f'Expected [1,3,7,5,7,11], but got {result}'

result = specificIndex([2, 4, 6, 8, 10, 12], 3, 9)
assert result == [2, 4, 6, 9, 8, 10, 12], f'Expected [2, 4, 6, 9, 8, 10, 12], but got {result}'

