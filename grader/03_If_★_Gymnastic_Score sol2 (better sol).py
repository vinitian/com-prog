#try avoid using min and max

a, b, c, d = [ float(x) for x in input().split()]

if a>c:
    a,c = c,a
if b>d:
    b,d = d,b
if a>b:
    a,b = b,a
if c>d:
    c,d = d,c
if b>c:
    b,c = c,b
    
print(a,b,c,d)

final = round((b+c)/2, 2)
print(final)