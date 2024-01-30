a = float(input())
b = a
L = 0
U = 1

while b//10 != 0.0:
    U += 1
    b = b//10
    
x = (L + U)/2

while abs(10**x - a) > (10**(-10))*max(a, 10**x):
	if 10**x > a:
		U = x
	else:
		L = x
	x = (L + U)/2

print(round(x, 6))