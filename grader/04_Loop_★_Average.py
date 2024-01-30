x = input()
sum = 0
count = 0

while x != 'q':
    sum += float(x)
    count += 1
    x = input()
    
if count == 0:
    print('No Data')
else:
    print(round(sum/count, 2))