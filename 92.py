def Question92():
    dic=dict()
    s=input()
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]]=0
        dic[s[i]]+=1
    for key in dic.keys():
        print(key,dic[key])

Question92()