x = [ float(x) for x in input().split() ]
count = 0

for i in range(1,len(x)-1):
    if x[i] > x[i-1] and x[i] > x[i+1]:
            count+=1

print(count)