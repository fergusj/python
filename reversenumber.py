#encoding:utf8
"""所谓反序数，即有这样成对的数，
其特点是其中一个数的数字排列顺序完全颠倒过来，就变成另一个数，如102和201，36和63等，
简单的理解就是顺序相反的两个数，我们把这种成对的数互称为反序数。反序数唯一不可能出现以0结尾的数。
一个3位数各位上的数字都不相同，它和它的反序数的乘积是280021，这个3位数应是多少？"""

"""定义一个函数，求一个数的反序数
    从100-999依次测试成绩
"""

"""""def reversenumber(n):
    t = [ i for i in str(n)]    
    t.reverse()
    u = ""
    for x in t:
        u += x
    return int(u)
for i in xrange(101, 500):
    if reversenumber(i) * i == 280021:
        print i"""""

# a:(1-9), b:(0-9), c:(1-9)分析范围，缩小范围
# a != b != c 分析特征，缩小范围
# a < c 分析特征 缩小范围
count = 0
for b in range(10):
    for a in range(1, 10):
        if a == b: continue#continue的用法，相当于该循环时，什么也不做，继续下一个循环
        for c in range(a + 1, 10):
            if c == b: continue
            count += 1
            t1 = 100 * a + 10 * b + c
            t2 = 100 * c + 10 * b + a
            if t1 * t2 == 280021: print t1, t2            
            

print count  #只乘法了288次就可以了 