#Let us find the factorial of a number

print("Enter a number : ")
n=int(input())
answer=1
i=1

while(i<=n):
    answer=answer*i  
    i=i+1
    
print(answer)