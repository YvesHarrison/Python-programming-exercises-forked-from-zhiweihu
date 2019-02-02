class Error:
    def __init__(self,msg):
        self.e=msg

def Question56():
    error=Error("Something Wrong")
    print(error)
    
Question56()