l=[12,10,7,18,6,42,8,35,789,876,456,654]

x=[]

while(len(l)>0):
    
    min=l[0]

    for i in range(len(l)):
        if(l[i]<min):
            min=l[i]
    x.append(min)
    l.remove(min)
print(l)
print(x)
    
