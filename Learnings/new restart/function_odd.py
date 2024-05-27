def odd(lower,upper):
    print("Odd numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        if num%2 != 0:
            print(num,end=" ")
odd(1,100)
