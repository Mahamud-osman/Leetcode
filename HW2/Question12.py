""""
12. Find the First Prime Number in an Array
Iterate over an array and find the first prime number. Stop the iteration once you find it.

Prime Number: a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
"""


def findPrime(nums):
    
    for i in range(len(nums)):
        print(nums[i])
        # if nums[i] != 1 and nums[i]/nums[i + 1] != 0:
        if isprime is True:
            print(nums[i])
            break

def isprime(num):

    if num != 1 and num/num == 0:
        print('num is prime')




#Manual Testing
result = findPrime([1,3,4,8,10])
assert result == 3, f'Expected 3 but got {result}'