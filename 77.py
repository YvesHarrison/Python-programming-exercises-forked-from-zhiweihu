import random
def Question77():
    print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))
    
Question77()