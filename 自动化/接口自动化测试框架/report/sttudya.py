a=[1,2,3,1,2,3,4]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
