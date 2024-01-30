n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = [ float(x) for x in input().split() ]

distance = [0]*n
for i in range(n):
    distance[i] = ( x[i]**2 + y[i]**2 )**0.5
    
sortedDistance = sorted(distance)

for i in range(n):
    if (x[i]**2 + y[i]**2 )**0.5 == sortedDistance[2]:
        print('#{}: ({}, {})'.format(i+1, x[i], y[i]))   