c = 1
s = input()
while s != 'Zig-Zag' and s != 'Zag-Zig':
    
    if c%2 == 1:
        a, b = [int(e) for e in s.split()]
    else:
        b, a = [int(e) for e in s.split()]
        
    if c == 1:
        aM = a ; am = a
        bM = b ; bm = b
        
    else:
        if a > aM:
            aM = a
        elif a < am:
            am = a
        
        if b > bM:
            bM = b
        elif b < bm:
            bm = b
    c += 1
    s = input()
    
if s == 'Zig-Zag':
    print(am, bM)
else:
    print(bm, aM)