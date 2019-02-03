def Question96(leg,head):
    li=list()
    for i in range(head+1):
        r=head-i
        if r*4+i*2==leg:
            li.append([r,i])
    if len(li)==0:
        return "No Solution"
    else:
        return li

print(Question96(94,35))