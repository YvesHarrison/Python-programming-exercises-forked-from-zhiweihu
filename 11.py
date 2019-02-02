def Question11():
    sen=input().split(",")
    res=[]
    for item in sen:
        tmp=int(item,2)
        if tmp%5==0:
            res.append(item)
    print (",".join(res))
    
Question11()