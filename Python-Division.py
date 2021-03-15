'''
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
'''
# ..........SOLUTION..........
a = int(input())  # Integer Input number
b = int(input())  # Integer Input number
print(a//b)  # Integer division
print(a/b)  # Float division
