def Question14():
    sen=input()
    upper=0
    lower=0
    for i in range(0,len(sen)):
        if sen[i]>="a" and sen[i]<="z":
            lower+=1
        if sen[i]>="A" and sen[i]<="Z":
            upper+=1
    print("UPPER CASE",upper)
    print("LOWER CASE",lower)
    
Question14()
