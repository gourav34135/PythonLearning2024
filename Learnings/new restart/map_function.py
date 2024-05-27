list1 = [4, 6, 1, 55, 22, 33]

def square(n):
    return n**2
result = map(square, list1)
print(list(result))

result2= list(map(lambda x: x**2, list1))
print(result2)