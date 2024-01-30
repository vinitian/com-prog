# Q2: Expression

import math

def f(x, m, s):
    if x > 0 and m != 0 and s > 1:
        return round(((2*math.pi)**(-0.5))*(s**-1)*math.e**(-0.5*(((x-m)/s)**2)),2)
    else:
        return "Invalid input"
        
x, m, s = [ float(e) for e in input().split() ]
print(f(x, m, s))