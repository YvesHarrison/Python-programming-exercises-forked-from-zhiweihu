class Person():
    def getGender(self):
        return " "

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

def Question91():
    M1=Male()
    print(M1.getGender())
    F1=Female()
    print(F1.getGender())

Question91()