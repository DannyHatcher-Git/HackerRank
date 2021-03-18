'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.
'''
# ..........SOLUTION 1..........
n = int(input())
nums = map(int, input().split())
# Set removes duplicates, make it a list, sort the list, pick the second to last number)
print(sorted(list(set(nums)))[-2])

# .......... SOLUTION 2 ..........
if __name__ == '__main__':
    n = int(input())
    # make input into a list, turn them all into integers, then remove duplicates, make a list, sort the list.
    arr = sorted(list(set(map(int, input().split()))))
    # print the vale in the list 2 back from the start so 2 from the end.
    print(arr[-2])
