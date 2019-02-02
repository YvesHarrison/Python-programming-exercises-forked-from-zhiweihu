class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def cal(self):
        return self.length*self.width

def Question52():
    a=Rectangle(3,5)
    print(a.cal())
    
Question52()