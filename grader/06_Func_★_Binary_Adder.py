a,b = [int(x,2) for x in input().split()]

sum = bin(a+b)
sum = sum[2:]
print(sum)