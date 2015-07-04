#encoding:utf8
"""220的真因数之和为1+2+4+5+10+11+20+22+44+55+110=284
284的真因数之和为1+2+4+71+142=220
毕达哥拉斯把这样的数对A、B称为相亲数：A的真因数之和为B，而B的真因数之和为A。

求100000以内的相亲数。
"""


"""
#第一步就真因素和
def proper_factor(n):
    point=1
    w=n
    sum=0
    
    while point <= w:#这个不好的原因是把每次判断相等都放到循里面了，放到point<w这个循环结束更娇高效
        if n%point==0:
            w=w/point            
            if point==w:
                sum +=point
            else:
                sum +=point + w
            
        point +=1
            
    return sum-n
#判断是否为相亲数
def Amicable_Pair(a,b):
    A=proper_factor(a)
    B=proper_factor(b)
    if A==b and B==a:
        print a,b
    
print proper_factor(220)
for a in xrange(1,1000):
    for b in xrange(a+1,1000):
        Amicable_Pair(a,b)
        
"""


def sumOfFactors(k):
    p = 1 
    q = k 
    s = 0 
    while p < q:
        if k % p == 0:
            s += p + q 
        p += 1
        q = k / p 

    if k == p * q and p == q:
        s += p

    return s - k 

def fun(start, end):
    for x in range(start, end):
        y = sumOfFactors(x)
        if x < y and sumOfFactors(y) == x:
            print x, y
    
fun(2, 10000)
