'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

# ..........SOLUTION..........
if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()  # pupil inputs (id name, *line (everything after))
        # line is the group of scores after name. Scores made a float then into a list called scores.
        scores = list(map(float, line))
        # putting the name and scores into the dictionary
        student_marks[name] = scores
    query_name = input()  # Who to search for to output the score
    marks = []  # Marks of the selected student
    if query_name in student_marks:  # look for query student in the dictionary
        # puts the marks of the student in a list
        marks = student_marks[query_name]
        # finds the list (marks) average and formats to 2sf
        print("{:.2f}".format(sum(marks)/len(marks)))
