#factorial problem(using_for_loop)
'''num=int(input("Enter a number : "))
fact=1

if(num<0):
    print("Not defined")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)'''
    
#no.of digits problem(using_for_loop_)

'''num=abs(int(input("Enter a number : ")))

strNum=str(num)
digits=0
for c in strNum:
    digits=digits+1
print(digits)'''


#Reverse the digits(using_for_loop)_problem

'''num=int(input("Enter a number : "))

absStrNum=str(abs(num))

rev=""

for c in absStrNum:
    rev = c + rev
    
if(num >=0):
    print(rev)
else:
    print("-" + rev)'''
    
#Palindrome_problem(using_for_loop_)

num=int(input("Enter a number : "))
absStrNum=str(abs(num))
rev=""

for c in absStrNum:
    rev = c + rev
    
if(num >=0):
    print(rev)
else:
    print("-" + rev)

if(num<0):
    rev="-"+rev 
    
    
if(num == int(rev)):
    print("Palindrome")
else:
    print("Not a palindrome")

























