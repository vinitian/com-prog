print('milgram ships')
num = ['00', '01', '02', '03', '04', '05','06', '07', '08','09','10']
for i in num:
    for j in num:
        if j > i:
            print(i+j)