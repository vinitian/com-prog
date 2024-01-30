m, n = [int(e) for e in input().split()]

x = []
y = []
for i in range(m):
    x.append([int(e) for e in input().split()])
for i in range(m):
    y.append([int(e) for e in input().split()])
    
sum = []
for i in range(m):
    for j in range(n):
        print(x[i][j] + y[i][j], end =' ')
    print("")