from operator import itemgetter
def Question19():
    res=[]
    while True:
        s=input()
        if not s:
            break
        res.append(tuple(s.split(",")))
    res.sort(key=itemgetter(0,1,2))
    print (res)
    
Question19()
