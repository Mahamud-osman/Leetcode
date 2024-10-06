"""""
18. Print an Inverted Pyramid of Stars
Write a program that prints an inverted pyramid of * characters with a base width of N.
Example: N=5
*****
 ****
  ***
   **
    *
"""


def invertedPyramid(N):
    for i in range(N + 1,0,-1):
        print('*' * i)


result = invertedPyramid(10)