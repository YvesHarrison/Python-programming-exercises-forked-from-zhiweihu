def Question64():
    n=int(input())
    if n==0: 
        print(0)
    elif n==1:
        print(1)
    else:
        f0=0
        f1=1
        for i in range(2,n+1):
            f2=f1+f0
            f0=f1
            f1=f2
        print(f2)

Question64()