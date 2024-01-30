card = input().split()
order = input()
n = len(card)
shuffle = [0]*n
half1 = card[:n//2]    
half2 = card[n//2:]
    
for i in range(len(order)):
    # cut
    if order[i] == 'C':
        card = half2 + half1
        
    # shuffle    
    if order[i] == 'S':
        for i in range(n):
            if i%2 == 0:
                card[i] = half1[i//2]
            else:
                card[i] = half2[i//2]
                
    half1 = card[:n//2]    
    half2 = card[n//2:]            

for i in range(n):
    print(card[i], end=" ")