a = 'kusunoki muu is so cute'
a_list = a.split()
l = len(a_list)
for n in reversed(range(1,l+1)):
    print('n = ' + str(n))
    for i in range(l):
        if i+n <= l:
            print(str(i)+':'+str(i+n) + ' is ', end='')
            kw = ' '.join(a_list[i:i+n])
            print(kw)
    