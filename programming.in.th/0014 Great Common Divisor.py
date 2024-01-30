# finding GCD using Euclidean algorithm

a, b = [int(e) for e in input().split()]

while b != 0:
    a, b = b, a%b
    
print(a)