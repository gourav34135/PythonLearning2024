# program to print the list of all the prime numbers between given range

def prime(n,m):
    for i in range(n,m+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count ==2:
            print(j,",",end='')

n=int(input("Enter the upper limit:"))
m=int(input("Enter the lower limit:"))

prime(n,m)
        
