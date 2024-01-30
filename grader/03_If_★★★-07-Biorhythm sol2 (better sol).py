import math

bd, bm, by, d, m, y = [int(x) for x in input().split()]
total = 0
mlist = [31,28,31,30,31,30,31,31,30,31,30,31]

by -= 543
y -= 543

leapYear1 = False
if (by%400==0) or (by%4==0 and by%100 != 0):
    leapYear1 = True

leapYear2 = False
if (y%400==0) or (y%4==0 and y%100 != 0):
    leapYear2 = True
    
#red

## days
if bm in [4, 6, 9, 11]: # m has 30 days
    total = 30 - bd + 1
elif bm == 2: # m has 28 or 29 days
    if leapYear1:
        total = 29 - bd + 1
    else:
    	total = 28 - bd + 1
else: # m has 30 days  
	total =  31 - bd + 1 
 
## month

for i in range(13):
    if bm < i:
        if i == 2:
            if leapYear1:
                total += 29
            else:
                total += 28
        else:
            total += mlist[i-1]  

# -----
# black 

total += 365 * (y-by-1)

# -----
# blue

## days
total += d - 1

## month

for i in range(1,12):
    if m > i:
        if i == 2:
            if leapYear2:
                total += 29
            else:
                total += 28
        else:
            total += mlist[i-1]
            
# -----
# compute & print

physical = math.sin((2*math.pi*total)/23)
emotional = math.sin((2*math.pi*total)/28)
intellectual = math.sin((2*math.pi*total)/33)

print('{} {:.2f} {:.2f} {:.2f}'.format(total, physical, emotional, intellectual))

# 1 1 2559 1 1 2560
# 1 1 2560 1 1 2561
# 20 11 2540 10 2 2544
# 10 8 2541 27 10 2559
# print("red month" + str(total))