
def fib():
    a=0
    b=1
    count=0
    while count<k:
        print(a,",",end='')
        n=a+b
        a=b
        b=n
        count+=1

k=int(input("Enter the limit till where you wanna print the series:"))

fib()
        
