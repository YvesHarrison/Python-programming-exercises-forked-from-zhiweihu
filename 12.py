def check(num):
    while(num>=1):
        if num%2==0:
            num=int(num/10)
        else:
            return False
    return True

def Question12():
    res=[]
    for i in range(1000,3001):
        if check(i):
            res.append(str(i))
    print(",".join(res))
    
Question12()