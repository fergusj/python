#encoding:utf8

"""所谓勾股数，一般是指能够构成直角三角形3条边的3个正整数（a,b,c)。
即a²+b²=c²，a，b，cΣN

求1000以内的勾股数。
"""
import math

for a in xrange(2,100):
    for b in xrange(a+1,100):
        c=math.sqrt( a*a+b*b)# 对数学模块math的方法的查询
        if c>100:
            break# 确定c的范围，跳出b的循环
        
        if c.is_integer():
            print a,b,int(c)
            
