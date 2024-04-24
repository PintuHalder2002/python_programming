#sum of first n numbers
def sum(n):
    if n==1 :
        return 1
    else:
        return n+sum(n-1)
    
print(sum(10))    

#compound interest
def comp(p,n):
    if n==1 :
        return p*(1.1)#assumed interest to be 10 %.
    else:
        return 1.1*(comp(p,n-1))
print(comp(5000,10))

#factrial

def fact(n):
    if n==1 :
        return 1
    else:return n*(fact(n-1))
print(fact(8))

L=[1,6,7,8]
x=5
def insert(L, x):
    new_list=[]
    p=[]
    for j in range(len(L)):
        p.append(L[j])
    for i in range(len(p)):
        if(x<p[i]):
            p[i]=x
            k=p.index(x)
            break
        else:
            continue
    for i in range(0,k+1):
        new_list.append(p[i])
    for i in range(k,len(L)):
        new_list.append(L[i])
    return new_list
print(insert(L, x))
    
