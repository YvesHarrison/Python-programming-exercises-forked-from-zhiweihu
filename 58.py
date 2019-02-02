def Question58():
    email=input()
    a=email.find("@")
    b=email.find(".")
    print(email[:a])
    print(email[a+1:b])
    
Question58()