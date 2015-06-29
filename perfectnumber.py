#encoding:utf8

"""完全数（Perfect number)，又称完美数或完备数，是一些特殊的自然数。

它所有的真因子(即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如，第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

编程求10000以内的完全数。"""

#----------------------------------------------------------------------
def isPerfect(n):
    """"""
#    zhenyinzi = [x for x in xrange(1, n) if(n % x == 0):  return x]
    l = []
    for x in xrange(1, n):
        if (n % x == 0 ):
            l.append(x)            
    
    return sum(l) == n

for i in xrange(10000):
    
    if isPerfect(i):
        print i
        
        

def isPerfectNumber(n):
    a = 1
    b = n
    s = 0

    while a < b:
        if n % a == 0:
            s += a + b
        a += 1
        b = n / a

    if a == b and a * b == n:
        s += a

    return s - n == n

for k in range(2, 10000):
    if isPerfectNumber(k):
        print k
           