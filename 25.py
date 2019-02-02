class A:
	name="a"
	def __init__(self,name=None):
		self.name=name

def Question25():
	a=A()
	a.name="hhh"
	print(a.name,A.name)
	b=A("bbb")
	print(b.name,A.name)

Question25()