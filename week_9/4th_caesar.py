f=open("new.txt",'r')
s=f.read()

import string

def create_ceaser_dictionary(x):
    l=string.ascii_lowercase
    l=list(l)
    d={}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
    return d

print(create_ceaser_dictionary(s))




