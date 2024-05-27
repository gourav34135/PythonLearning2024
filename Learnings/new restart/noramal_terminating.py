count=sum=0
ans='y'
while ans=='y':
    num=int(input("ENter your number:"))
    if num<0:
        print("number is below zero .aborting!.")
        break
    sum=sum+num
    count=count+1
    ans=input("Want to enter more numbers?(y/n)..")
else:
    print("you entered ",count,"so faar")
print("Sum of all the numbewrs you enterd is ",sum)
