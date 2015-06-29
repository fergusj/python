'''def isPalidromNum(n):
    a=[]
    while n>0:
        a.append(n%10)
        n/=10
    for i in range(len(a)):
        if a[i]!=a[-i-1]:
            return False
    return True
        
    
    
print isPalidromNum(987789)'''


def isP(n):
    s=str(n)    
    for i in range(len(s)):
        if s[i]!=s[-i-1]:
            return False
        
    return True

print isP(9837789)