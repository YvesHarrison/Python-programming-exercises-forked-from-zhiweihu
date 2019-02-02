def square(num):
    return num**2

def even(num):
    return num%2==0

def Question46():
    tu=[1,2,3,4,5,6,7,8,9,10]
    tu=list(map(square,tu))
    tu=filter(even,tu)
    print(list(tu))
    
Question46()