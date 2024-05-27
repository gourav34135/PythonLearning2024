# program to find the duplicating characters in  a stirng using fuction

def dupli(string):
    lis=[]
    for i in string:
        if string.count(char)>1:
            lis.append(char)
    print(set(lis))

hola=input("Enter the string youy wanna use:")

dupli(hola)
