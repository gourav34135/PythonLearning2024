# program to find the factorial of the number given by the user using function

def fact(k):
    ans=1
    while k>0:
        ans*=k
        k-=1
    print(f"The factorial of {k} is :{ans}")

num=int(input("Enter the number whose factorial you wanna find :"))

fact(num)
