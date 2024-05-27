#program to create a dicrtionary fromthe names ofcompitition winners as keys and the numbeer of wines they got as values
n=int(input("Enter the number of students:"))
compwinners={}
for i in range(n):
    key=input("Entere the name of student:")
    value=int(input("Enter the number of compitition won:"))
    compwinners[key]=value
print("The Dictionary formed is:")
print("-"*50)
print(compwinners)
