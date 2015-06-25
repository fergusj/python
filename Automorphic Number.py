# encoding:utf8
#如果某个数的平方的末尾几位等于这个数，那么就称这个数为自守数。
#显然，5和6是一位自守数（5*5=25，6*6=36)。 25*25=625,76*76=5776，所以25和76是两位自守数。

#求10000以内的自守数。

#def isA(n):
    
    #t = n * n
    #for temp in range(len(str(t))):
        #if t % 10 ** temp == n:
            #return n
        
#for x in range(100000):
    #print isA(x)
    
    
for n in range(1, 10000):
    l = len(str(n))
    t = n * n % (10 ** l)
    if t == n:
        print n
        
#[n * n % (10 ** len(str(n))) for n in range(1, 10000)]
print [n for n in range(1, 10000) if n * n % (10 ** len(str(n))) == n]