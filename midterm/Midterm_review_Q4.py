def f1(l, x):
    maxIndex = 0
    minIndex = 0
    j = 0
    
    while j != len(l):
        if l[j]*x < l[minIndex]*x:
            minIndex = j
        if l[j]*x > l[maxIndex]*x:
            maxIndex = j
        j += 1
    
    s = ''
    s += str(l[minIndex]) + ' ' + str(l[maxIndex])
    return print(s)

exec(input().strip())