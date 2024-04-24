#find the factiorial of given number

num=int(input())

fact=1

while(num>0):
    fact=fact*num
    num=num-1
    
print(fact)