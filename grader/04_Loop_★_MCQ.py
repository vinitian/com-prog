# Answer checker

ans = input() # correct answer
stu = input() # student's answer
score = 0

if len(ans) != len(stu):
    print("Incomplete answer")
else:
    for i in range(len(ans)):
        if ans[i] == stu[i]:
            score += 1
    print(score)

