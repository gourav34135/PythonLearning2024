a=int(input("enter a number:"))
b=int(input("enter the second number:"))
c=(a+b)
print("the sum of a and b is:",c)

# Read the input
n = int(input())
elements = set(map(int, input().split()))
m = int(input())

# Execute each command
for _ in range(m):
    command = input().split()
    if command[0] == 'pop':
        elements.pop()
    elif command[0] == 'remove':
        try:
            elements.remove(int(command[1]))
        except KeyError:
            pass  # if the element is not present, we just pass
    elif command[0] == 'discard':
        elements.discard(int(command[1]))

# Print the sum of elements in the set
print(sum(elements))
