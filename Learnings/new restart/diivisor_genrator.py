a=float
num=int(input("enter any number whose divisor you wanna find:"))
mid=num/2
print("The divisor of",num,"are:")
for a in range(2,mid+1):
    if num%a==0:
        print(a,end='')
    else:
        print("-END")
