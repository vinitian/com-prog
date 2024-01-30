# detect repitition in list

def has_duplicate(x):
    print(x)
    for i in x[:-1]:
        for j in range(i+1, len(x)):
            print(i, x[j])
            if i == x[j]:
                return True
    return False

print(has_duplicate([11,34,22,35]))

            
        