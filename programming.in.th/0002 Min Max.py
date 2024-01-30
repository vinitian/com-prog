# Input
n = int(input())
arr = []
num = 0

for x in range(0, n):
    num = int(input())
    arr.append(num)
   
#Compare
m = arr[0]
M = arr[0]

for x in range(0, n):
    if m > arr[x]:
        m = arr[x]
    elif M < arr[x]:
        M = arr[x]
            
print(m)
print(M)        
    
