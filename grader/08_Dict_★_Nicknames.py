def reverse(d):
    new_d = {}
    for x in d:
        new_d[d[x]] = x
    return new_d

n = int(input())
name = {}
for i in range(n):
    a, name[a] = input().split()
 
name2 = reverse(name)

m = int(input())
for i in range(m):
    b = input()
    
    if b in name:
        print(name[b])
    elif b in name2:
        print(name2[b])
    else:
        print('Not found')