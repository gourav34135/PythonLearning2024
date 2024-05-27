def prime(a):
    count=0
    for i in range(2,a):
        if a%i==0:
            count+=1
    if count>0:
        print("Entered number is not a prime number")
    else:
        print("Entered number is a prime number")

num=int(input("Enter a number you wanna check:"))
prime(num)
