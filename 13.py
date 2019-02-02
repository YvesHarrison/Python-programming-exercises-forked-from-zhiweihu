def Question13():
    sen=input()
    digit=0
    letter=0
    for i in range(0,len(sen)):
        se=sen[i].upper()
        if se>="0" and se<="9":
            digit+=1
        if se>="A" and se<="Z":
            letter+=1
    print("LETTER",letter)
    print("DIGITS",digit)
    
Question13()
