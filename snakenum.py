#encoding:utf8
"""打印回型矩阵如图：
1      2     3     4     5     6     7      8
28     29    30    31    32    33    34     9
27     48    49    50    51    52    35    10  
26     47    60    61    62    53    36    11
25     46    59    64    63    54    37    12
24     45    58    57    56    55    38    13
23     44    43    42    41    40    39    14
22     21    20    19    18    17    16    15"""

"""
(p,p)    (p,i)      (p,q)


(i,p)               (i,q)


(q,p)    (q,i)      (q,q)

"""


def snakenum(n):
    matrix = [[n * n] * n for i in range(n)]  #初始化全为n*n的二维数组
    p = 0
    q = n - 1  # 坐标p,q
    t = 1  # 临时变量t
#四个边交叉，每一个while循环打印一圈。
#直到p，q相等结束
    while (p < q):
        for i in range(p, q):
            matrix[p][i] = t
            t += 1
        for i in range(p, q):
            matrix[i][q] = t
            t += 1
        for i in range(q, p, -1):
            matrix[q][i] = t
            t += 1
        for i in range(q, p, -1):
            matrix[i][p] = t
            t += 1
        p += 1
        q -= 1

    return matrix

"""打印二维数组"""
for x in snakenum(6):
    print x
