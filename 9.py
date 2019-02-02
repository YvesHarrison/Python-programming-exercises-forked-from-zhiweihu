def Question9():
    lines=[]
    while True:
        sen=input()
        if sen:
            lines.append(sen.upper())
        else:
            break
    for item in lines:
        print(item)

Question9()