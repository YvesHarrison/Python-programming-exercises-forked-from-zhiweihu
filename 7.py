def Question7():
    info=input().split(",")
    test = [[i*j for i in range(int(info[1]))] for j in range(int(info[0]))]
    print(test)

Question7()