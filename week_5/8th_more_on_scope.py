def myfunction1():
    global x
    x=x*2
    print("value of x in the function 1", x)

def myfunction2():
    global x
    x=x*3
    print("value of x in the function 2", x)

x=5
print("value of x before function call", x)

myfunction1()
myfunction2()

print("value of x after function call", x)
