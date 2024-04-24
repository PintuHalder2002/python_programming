def list_min(l):
    mini=l[0]
    for i in range(len(l)):
        if(l[i]<mini):
            mini=l[i]
    return mini

def list_maxi(l):
    maxi=l[0]
    for i in range(len(l)):
        if(l[i]>maxi):
            maxi=l[i]
    return maxi

def list_appendbefore(l,z):
    newl=[]
    for i in range(len(z)):
        newl.append(z[i])
    for j in range(len(l)):
        newl.append(l[j])
    return newl

def list_appendend(l,z):
    newl=[]
    for i in range(len(l)):
        newl.append(l[i])
    for j in range(len(z)):
        newl.append(z[j])
    return newl

l=[9,7,654,67,0,-2,4,8]
print(list_min(l))
print(list_maxi(l))

z=[20,40,60]
print(list_appendbefore(l,z))

print(list_appendend(l,z))

def list_average(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    ans=sum/len(l)
    return ans

l=[2,8,9,11] 

print(list_average(l))






