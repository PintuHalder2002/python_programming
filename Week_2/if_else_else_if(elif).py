#problem_2 page_29
'''num=int(input("Enter a number: "))
if(num%5==0):
    if(num%10==0):
        print("0")
    else:
        print("5")

else:print("other")'''

#problem_3 page_30

marks=int(input("Enter a number:"))

'''if(marks>=0 and marks<100):
    if(marks>90):
        print("A")

    if(marks>=80 and marks<90):
        print("B")

    if(marks>=70 and marks<80):
        print("C")

    if(marks>=60 and marks<70):
        print("D")  

    else:
        print("E")

else:
    print("Invalid input") '''


if(marks>=0 and marks<100):
    if(marks>90):
        print("A")

    elif(marks>=80):
        print("B")

    elif(marks>=70):
        print("C")

    elif(marks>=60):

        print("D")  

    else:
        print("E")

else:
    print("Invalid input")         