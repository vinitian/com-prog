s = input()
c = s[0]
count = 0

print(c + ' ', end='')

for i in range(len(s)):
    if s[i] == c:
        count += 1
    else:
        print(str(count) + ' ', end='')
        c = s[i]
        print(c + ' ', end='')
        count = 1
print(count)