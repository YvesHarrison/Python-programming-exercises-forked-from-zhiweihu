def Question22():
    sen=input().split()
    dic=dict()
    for item in sen:
    	if item in dic:
    		dic[item]+=1
    	else:
    		dic[item]=1
    sen=list(dic.keys())
    sen.sort()
    for item in sen:
    	print(item,dic[item])
    
Question22()
