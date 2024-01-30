# Program to find mean and standard deviation

# first input: number of values (n)
# the following inputs: x[i]

n = int(input())
x = [0.0]*n
for i in range(n):
    x[i] = float(input())
    
s = 0
for i in range(n):
    s += x[i]
mean = s/n

s2 = 0
for i in range(n):
    s2 += (x[i] - mean)**2
sd = (s2/n)**2

print(mean, sd)