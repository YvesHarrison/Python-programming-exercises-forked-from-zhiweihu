def is_even(num):
    return num%2==0

def Question44():
    li=[1,2,3,4,5,6,7,8,9,10]
    li=filter(is_even,li)
    print(list(li))
    
Question44()