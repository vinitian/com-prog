n = int(input())
names = []
for i in range(n):
    names.append(input())

fullName = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]
check = 0

for i in range(len(names)):
    for j in range(len(fullName)):
        # check fullName
        if names[i] == fullName[j]:
            print(nickname[j])
            check = 1
            
        # check nickname
        elif names[i] == nickname[j]:
            print(fullName[j])
            check = 1
    if check == 0:
        print("Not found")
    check = 0