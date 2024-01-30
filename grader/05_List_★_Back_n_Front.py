list1, list2, list3 = [],[],[]

# first set
n = int(input())
for i in range(n):
    list1.append(int(input()))
    
# second set
input2 = input()
if input2 != '-1':
    list2 = [ int(x) for x in input2.split() ]
    # third set
    x = int(input())
    while x != -1:
        list3.append(x)
        x = int(input())
    
# print(list1)
# print(list2)
# print(list3)

bigList = list1 + list2 + list3

final = []
for i in range(len(bigList)):
    if i%2 == 0:
        final.append(bigList[i])        
    else:
        final.insert(0, bigList[i])

print(final)