#Matrix addition by first principles......
dim=int(input("Enter the dimension: "))
C=[]
c=[]
r1=[2,3,7]
r2=[9,8,7]
r3=[1,2,3]
a=[]
a.append(r1)
a.append(r2)
a.append(r3)
b1=[1,3,4]
b2=[3,3,4]
b3=[4,4,8]
b=[]
b.append(b1)
b.append(b2)
b.append(b3)

for i in range(dim):
   c.append(0)


for j in range(dim):
   C.append(c)



                # MATRIX ADDITION
for i in range(dim):
   for j in range(dim):
      C[i][j]=a[i][j]+b[i][j]
print("the matrix addition is : ",C)


                # DOT_PRODUCT
X=[1,2,3,4]
Y=[5,6,7,8]
dot_product=0
for i in range(len(X)):
   dot_product=dot_product+X[i]*Y[i]
print("The dot_product is : ",dot_product)
   
                #Matrix_Multiplication

#c[2][1] is the dot product of the 
#2nd row and the 1st column of b.
for i in range(dim):
   for j in range(dim):
      for k in range(dim):
         C[i][j]=C[i][j]+a[i][k]*b[k][j]
print("the matrix multiplication is : ",C)
#c[i][j]=dot product of a[i][...] and b[...][j].





    