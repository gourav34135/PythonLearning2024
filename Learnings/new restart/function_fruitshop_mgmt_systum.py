# python function program to create a fruitshop management systum

def fruit():
    print("-"*40)
    print("\t\tINVOCE")
    print("-"*40)
    print("Fruit Name:",fname)
    print("Fruit Price:",fprice)
    print("Fruit Quantity In (kgs):",quantity)
    print("Bill:",fprice*quantity)
fname=input("Enter the name of the fruit:")
fprice=int(input("Enter the price of fruit:"))
quantity=float(input("Enter the quantity of fruits(in kgs):"))
fruit()
