num=int(input("eny=ter an  integer(>1000):"))
tnum=num
reverse=0
while tnum:
    digit=tnum%10
    tnum=tnum//10
    reverse=reverse*10+digit
print("the reverse of",num," is :",reverse)
