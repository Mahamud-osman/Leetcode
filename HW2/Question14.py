""""
14. Print a Right-Angled Triangle
Write a program that prints a right-angled triangle of height N using the * character.
Example:
*
**
***
****

"""

def rightAngle(N):
    for i in range(1, N + 1):
        print('*' * i)


result = rightAngle(10)