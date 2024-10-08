""""
12. Find the First Prime Number in an Array
Iterate over an array and find the first prime number. Stop the iteration once you find it.

Prime Number: a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
"""


def findPrime(nums):
    
    for i in range(len(nums)):
        print(nums[i])
        if isprime(nums[i]):
            print(nums[i])
            break

def isprime(N):
    for i in range(2, N + 1):
        if N % i == 0:
            return False
    return True




#Manual Testing
result = findPrime([1,3,4,8,10])
assert result == 3, f'Expected 3 but got {result}'


# # [5 3 2 4 5 1], 4
# # 
# # (0, N)
# # 
# # 
# def findPrime(nums):
#   	for i in range(len(nums)):
#       for j in range(2, nums[i]):
#         if nums[i] % j == 0:
#           print(nums[i])
#           break

# def fun()
#   print(10)
# # 1..num
# # range(10, 100) range(100) 0..99
# def hasFactors(num):
#   for i in range(1, num + 1):
#     if num % i == 0:
#       return True
#   return False

# def findFactors(num):
#   for i in range(1, num + 1):
#     if num % i == 0:
#       print(i)
#   return True

# # N = 7
# # 2..7
# # Prime number that's only divisible by self or 1: 2, 3, 5, 7, 11, 13
# # 2..(N-1) -> 2..6
# # 10 -> 2..9
# # range(a, b) -> a, a + 1, b-1 
# # range
# def isprime(N):
#     for i in range(2, N):
#         if N % i == 0:
#           	print i
#             return False
#     return True


