""""
15. Multiplication Table
Write a program that prints the multiplication table for numbers from 1 to N.
Example: For N=5:

1  2  3  4  5
2  4  6  8  10
3  6  9  12 15
4  8  12 16 20
5  10 15 20 25

15. We won't be using recursion yet! This problem is solved with nested loops. 
Try to solve the problem row by row. 
Think about how you would print numbers from 1 to N. 
Then think how you would print every even number 2, 4, 6, etc. 
Then think how you would print every multiple of 3. 
And so on. 
If i is the row number then every next number in row i, is i added to the previous number. E.g. 4 => 4 + 4 = 8 => 4 + 8 => 12 ...

"""

def multiplicationTable(N):
    for i in range(1, N + 1):
        for x in range(1, N + 1):   
            print(i * x)


        




# Manual testing:
result = multiplicationTable(5)
