""""
16. Print a Pyramid of Numbers
Write a program that prints a pyramid of numbers of height N, where the numbers increase along each row.
   1
  1 2
 1 2 3
1 2 3 4
"""

def printPyramid(N):
    # for i in range(1, N + 1):
    #     print(i)
    #     for i in range(1, N + 1):
    #         print(i)
    #         for i in range(1, N + 1):
    #             print(i)
    #             for i in range(1, N + 1):
    #                 print(i)
    pyramid_builder = 0
    for i in range(N + 1):
        pyramid_builder += 1
        print(i , pyramid_builder)



result = printPyramid(4)