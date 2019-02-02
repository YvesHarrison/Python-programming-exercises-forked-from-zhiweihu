class shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class square(shape):
    def __init__(self,l):
        shape.__init__(self)
        self.length=l

    def cal(self):
        return self.length**2

def Question53():
    a=square(3)
    print(a.cal())
    
Question53()