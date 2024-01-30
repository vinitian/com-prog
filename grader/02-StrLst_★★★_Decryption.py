x = input()

a = x[3::7]
b = x[7::5]
c = int(a) + int(b) + 10000
d = str(c)[-4:-1]
e = (int(d[0]) + int(d[1]) + int(d[2]))%10 +1
f = chr(64+e)
g = d + f

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
print(g)