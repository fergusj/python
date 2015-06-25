#encoding:utf8
#在编程竞赛中，有10个评委为参赛的选手打分，分数为0~100分。
#选手最后得分为：去掉一个最高分和一个最低分后其余8个分数的平均值。

#请编写一个程序实现。

import random
"""def average(n):
        
    scores = [random.randint(0, 100) for x in xrange(n)]
    print scores   
    scores.remove(max(scores))
    scores.remove(min(scores))
    average = sum(scores) / n - 2

    print average
    
average(5)"""

def average2(n):
    
    s = []
    for i in xrange(n):
        s.append(random.randint(0, 100))
    print s
    """对于列表的操作可以用列表解析
    但是不是很让别人理解
    对于自己来说尽量使用
    不要太复杂"""
    
    maxScore = 0
    minScore = 100
    sumScore = 0
    
    for k in s:
        if k > maxScore:
            maxScore = k
        if k < minScore:
            minScore = k
        sumScore += k
"""使用python内置函数
   对内置函数看说明
   列表的基本操作增删改append remove 要熟悉
   对于列表的操作有很多是可以不明显使用for循环的
   max min sum
   字符串==列表==迭代
"""
   
    print sumScore, minScore, maxScore
    
    return float(sumScore - minScore - maxScore) / (n - 2)

print average2(8)