#try avoid using min and max

a, b, c, d = [ float(x) for x in input().split()]

if a>b:
    a,b = b,a
if c>d:
    c,d = d,c
if a>d:
    b,d = d,b
    a,c = c,a
if b>c:
    b,c = c,b
if b>d:
    b,d = d,b
if c>d:
    c,d = d,c
if a>b:
    a,b = b,a
    
#print(a,b,c,d)

final = round((b+c)/2, 2)
print(final)