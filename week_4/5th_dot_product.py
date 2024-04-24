import random
#write a piece of code to find the dot_product.
x=[1,7,4,5]
y=[2,4,6,7,5,6]
#dot product = (1*2)+(7*4)+(4*6)+(5*7)
sum=0
for i in range(min(len(x),len(y))):
    sum=sum+x[i]*y[i]
print(sum)






