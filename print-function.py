'''
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .
'''
# ..........SOLUTION..........

n = int(input())  # Number input
answer = []  # Create a list
for x in range(1, n+1):  # Search for in range 1 to n+1 (so n is included)
    answer.append(str(x))  # Add the string version of x to the answer list
print("".join(answer))  # print the answer list as a string
