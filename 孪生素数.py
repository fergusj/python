#encoding:utf8
"""
若两个素数之差为2，则这两个素数就是孪生素数。

编写程序找出1~100之间的所有孪生素数。
"""

def isPrime(n):  
    if n <= 1:  
        return False 
    i = 2 
    while i*i <= n:  
        if n % i == 0:  
            return False 
        i += 1 
    return True

for i in xrange(100):
    if isPrime(i):
        if isPrime(i + 2):
            print i, i + 2

    

