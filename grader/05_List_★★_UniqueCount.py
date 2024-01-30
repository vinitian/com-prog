a = [ int(x) for x in input().split() ]
l = sorted(a)
x = l[0]
count = 1
show = [x]

for i in range(len(l)):
    if l[i] != x:
        x = l[i]
        count += 1
        if len(show) < 10:
            show.append(x)

print(count)
print(show)