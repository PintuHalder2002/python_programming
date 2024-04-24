#Reverse the digits in th bgiven number....

num=int(input())
absnum=abs(num)

rev=absnum%10
absnum=absnum//10

while(absnum>0):
    r=absnum%10
    absnum=absnum//10
    rev=rev*10+r
    
if(num>0):
    print(rev)
else:
    print(rev-2*rev)    