import math

bd, bm, by, d, m, y = [int(x) for x in input().split()]
total = 0

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
if bm < 2:
    if leapYear1:
    	total += 29
    else:
        total += 28        
if bm < 3:
    total += 31
if bm < 4:
    total += 30
if bm < 5:
    total += 31
if bm < 6:
    total += 30
if bm < 7:
    total += 31
if bm < 8:
    total += 31
if bm < 9:
    total += 30
if bm < 10:
    total += 31
if bm < 11:
    total += 30
if bm < 12:
    total += 31    


# black 

total += 365 * (y-by-1)


# blue

## days
total += d - 1

## month
if m > 1:
    total += 31
if m > 2:
    if leapYear2:
        total += 29
    else:
        total += 28
if m > 3:
    total += 31
if m > 4:
    total += 30
if m > 5:
    total += 31
if m > 6:
    total += 30
if m > 7:
    total += 31
if m > 8:
    total += 31
if m > 9:
    total += 30
if m > 10:
    total += 31
if m > 11:
    total += 30

physical = math.sin((2*math.pi*total)/23)
emotional = math.sin((2*math.pi*total)/28)
intellectual = math.sin((2*math.pi*total)/33)

print('{} {:.2f} {:.2f} {:.2f}'.format(total, physical, emotional, intellectual))

# 1 1 2559 1 1 2560
# 20 11 2540 10 2 2544
# 10 8 2541 27 10 2559