sales = [int(x) for x in input().split()]
sum = 0
for i in range(len(sales)):
    sum += sales[i]
    
print(sum)