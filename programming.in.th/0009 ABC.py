x = [int(e) for e in input().split()]
x = sorted(x)

s = input()
for i in range(3):
    if s[i] == 'A':
        print(x[0], end=' ')
    elif s[i] == 'B':
        print(x[1], end=' ')
    elif s[i] == 'C':
        print(x[2], end=' ')