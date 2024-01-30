ID = []
grade = []
level = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

s = input()
while s != 'q':
    a, b = s.split()
    ID.append(a)
    grade.append(b)
    s = input()
upgrade = input().split()

# upgrade
for i in range(len(upgrade)):
    j = ID.index(upgrade[i])
    if grade[j] != 'A':
        grade[j] = level[level.index(grade[j])+1]

# sort
sortedID = sorted(ID)
sortedGrade = [0]*len(grade)
for i in range(len(ID)):
    sortedGrade[i] = grade[ID.index(sortedID[i])]
    print(sortedID[i], sortedGrade[i])