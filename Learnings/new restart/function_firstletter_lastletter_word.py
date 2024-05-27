# Program to create dictionary output from the given string
# first character of sting and last character of string will form a new word

def bob(string):
    a={}
    listo=string.split(" ")
    for i in listo:
        a[i[0]+i[-1]]=i
    return a
print(bob("we can call TR as systu"))
