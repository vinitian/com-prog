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

for i in range(len(upgrade)):
    j = ID.index(upgrade[i])
    if grade[j] != 'A':
        grade[j] = level[level.index(grade[j])+1]

for i in range(len(ID)):
    print(ID[i], grade[i])