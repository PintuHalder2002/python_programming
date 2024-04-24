'''z={"amit","neeru","anamika","varsha","nitin"}
print("nitin" in z)
print("pintu" in z)

z.add("pintu")
print(z)

#To find any element is present there or not 
#we must use set .
import sys

print(sys.getsizeof(z))

y=["amit","neeru","anamika","varsha","nitin"]

print(sys.getsizeof(y))

#z[2] will throw an error
#hence we must use list  to define a particular element.
#there is no first element ,no
#second element and so on....

my_set={2,3,3,3,3,4,2,6,2,4,780,5,6,7,7,}

print(my_set)

my_set.add(100)

print(my_set)

print(len(my_set))

my_set.pop()

print(my_set)

my_set.pop()

print(my_set)

my_set.clear()
print(my_set)

l=input()
m=list(l)
def is_sorted(l):
    x=[]
    while(len(l)>0):
        mini=l[0]
        for i in range(len(l)):
            if (l[i]<mini):
                mini=l[i]
        x.append(mini)
    if(x==m):
        return True
    else:
        return False
print(is_sorted(l))'''

l=[7,8,9,6]
l[0]=8
print(l)

L=[9,8,9,5,7]

def first_three(L):
    L.sort()
    fmax=L[-1]
    smax=L[-2]
    tmax=L[-3]
    return fmax,smax,tmax
print(first_three(L))
    