"""
8. Left Rotation by K Positions
Write a function to rotate an array to the left (-1) by k positions. Use modular arithmetic to handle the array indexing.
nums = [1,3,5,7,11]
output = [5,7,11,1,3]
"""
def rotatebyK(nums, k): 
    res = []

    for i in range(len(nums)):
        res.append(nums[(i + k)%len(nums)])
    
    print(res)
    return res

    
#Manual testing:
result = rotatebyK([1,3,5,7,11], 2)
assert result ==[5,7,11,1,3], f'Expected [5, 7, 11, 1, 3]. but got {result}'

"""
og_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 4
nums[0]
cp_nums = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6] 

cp_nums[(i+k)%len(nums)] = og_nums[i]
4 % 10 => 4
5 % 10 => 5
9 % 10 => 9
10 % 10 => 0
11 % 10 => 1
12 % 10 => 2

i => (i + k) % n

(6 + 4) % 10

13 % 10 => 3
23 % 10 => 3


"""