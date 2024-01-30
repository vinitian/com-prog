# 0013 Seven Dwarves


hat = []
for i in range(9):
    hat.append(int(input()))

 
for s in range(512):
    
    s = '0'*(9 - len(bin(s)[2:])) + bin(s)[2:]
    if s.count('1') != 7:
        continue
    real = []
    for i in range(9):
        if s[i] == '1':
            real.append(hat[i])
    #print(s, sum(real))
    if sum(real) == 100 and len(real) == 7:
        break


for num in real:
    print(num)