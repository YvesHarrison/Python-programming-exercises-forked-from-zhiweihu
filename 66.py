def Question66():
    n=int(input())
    li=[]
    for i in range(0,n+1):
        if i%2==0:
            li.append(str(i))
    print((",").join(li))
    
Question66()