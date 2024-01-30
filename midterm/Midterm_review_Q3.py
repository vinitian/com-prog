# Q3 search card game

def show(d):
    for e in d:
        print(e)
        
def search(m, keyword, power):
    search = []
    if keyword != '-':
        for i in range(len(m)):
            a = m[i][0].split() + [e.strip(':') for e in m[i][1].split()]
            if keyword in a:
                if power == '-':
                    search.append(m[i])  
                else:
                    if power == str(m[i][2]):
                        search.append(m[i])
    else:
        for i in range(len(m)):
            if power == '-':
                search.append(m[i])  
            else:
                if power == str(m[i][2]):
                    search.append(m[i])

    return search
    
    
    
m1 = ["green giant", "sacrifice a monster: draw a card", 5]
m2 = ["blue giant", "tap: draw a card, then discard a card", 3]
m3 = ["blue drake", "discard a card: return to hand", 1]
m4 = ["green drake", "sacrifice a land: destroy target giant", 3]
m5 = ["black wurm", "sacrifice a permanent: destroy target permanent", 3]
m = [m1,m2,m3,m4,m5]

exec(input())  