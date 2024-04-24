#IF CONDITION.
#lET US CONSIDER THE MOVIE "AVENGERS".Thisa is a 13+ movie.

birth_year=int(input("please enter your date of birth:"))

print(birth_year)


current_year=2024

age=current_year-birth_year

if(age>13):
    print('''you are under age . you can't watch this movie.
          \nwait until you become old enough to watch 
          this movie''')
else:
    print('''You are old enough to watch Avengers, enjoy!
          \n don't forget to watch the sequels and prequels.''')
    
print("Have a nice time.")

