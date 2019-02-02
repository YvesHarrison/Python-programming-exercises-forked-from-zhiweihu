import math
def Question21():
    x=0
    y=0
    while True:
    	com=input()
    	if not com:
    		break
    	com=com.split(" ")
    	if com[0]=="UP":
    		y+=int(com[1])
    	elif com[0]=="DOWN":
    		y-=int(com[1])
    	elif com[0]=="LEFT":
    		x-=int(com[1])
    	elif com[0]=="RIGHT":
    		x+=int(com[1])
    print(int(round(math.sqrt(x*x+y*y))))

Question21()
    

