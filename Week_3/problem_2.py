#find the number of digits in the given number:
    
num=abs(int(input("Enter a number : ")))

digits=1#it ciover4s aqll the digits from-9 rtoi +9.
while(num>9):
    num=num//10
    digits+=1
    
print(digits)




