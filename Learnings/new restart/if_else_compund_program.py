num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
print("the list of operator are asa follows:")
print("if you press 1----(+)")
print("if you press 2----(-)")
print("if you press 3----(*)")
print("if you press 4----(/)")
print("if you press 5----(%)")
op=input("Enter your OPERATOR choice[+-*/%]:")
result=0
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
elif op=='%':
    result=num1%num2
else:
    print("INVALID OPERATOR")
print(num1,op,num2,"=",result)
