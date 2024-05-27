def hcf(s,g):
    if s>g:
        smaller=g
    else:
        smaller=s
    for i in range(1,smaller+1):
        if((s % i == 0) and (g % i == 0)):
            hcf=i
    print(f"H.C.F of {s} and {g}:{hcf}")

gora=int(input("Enter the first number:"))
mora=int(input("Enter the second number:"))
hcf(gora,mora)
