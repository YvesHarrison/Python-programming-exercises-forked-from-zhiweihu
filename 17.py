def Question17():
    account=0
    while True:
        s=input().split(" ")
        if s[0]=="D":
            account+=int(s[1])
        elif s[0]=="W":
            account-=int(s[1])
        else:
            break
    print(account)
    
Question17()
