num = a =int(input("enetrer a number:"))
rev = 0
while a>0:
    rem = a%10
    rev = rev +rem**3
    a= a//10

if rev == num:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")
