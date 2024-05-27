mycode = 'print("GOURAV")'
code = """
# here we will execute the program of fuction of adding two numbers
def add(a,b):
    t=a+b
    print("Toatl:",t)
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
add(num1,num2)
#here now we will execute the print statemnet
print('plays BASKTBALL')
"""
exec(mycode)
exec(code)
