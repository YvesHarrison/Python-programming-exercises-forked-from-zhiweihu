def check(n):
    for i in range(0,n+1):
        if(i%5==0 and i%7==0):
            yield i

def Question67():
    n=int(input())
    li=[]
    for i in check(n):
        li.append(str(i))
    print((",".join(li)))
    
Question67()