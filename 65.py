def Question65():
    n=int(input())
    li=[]
    if n==0: 
        li.append(0)
    elif n==1:
        li.append(0)
        li.append(1)
    else:
        li.append(0)
        li.append(1)
        for i in range(2,n+1):
            li.append(li[i-1]+li[i-2])
    for i in range(0,n+1):
        li[i]=str(li[i])      
    print((",").join(li))
    
Question65()