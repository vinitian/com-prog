m = input()
n = int(input())

result = m
if len(m) < n:
    result = "0"*(n-len(m)) + result

print(result)
