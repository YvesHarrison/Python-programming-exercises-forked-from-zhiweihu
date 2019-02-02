def check(item):
    if len(item)<6 or len(item)>12:
        return False
    num=0
    upper=0
    lower=0
    tag=0
    for i in range(0,len(item)):
        if item[i]>="0" and item[i]<="9":
            num+=1
        elif item[i].islower():
            lower+=1
        elif item[i].isupper():
            upper+=1
        elif item[i]=="#" or item[i]=="@" or item=="$":
            tag+=1
    if tag>=1 and num>=1 and lower>=1 and upper>=1:
        return True
    else:
        return False

def Question18():
    pas=input().split(",")
    res=[]
    for item in pas:
        if check(item):
            res.append(item)
    print(",".join(res))
    
Question18()
