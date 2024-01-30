s = input()
l = len(s)*4+1
# line 1
for i in range(l):
    if i%12 == 10:
        print('*', end='')
    elif i%4 == 2:
        print('#', end='')
    else:
        print(".", end='')
print('')

# line 2
for i in range(l):
    if i%12 == 9 or i%12 == 11:
        print('*', end='')
    elif i%2 == 1:
        print('#', end='')
    else:
        print(".", end='')
print('')
        
#line 3
count = 0
for i in range(l):
    if i%4 == 2:
        print(s[count], end='')
        count += 1
    elif i == l-1:
        if len(s)%3 == 0:
            print('*', end='')
        else:
            print('#', end='')
    elif i != 0 and (i%12 == 8 or i%12 == 0):
        print('*', end='')
    elif i%4 == 0:
        print('#', end='')
    else:
        print(".", end='')
print('')
        
# line 4
for i in range(l):
    if i%12 == 9 or i%12 == 11:
        print('*', end='')
    elif i%2 == 1:
        print('#', end='')
    else:
        print(".", end='')
print('')

# line 5
for i in range(l):
    if i%12 == 10:
        print('*', end='')
    elif i%4 == 2:
        print('#', end='')
    else:
        print(".", end='')