mname = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
zsign = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']

def read_date():
    # Read the day, month, and year separated by space.
    # Return a list containing the day, month, and year.
    date = input().split()
    date[1] = mname.index(date[1]) + 1
    date = [int(e) for e in date]
    return date

def zodiac(d,m):
    # Return the zodiac sign given the day (d) and month (m).
    if m in [1, 2]:
        if d > 20:
            sign = zsign[m-12]
        else:
            sign = zsign[m-13]
    elif d > 21:
        sign = zsign[m-12]
    else:
        sign = zsign[m-13]
            
    return sign

def days_in_feb(y):
    # Return the number of days in February of the given year (y).
    days = 0    
    if (y%400==0) or (y%4==0 and y%100 != 0):
        days = 29
    else:
        days = 28
    return days
    
def days_in_month(m,y):
    # Return the number of month given the month (m) and year (y).
    days = 0
    if m == 2:
        days = days_in_feb(y)
    elif m in [4,6,9,11]:
        days = 30
    else:
        days = 31
    return days

def days_in_between(d1,m1,y1,d2,m2,y2):
    # Return the number of days from d1 m1 y1 to d2 m2 y2.
    total = 0
    
    # from (1) to end of year
    for i in range(12,m1,-1):
        total += days_in_month(i, y1)
        # print(i, days_in_month(i, y1), total)
    total += days_in_month(m1,y1) - d1
    # print(total)
   
    # years
    for i in range(y1+1,y2):
        total += 337 + days_in_feb(i)
        # print(i, 337 + days_in_feb(i), total)
    # print(total)
    
    # from start of year to (2)
    for i in range(m2-1):
        total += days_in_month(i+1, y2)
        # print(i+1, days_in_month(i+1, y2), total)
    total += d2
    total -= 1
    return total

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    # Display the zodiac sign of d1 m1 y1 and d2 m2 y2 on the same line, separated by space.
    print(zodiac(d1, m1), zodiac(d2, m2))

    #Display the number of days from d1 m1 y1 to d2 m2 y2.
    print(days_in_between(d1,m1,y1,d2,m2,y2))
    
exec(input().strip())
