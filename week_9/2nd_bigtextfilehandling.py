f=open('pintu.txt','r')
s=f.readline()
while(s!=''):
    s=f.readline()
    n=int(s)
    if(n==786):
        print("The number was found ")
        break



