# encoding:utf8
# 0~9这10个数字可以组成多少不重复的3位数？

count = 0
l = range(9)

for a in l[1:]:   
    for b in l:
        if a == b: continue
        for c in l:
            if c != a and c != b:
                print a, b, c
                count += 1  
print count