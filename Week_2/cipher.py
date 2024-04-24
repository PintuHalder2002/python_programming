#this is popularly called  as ceaser cipher in CRYPTOGRAPHY.

alpha="abcdefghijklmnopqrstuvwxyz"

s="pintu"

#I EXPECT TO PRINT "QJOUV" ; shifting one letter in each of the letter in string "s".

i=0
k=1
t=""

t=t+alpha[(((alpha.index(s[i]))+k)%26)]
t=t+alpha[(((alpha.index(s[i+1]))+k)%26)]
t=t+alpha[(((alpha.index(s[i+2]))+k)%26)]
t=t+alpha[(((alpha.index(s[i+3]))+k)%26)]
t=t+alpha[(((alpha.index(s[i+4]))+k)%26)]

print(t)

