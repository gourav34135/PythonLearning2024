def multiple(lst):
    total=1
    for i in lst:
        total*=i
    print("The multiplication of all the elements in the above list is:",total)
list=[int(item) for item in input("Enter the list items(seperated with space) : ").split()]
multiple(list)

