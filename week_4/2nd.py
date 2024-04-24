'''import random

l=[]
for i in range(10):
    l.append(random.random())
    l.append(random.randint(1,10))
print(l)'''

import random

l=[]
#create an empty list

for i in range(30):
    l.append(random.randint(1,365))
    #append random numbers between 1 and 365.
    #append 30 of them.
l.sort()
print(l)

i=0
flag=False
while(i<=len(l)-2):
    if(l[i]==l[i+1]):
        print("Repeats",l[i],l[i+1])
        flag=True
        break
    i=i+1
if(flag==False):
    print("There is no repetition")
#as you increase the range you will see it repeats almost everytime.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        