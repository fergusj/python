#encoding:utf8

"""素数（质数）指的是不能被分解的数，除了1和它本身之外就没有其他数能够整除。

求100以内的所有素数。"""
#----------------------------------------------------------------------
''''def isprime(n):
    """"""
    k = n
    i = 1
    l = []
    
    for i in xrange(1, k):
        if n % i == 0:
            l.append(i)
            l.append(k)
            i += 1
            k = k / i            
    
    print l
    
isprime(100)'''



def isPrimeNumber(n, s):
    for k in s:
        if k * k > n: break
        if n % k == 0: return None
    return n

prime = []
for n in range(2, 100):
    res = isPrimeNumber(n, prime)
    if res: prime.append(res)

print prime        