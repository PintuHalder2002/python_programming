def myfunction(x):
    x=x*2
    print("the value of x in the function", x)#execution_2

x=5  #here x is a global variable which is accesible anywhere in code.
print("value of x before fuction call", x)#execution _1

myfunction(x)
print("value of x after function call", x)#here x is taking globally.