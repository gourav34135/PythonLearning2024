# program to do matematical operation on any two numbers
ram=int(input("Enter the frist number :"))
sam=int(input("Enter the second number :"))
see=input("Enter the operation(A,D,S,M):")

if see=='A':
    print(ram+sam)
elif see=='D':
    print(ram/sam)
elif see=='S':
    print(ram-sam)
elif see=='M':
    print(ram*sam)
else:
    print("Invalid operation")
