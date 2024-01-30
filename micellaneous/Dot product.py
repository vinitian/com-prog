# Dot product

u = [float(x) for x in input().split()]
v = [float(x) for x in input().split()]
dot = 0

for i in range(len(u)):
    dot += u[i] * v[i]

print(dot)