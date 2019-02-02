def Question1():
    res=""
    for i in range(2000,3201):
        if(i%7==0 and i%5!=0):
            res+=str(i)
            res+=","
    res=res[0:len(res)-1]
    print(res)

Question1()