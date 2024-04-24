import math

print(math.log(10))
print(math.log(10,2))
print(math.sqrt(67))
print(math.factorial(9))
print(math.pow(10,3))

#Let us simul;ate a coin toss.
import random
a=random.random()

if(a<0.5):
    print("Heads")

else:
    print("Tail")

    #Let us simulate a dice (six faced).

    import random
    dice_1=random.randrange(1,7)
    dice_2=random.randrange(1,7)

    total=dice_1+dice_2
    print("Your pair of dice is : ", total)