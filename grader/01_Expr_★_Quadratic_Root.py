import math

a = float(input())
b = float(input())
c = float(input())


det = b**2 - 4*a*c

if det<0;
    print("error")

x1 = round((-b - math.sqrt(det))/(2*a), 3)
x2 = round((-b + math.sqrt(det))/(2*a), 3)

print(x1, x2)