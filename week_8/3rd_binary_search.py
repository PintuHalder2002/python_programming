#check if a given element k is present or not.
def obvious_search(L,k):
    for x in L :
        if x==k :
            return True
    return False


L=list(range(100))
print(obvious_search(L,59))
import time
a=time.time();print(obvious_search(L,2));b=time.time();print(b-a)