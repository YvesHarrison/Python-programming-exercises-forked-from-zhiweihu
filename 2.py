def Question2(n):
    if(n<0):
        return None
    if(n==0):
        return 1
    res=1
    for i in range(1,n+1):
        res*=i
    return res

print(Question2(10))