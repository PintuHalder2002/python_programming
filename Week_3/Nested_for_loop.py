'''s="spyder"
t="frdty"
count=0

for i in range(6):
    for j in range(5):
        print(i,j,s[i],t[j])
        count+=1
print(count) ''' 

''' # problem_1:  find all prime numbers less than the entered number.....
num=int(input("Enter a Number : "))
if(num>2):
    print(2,end=" ")
for i in range(3,num):
    flag=False
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
        else:
            flag=True
    if(flag):
        print(i,end=" ")'''


#problem 2:find the total profit/loss of each trader working in a trading firm.
#Information regarding number of traders and njumber of transactions is unknown.
    
'''empID=input("Enter emplloyee ID : ")
while(empID!=-1):
    trade=int(input("Enter the trade amount : "))
    profit_loss=0
    while(trade!=0):
        profit_loss=profit_loss+trade
        trade=int(input("Enter the trade amount : "))
    print(f'Profit/loss for employee{empID} is {profit_loss}')
    empID=input("Enter emplloyee ID : ") '''
    
#problem 3:  find the day wise gtotal rainfall for the entered duration of time
# e.g. week , month ,etc.
'''
days=int(input("Enter the number of days : "))
for i in range(1,days+1):
    total=0
    rainfall=int(input("Enter the rainfall : "))
    while (rainfall!=-1):
        total=total+rainfall
        rainfall=int(input("Enter the rainfall : "))
    print('Total rain fall for the day{0} is {1}'.format(i,total))'''
    
#problem 4; find the length of longest word from the set of ewords from the set
# of words entered by the user.....    

'''word=input("Enter a word: ")
maxLen=0
while(word!="-1"):
    count=0
    for letter in word:
        count=count+1
    if(count > maxLen):
        maxLen=count
    word=input("Enter a word : ")
print("The length of longest word is",maxLen)'''


l="jbbdcbjk"
n="kjbdcwbdb"
for letter in n:
    for letter in l:
        if(l==n):
            break
        else:
            print(n) 
        
        
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     

                                                                                                                          