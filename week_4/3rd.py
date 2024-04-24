import random

l=[]

for i in range(10000):
    l.append(random.randint(1,100000))
l.sort()
print(l)



n=0

while(n>-1):
    n=int(input("\nEnter a number:"))
    print(n)
    
    flag=0
    
    for i in range(len(l)):
        if(n==l[i]):
            print("Hip Hip Hurray,element found")
            flag=1
            break
    if(flag==0):
        print("element not found")



