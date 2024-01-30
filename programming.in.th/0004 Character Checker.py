x = input()
check = 0

for i in range(len(x)):
    if ord(x[i]) >= 65 and ord(x[i]) <= 90:
        check += 1
    if ord(x[i]) >= 97 and ord(x[i]) <= 122:
        check -= 1
        
if check == len(x):
    print("All Capital Letter")
elif check == -len(x):
    print("All Small Letter")
else:
    print("Mix")
