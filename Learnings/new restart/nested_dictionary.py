#program for accessing data from a nested dictionary
Employees={"john":{"age":25,"sallary":56000},"taniya":{"age":18,"sallary":250000}}
for i in Employees:
    print("Employee",i,"::")
    print('Age:',str(Employees[i]['age']))
    print('sallary:',str(Employees[i]['sallary']))
    print("-"*35)
print("-"*35)
