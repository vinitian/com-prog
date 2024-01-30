import math

n = int(input())
ans = input()

adrian = 'ABC'*(math.floor(n/3)) + 'ABC'[:n%3]
bruno = 'BABC'*(math.floor(n/4)) + 'BABC'[:n%4]   
goran = 'CCAABB'*(math.floor(n/6)) + 'CCAABB'[:n%6]

a = 0
b = 0
g = 0

for i in range(len(ans)):
    if ans[i] == adrian[i]:
        a += 1
    if ans[i] == bruno[i]:
        b += 1
    if ans[i] == goran[i]:
        g += 1
        
m = max(a,b,g)
print(m)
if a == m:
    print('Adrian')
if b == m:
    print('Bruno')
if g == m:
    print('Goran')