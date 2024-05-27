def maxx(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is the gretest number")
    elif b>a:
        if b>c:
            print(f"{b} is the gretest number")
    else:
        print(f"{c} is the gretest number")

p=int(input("Enter the first number:"))
q=int(input("Enter the second number:"))
r=int(input("Enter the third number:"))

maxx(p,q,r)
