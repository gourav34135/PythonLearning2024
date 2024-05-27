#program to find the elment in the list taken from the user
lst=eval(input("Enter the list:"))
element=input("enter the element you wanna find in the list:")
length=len(lst)
for i in range(0,length):
    if element==lst[i]:
        print("elment found in list on index",i)
        break
else:
    print("elemnt not found in the list")
