def even(lst):
    poppy=[]
    for i in lst:
        if i%2==0:
            poppy.append(i)
    print(poppy)
lulu=[int(item) for item in input("Enter the list items(seperated with space) : ").split()]
even(lulu)
