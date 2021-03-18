'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.
'''
# ..........SOLUTION..........
n = int(input())
nums = map(int, input().split())
# Set removes duplicates, make it a list, sort the list, pick the second to last number)
print(sorted(list(set(nums)))[-2])
