#encoding:utf8
# 
"""
黑洞数又称陷阱数，是类具有奇特转换特性的整数。            (整数)
任何一个数字不全相同的整数，                         (数字不全相同)
经有限“重排求差”操作，总会得到某一个或一些数，这些数即为黑洞数。(递归)
“重排求差”操作                                       (函数)
即把组成该数的数字重排后得到的最大数减去重排后得到的最小数。   (最大max-最小min)
举个例子，3位数的黑洞数为495.
简易推导过程：随便找个数，如297,
3个位上的数从小到大和从大到小各排一次，为972和279，相减得693。
按上面做法再做一次，得到594，再做一次，得到495，之后反复都得到495。

问题：验证4位数的黑洞数为6174。"""
#----------------------------------------------------------------------
def blackHole(n):
    """黑洞数"""
    a = [int(i) for i in str(n)]
    a.sort()
    
    minn = 0
    maxn = 0
    
    for b in a:      
        minn = minn * 10 + b
    for c in a[::-1]:
        maxn = maxn * 10 + c
        
    if maxn - minn == n:
        return n
    else:
        #print n
        return blackHole(maxn - minn)
    
print blackHole(297)

"""
def fun(n):
    a = [int(c) for c in str(n)]
    a.sort()

    s1 = reduce(lambda x, y: 10 * x + y, a[::-1])
    s2 = reduce(lambda x, y: 10 * x + y, a)

    return n if s1 - s2 == n else fun(s1 - s2)

res = fun(6294)
print 'res : ', res
"""