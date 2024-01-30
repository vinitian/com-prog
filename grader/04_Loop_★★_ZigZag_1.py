n = int(input())
a = [0]*n ; b = [0]*n

for i in range(n):
    if i%2 == 0: ## even row
        a[i], b[i] = [int(x) for x in input().split()]
    else: ## odd row
        b[i], a[i] = [int(x) for x in input().split()]

z = input()

if z == 'Zig-Zag':
    min = min(a)
    max = max(b)
else: # z == 'Zag-Zig'
    min = min(b)
    max = max(a)
    
print(min, max)