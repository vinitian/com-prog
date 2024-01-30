import math

# Input

n = int(input())
arr = []
num = 0


for x in range(0, n):
    num = int(input())
    arr.append(num)
    
m = min(arr)
M = max(arr)

print(m)
print(M)