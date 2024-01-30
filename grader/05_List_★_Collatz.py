n = int(input())
num = [n]

while n != 1:
    if n%2 == 0:
        n = n//2
        num.append(n)
    else:
        n = 3*n + 1
        num.append(n)
num.append(-1)

num = [ str(x) for x in num ]
print('->'.join(num[-16:-1]))