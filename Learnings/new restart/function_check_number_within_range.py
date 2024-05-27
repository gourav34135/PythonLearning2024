def ranger(a):
    if a in range(n,m):
        print("Yes the given number is in range")
    else:
        print("The entered number is out of the range")
num=int(input("Enter the number you wanna check:"))
n=int(input("Enter the uppper limit within you wanna check:"))
m=int(input("Enter the lower limit within you wanna check:"))
ranger(num)
