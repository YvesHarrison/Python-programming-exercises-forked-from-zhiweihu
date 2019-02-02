def Question42():
    tu=(1,2,3,4,5,6,7,8,9,10,11)
    li=list()
    for item in tu:
        if item%2==0:
            li.append(item)
    tu1=tuple(li)
    print(tu1)

Question42()