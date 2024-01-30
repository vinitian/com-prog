x = [1,0,0]
s = input()
for i in range(len(s)):
    if s[i] == 'A':
        x[0], x[1] = x[1], x[0]
    elif s[i] == 'B':
        x[2], x[1] = x[1], x[2]
    elif s[i] == 'C':
        x[0], x[2] = x[2], x[0]
        
print(x.index(1)+1)