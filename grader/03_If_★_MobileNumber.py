x = input()

if len(x) == 10 and (x[0:2] == '06' or x[0:2] == '08' or x[0:2] == '09'):
    print("Mobile number")
else:
    print("Not a mobile number")