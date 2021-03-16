'''
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
'''
# ..........SOLUTION..........
n = int(input())
for i in range(n):  # Go from 0 - n (n is not included)
    print(i**2)  # Print i ^ 2 (to the opwer of is **)
