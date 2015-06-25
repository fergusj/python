# encoding:utf8
# 水仙花数是指一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。
# 例如：1^3+5^3+3^3=153。
# 求100~999之间所有的水仙花数。

# 它的每个位上的数字
# 的n次幂之和
# 等于
# 它本身。
"""def isArmstrongnumber(n):
    l = []
    while n != 0:
        s = n % 10
        n /= 10
        l.append(s)
    for y in l:
        if y ** len(l) == n:    
            return True
        else:
            return False

for x in xrange(100, 999):
    if isArmstrongnumber(x):
        print x
"""

#def isArmstrongNumber(n):
    #a = []
    #t = n
    #while t > 0:
        #a.append(t % 10)
        #t /= 10

    #k = len(a)
    #return sum([x ** k for x in a]) == n

#for x in range(100, 10000):
    #if isArmstrongNumber(x): 
        #print x
        
        
def isA(n):
    #True or False
    a = []
    t = n
    while t > 0:
        a.append(t % 10)
        t /= 10
        
    k = len(a)
    s = 0
    for x in a:
        s += x ** k
    
    return s == n
    #return sum([x**len(a) for x in a]) == n
    
for x in xrange(100, 1000):
    if isA(x): print x

#整数取前3位 123456/10**(n-3)
#取后3位   123456%10**3
    
    
def isB(n):
    temp = str(n)
    return sum([int(x) ** len(temp) for x in temp]) == n

for x in xrange(100, 1000):
    if isB(x): print x
