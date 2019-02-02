class inputstring(object):
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string=str(raw_input())
    def printString(self):
        print(self.string.upper())

def Question5():
	Object=inputstring()
	Object.getString()
	Object.printString()

Question5()