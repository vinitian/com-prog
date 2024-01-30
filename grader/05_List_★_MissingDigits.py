s = input()
num = [0,1,2,3,4,5,6,7,8,9]

for i in reversed(range(10)): # can also use range(9,-1,-1)
    if str(i) in s:
        num.pop(i)

if len(num) == 0:
    print("None")
else:
    for i in range(len(num)):
        if i != len(num)-1:
            print(str(num[i]) + ',', end='')
        else:
            print(str(num[i]))
