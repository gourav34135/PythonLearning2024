def lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if ((greater%a==0) and (greater%b==0)):
            lcm=greater
            break
        greater+=1
    print("L.C.M of",a,"and",b,"is:",lcm)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
lcm(a,b)
