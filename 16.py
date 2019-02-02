def Question16():
    res=[]
    numbers=input().split(",")
    for i in range(0,len(numbers)):
        if int(numbers[i])%2!=0:
            res.append(numbers[i])
    print(",".join(res))
    
Question16()
