lst=eval(input("Enter the list :"))
length=len(lst)
element=int(input("Enter the element you wanna search:"))
count=0
for i in range(0,length):
    if element==lst[i]:
        count+=1
if count==0:
    print("The element is not in the list")
else:
    print(element,"has a frequency as",count,"in the given list")
