'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
'''
# .......... SOLUTION ..........
n = int(input().strip())  # this is an integer taken from the input

# Check to see if the mod of n does not = 0 (meaning odd number)
if n % 2 != 0:
    print("Weird")  # If above is true
else:  # If even number
    if n > 20 or n >= 2 and n <= 5:  # If number is bigger than 20 or is in the range 2-5
        print("Not Weird")  # if above is true
    elif n >= 6 and n <= 20:  # if the number is in the range 6-20
        print("Weird")  # if above is true
