n=int(input())
output=""
for x in range(1,n):
    str_x=str(x)
    for y in range(x,n):
        str_y=str(y)
        for z in range(y,n):
            str_z=str(z)
            if(x**2+y**2==z**2):
                output=str_x+","+str_y+","+str_z
                print(output)
            else:
                pass
    if(output==""):
        print("NO SOLUTION")
        