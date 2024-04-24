#s(n)=n+s(n-1)#simple recursive example.
#Find 0 in a list.
# L=[2,4,0,3,2,]
# return True if 0 is present in the list else print False.
# Pseudocode
# check0(L):
# check the first element& outsource the program to the
# rest elements.

def check0(L):
    i=0
    if(len(L)==0):#if the list is empty return False.
        return False
    if L[i]==0 :
        return True#return True and break the progrAm.
    else:
        i=i+1
        return check0(L[i:len(L)])
print(check0([4,4,3,3,5,5,6,66,8,0,9,8,7,6,5,5,5,8]))

    