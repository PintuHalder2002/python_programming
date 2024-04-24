def list_mini(l):
    mini=l[0]
    for i in range(len(l)):
        if l[i]<mini :
            mini=l[i]
    return mini

def obvious_sort_1(l):
    x=[]
    while(len(l)>0):
        mini=list_mini(l)
        x.append(mini)
        l.remove(mini)
    return x


def obvious_sort(l):
    x=[]
    while(len(l)>0):
        mini=l[0]
        for i in range(len(l)):
            if(l[i]<mini):
                mini=l[i]
        x.append(mini)
        l.remove(mini)
    return x


l=[90,23,97,88,5,1]

#print(obvious_sort(l))
print(obvious_sort_1(l))
