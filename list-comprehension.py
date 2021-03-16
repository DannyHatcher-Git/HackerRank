'''
You are given three integers  and  representing the dimensions of a cuboid along with an integer . 
Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . 
Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
'''
# ..........SOLUTION..........
x = int(input())
y = int(input())
z = int(input())
n = int(input())

answer = [[X, Y, Z] for X in range(x+1) for Y in range(y+1)
          for Z in range(z+1) if X+Y+Z != n]
print(answer)

'''
# If you use for loops
answer=[]
for x in range(x+1): # looking for all number under x+1
    for y in range(y+1): # looking for all number under y+1
        for z in range(z+1): # looking for all number under x+1
            if x+y+z!=n:
                answer.append([x,y,z]) # Put x then y then all z and go to next y, then all x after.
print(answer)
'''
