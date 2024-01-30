x = []
for i in range(10):
    x.append(int(input()))
    
re = []
for i in x:
    if i%42 not in re:
        re.append(i%42)
    
print(len(re))