num1 =int(input("enter the first number:"))
num2 =int(input("enter the second number number"))
a = num1
b = num2
while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("HCF or GCD of", a, "and", b, "is", num1)
