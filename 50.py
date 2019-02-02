class American:
    def printNationality(self):
        print("American")

class NewYorker(American):
    pass

def Question50():
    a=American()
    b=NewYorker()
    a.printNationality()
    b.printNationality()
    
Question50()