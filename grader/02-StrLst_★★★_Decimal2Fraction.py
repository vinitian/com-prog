import math

a, b, c = input().split(',')

# finding numerator & denominator
x = int(a + b + c) - int(a + b)
y = int('9'*len(c) + '0'*len(b))

# simplifying numerator & denominator
n = int(x//math.gcd(x, y))
d = int(y//math.gcd(x, y))

print('{0} / {1}'.format(n, d))

# https://www.mathpaper.net/index.php/en/2013-01-01-11-44-04