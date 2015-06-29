def aijishu(a,b):
    k=b/a
    if b%a==0:
        res="1/%s"%k
    else:
        k+=1
        res="1/%s+%s"%(k,aijishu(a*k-b, b*k))        
    return res

print aijishu(3, 7)