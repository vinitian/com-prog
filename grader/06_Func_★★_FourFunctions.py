def make_int_list(x):
    # Receive x as sring input and convert them into int list
    # EX: x = '12 34 5' returns [12, 34, 5]
    l = [int(e) for e in x.split()]
    return l

def is_odd(e):
    # Return true if e is an odd number, otherwise return false
    return e%2 == 1
    
def odd_list(alist):
    # Return a list which is like alist but contains only odd numbers
    # EX: alist = [10, 11, 13, 24, 25] returns [11, 13, 25]
    l = []
    for e in alist:
        if is_odd(e):
            l.append(e)  
    return l

def sum_square(alist):
    # Return a sum of square of each number in alist
    # EX: alist = [1, 3, 4] returns (1*1 + 3*3 + 4*4), which is 26
    sum = 0
    for e in alist:
        sum += e**2
    return sum
    
exec(input().strip())