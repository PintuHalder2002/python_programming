s=" "*2
print("o"+s+"o")
def survival(T):
   flag=True
   for x in range(0,6):
       for y in range(0,6):
           temperature=30+(x**2)+(y**2)-(3*x)-(4*y)
           if(temperature<=T):
               flag=True
           else:
                flag=False
                break
           break
       break
   
   if(flag):
        return True
   else:
        return False

T=30    
print(survival(T))
    