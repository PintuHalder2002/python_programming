
#code vetrified , works completely fine on the test cases.
c=[]
C=[]

def initialize_mat(dim):
    for i in range(dim):
        c.append(0)
    for j in range(dim):
        C.append(c)
    return C

u=[1,2,3]
v=[5,6,7]
def dot_product(u,v):
    dim=len(u)
    ans=0
    for i in range(dim):
        ans=ans+(u[i]*v[i])
    return ans


M=[[1,2,3],[4,5,6],[7,8,9]]

def row(M,i):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[i][k])
    return l

def column(M,i):
    dim=len(M)
    m=[]
    for k in range(dim):
        m.append(M[k][i])
    return m

A=[1,2,3]
B=[4,5,6]

def mat_mul(A,B):
    dim=len(A)
    C=initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j]=dot_product(row(A,i),row(B,j))
    return C
print(mat_mul(A,B))



