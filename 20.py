def Question20(n):
    for i in range(0,n+1):
        if i%7==0:
            yield i
    
for n in Question20(100):
    print(n)
