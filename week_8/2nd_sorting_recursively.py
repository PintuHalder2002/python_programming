def mini(L):#finds the minimum  element in the list.
    mini=L[0]
    for i in range(len(L)):
        if (L[i]<mini):
            mini=L[i]
    return mini
def sorted(L):
    #recursively sort the list L
    if L==[] or len(L)==1 :
        return L
    #if the list is empty then it is already sorted.

    m=mini(L)# m now contains the minimum most element in L.
    L.remove(m)
    # We remove that element from L.
    return [m]+sorted(L)
    # We recursively sort the smaller list.
L=[3,2,2,4,4,4,2,3,2,1,1,3,5,5,6]
print(sorted(L))




            