import math

n = int(input())

lowerBound = math.sqrt(2*math.pi)*(n**(n + 0.5))*(math.e**(-n + 1/(12*n + 1)))
upperBound = math.sqrt(2*math.pi)*(n**(n + 0.5))*(math.e**(-n + 1/(12*n)))

print(lowerBound)
print(upperBound)