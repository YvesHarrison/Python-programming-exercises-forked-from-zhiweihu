import math
class Circle:
    def __init__(self,r):
        self.r=r

    def cal(self):
        return self.r**2*math.pi

def Question51():
    a=Circle(3)
    print(a.cal())
    
Question51()