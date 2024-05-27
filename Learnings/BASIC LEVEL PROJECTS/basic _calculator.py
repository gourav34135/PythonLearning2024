#python program to make a basic calcualtor which can perform all the basic mathematical calculations

import math

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "cannot divide by zero"
    else:
        return x/y
def square_root(x):
    return math.sqrt(x)
def square(x):
    return x**2
def cube(x):
    return x**3
def simple_interest(principle,rate,time):
    return (principle*rate* time)/100
def compound_interest(principle,rate,time):
    return principle*(pow((1+rate/100),time))
def calculator():
    print("Welcome To The Basic Calculator")
    print("="*35)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Square")
    print("7. Cube")
    print("8. Simple Interest")
    print("9. Compound Interest")
    print("0. Exit")
    print("="*35)


    while True:
        choice=input("Enter your choice(0-9): ")

        if choice=='0':
            print("Thnak you very much for using basic calculator ")
            print("="*35)
            break
        elif choice in('1','2','3','4'):
            num1=float(input("Enter the value of x:"))
            num2=float(input("Enter the value of y:"))
            if choice =='1':
                print("Result:",add(num1,num2))
                print("="*35)
            elif choice=='2':
                print("Result:",subtract(num1,num2))
                print("="*35)
            elif choice=='3':
                print("Result:",multiply(num1,num2))
                print("="*35)
            elif choice=='4':
                print("Result:",divide(num1,num2))
                print("="*35)

        elif choice in('5','6','7'):
            num=float(input("Enter the number:"))
            if choice=='5':
                print("Result:",square_root(num))
                print("="*35)
            elif choice=='6':
                print("Result:",square(num))
                print("="*35)
            elif choice=='7':
                print("Result",cube(num))
                print("="*35)
        elif choice in('8','9'):
            principle=float(input("Enter the principle amount: "))
            time=float(input("Enter the time (in years): "))
            rate=float(input("Enter the rate of interest: "))

            if choice=='8':
                print("Result:",simple_interest(principle,rate,time))
                print("="*35)
            elif choice=='9':
                print("Result:",compound_interest(principle,rate,time))
                print("="*35)

        else:
            print("Invalid choice: Please enter a valid choice")


if __name__=="__main__":
    calculator()
