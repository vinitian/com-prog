x = input().split()
while x[0] != 'q':
    a, b = int(x[0]), int(x[1])
    while b!= 0:
        a, b = b, a%b
    print(a)
    
    x = input().split()