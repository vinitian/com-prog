h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

s = (s2 - s1) % 60
m = (m2 - m1) % 60
h = (h2 - h1) % 24 # -1%24 = 23

# ทดเลขหลักนาที 
if s1>s2:
    m = (m - 1) % 60
    # ทดเลขหลักชั่วโมง
    if m == 59: 
        h = (h - 1) % 24

# ทดเลขหลักชั่วโมง
if m1>m2:
    h = (h - 1) % 24

print(str(h)+":"+str(m)+":"+str(s))