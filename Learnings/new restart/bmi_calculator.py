name=str(input("Enter your name:"))
weight=float(input("Enter your weight (in kgs):"))
height=float(input("Enter your height (in mtr):"))
bmi=weight/height**2
print("*"*30)
print("\tRESULT")
print("*"*30)
print(name,"your BMI  is:",bmi)
if bmi<18.5:
    print(name,"you are underweight.. needs to morefocus on diet")
elif bmi<25:
    print(name,"you are falling in NORMAL category)")
else:
    print(name,"you are obbess , need to cut off your diet and try to avoid junk food")
    
