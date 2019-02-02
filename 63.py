def Question63():
    n=int(input())
    if n==0: 
        print(0)
    else:
        f=0
        for i in range(1,n+1):
            res=f+100
            f=res
        print(res)

Question63()