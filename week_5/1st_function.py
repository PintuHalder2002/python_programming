def add(a,b):
    ans=a+b
    #print(ans) will throw an error.
    return ans


ans=add(13441,9797)+6464
print(ans)


def discount(cost,d):
    ans=cost-(cost*(d/100))
    return ans

x=int(input("enter the cost price : "))
y=int(input("enter the discount percentage : "))

print("the final discounted price is : ",discount(x,y))