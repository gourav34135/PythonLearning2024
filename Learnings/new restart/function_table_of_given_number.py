def table(num):
    a=0
    for i in range(1,11):
        a=i*num
        print(num,"*",i,"=",a)
n=int(input("Enter a number:"))
table(n)
