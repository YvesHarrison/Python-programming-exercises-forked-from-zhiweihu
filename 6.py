import math
def Question6():
    C=50
    H=30
    number=str(input("Input number "))
    number=number.split(",")
    for i in range(0,len(number)):
        number[i]=int(number[i])
        number[i]=str(int(round(math.sqrt(2*C*number[i]/H))))
    print (','.join(number))
    #print(number)

Question6()