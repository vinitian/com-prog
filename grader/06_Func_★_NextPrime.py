def is_prime(n):
    #check is n is a prime number
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(n):
    # return the least prime number which is more than n
    for i in range(n+1, 2*n):
        if is_prime(i):
            return i
    
def next_twin_prime(n):
    # return the least twin prime number which is more than n
    # twin prime number are 2 prime numbers differed by 2 //e.g. 11&13, 41&43
    p = n
    while True:
        p = next_prime(p)
        if next_prime(p) == p+2:
            return p, p+2

exec(input().strip())