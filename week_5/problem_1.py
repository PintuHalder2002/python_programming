'''write a python code  using functions which calculates 
the number of upper case letters, lower case letters,total
number of characters and number of words.'''

def upper_count(s):
    uppercase=0
    for c in s:
        if c.isupper():
            uppercase+=1
    return uppercase


def lower_count(s):
    lowercase=0
    for c in s:
        if c.islower():
            lowercase+=1
    return lowercase

def character_count(s):
    char=0
    for c in s:
        char+=1
    return(char)

def word_count(s):
    words=1
    for c in s:
        if c==" " :
            words+=1
    return words


sentence=input()
print("no. of upper case letters : ", upper_count(sentence))

print("no. of lower case letters : ", lower_count(sentence))

print("no. of characters : ", character_count(sentence))

print("no. of words : ", word_count(sentence))




