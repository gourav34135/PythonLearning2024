def addd(lst):
    total=0
    for i in lst:
        total+=i
    print("Sum of all number in the list is:",total)
suuu = [int(item) for item in input("Enter the list items(seperated with space) : ").split()]

addd(suuu)
    
    
