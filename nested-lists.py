'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
# ..........SOLUTION..........

mylist = [[input(), float(input())]
          for _ in range(int(input()))]  # make a list with names and marks
# making a list of marks, making it a set (remove duplicates), sorting it
second_highest_grade = sorted(set([x[1] for x in mylist]))
print("\n".join(sorted(name for name,
                       marks in mylist if marks == second_highest_grade[1])))
# make each answer a new line, join for string, search for name (sorted by name) in my list (for name, marks as it is a nested list) and if mark = second highest add the name to the list ..... answer


# ..........LONG..........
if __name__ == '__main__':  # Checking the file is correct
    students = []  # Make a list
    for _ in range(int(input())):  # looking through people in range (n input given)
        name = input()  # name of person
        score = float(input())  # score for person
        students.append([name, score])  # putting name and score into the list

    students = sorted(students, key=lambda x: x[1])  # sorting list (by score)
    # sorted(list,key)
    #second_lowest_score = students[1][1]
    second_lowest_score = sorted(list(set([x[1] for x in students])))[
        1]  # finding second score as a number

    desired_students = []  # student list
    for stu in students:  # look through students lists made above
        if stu[1] == second_lowest_score:  # does the mark = second lowest
            # add the name to the student list if = second mark
            desired_students.append(stu[0])
    # pring one different lines, sorted version of the desired students list.
    print("\n".join(sorted(desired_students)))
