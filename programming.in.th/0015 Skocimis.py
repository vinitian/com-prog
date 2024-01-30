num = [int(e) for e in input().split()]

count = 0
d = max([num[1]-num[0], num[2]-num[1]])
print(num)
while d != 1:
    if num[1]-num[0] > num[2]-num[1]:
        num[2] = num[0]+1
    else:
        num[0] = num[1]+1
    num = sorted(num)
    #print(f'{d} | {num[0]} {num[1]} {num[2]}')    
    d = max([num[1]-num[0], num[2]-num[1]])
    count += 1
    
print(count)
