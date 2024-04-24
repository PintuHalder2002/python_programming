b1=True
b2=False
print('b1 is of type',type(b1))
print('b2 is of type',type(b2))

##TYPECASTING(conversion from one data type to another datatype)...
a=int(5.7)
print(a,type(a))

b=int('10')
print(b,type(b))

c=str(.9)
print(c,type(c))

a=10
print(bool(a))

print(bool(0))
print(bool(0.0))##for 0 and 0.0 the boolean representation will be False.

print(bool(-19))##for all positive and negative no.s (even for fractional value) the boolean representation will be True.

a=bool('India')
print(a)

b=bool('0')
print(b)     ##for any non empty string boolean value will be True.

c=bool('')
print(c)    ##for a empty string boolean value will be False.





