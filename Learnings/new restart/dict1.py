# Creating a dictionatry
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'occupation': 'Engineer'
}

print("Original Dictionary:")
print(my_dict)

print("\nAccessing values:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])
print("Occupation:", my_dict['occupation'])

print("\nModifying values:")
my_dict['age'] = 26
my_dict['city'] = 'San Francisco'
print("Updated Dictionary:", my_dict)

print("\nAdding a new key-value pair:")
my_dict['gender'] = 'Male'
print("Updated Dictionary with Gender:", my_dict)


print("\nRemoving a key-value pair:")
removed_value = my_dict.pop('occupation')
print("Updated Dictionary after removing 'occupation':", my_dict)
print("Removed Value:", removed_value)

print("\nChecking if a key exists:")
if 'age' in my_dict:
    print("Key 'age' exists in the dictionary.")
else:
    print("Key 'age' does not exist
