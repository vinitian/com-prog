h = int(input())
line = 0

for i in range(h-1):
    if i == 0:
        print(' '*(h-1) + '*' + ' '*(h-1))
    else:
        line = ' '*(h-i-1) + '*' + ' '*(2*i-1) + '*'+' '*(h-i-1)
        print(line)

print('*'*(2*h-1))

