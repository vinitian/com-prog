'''
toAdd = ["Southampton", "Arsenal", "Liverpool"]

for i in toAdd:
    print("hi, " + i)
    
'''

# s = "Team        |Pld|Pts|Dif|For|Agst|"

f = open("hw2text.txt", "r")
s = f.readlines()
s.pop(0)
for i in range(len(s)):
    s[i] = s[i].strip("|\n")
    
a = []

for i in range(len(s)):
    a.append(s[i].split("|"))

for i in range(len(s)):
    for j in range(6):
        a[i][j] = a[i][j].strip()
        if j != 0:
            a[i][j] = int(a[i][j])
print(a)