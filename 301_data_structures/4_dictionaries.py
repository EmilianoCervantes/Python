# Dictionaries
# In Python 3, currently only one standard mapping type

dictionary = {'jack': 4098, 'jm': 4139}
dictionary['guido'] = 4127
print(f"Dictionary: {dictionary}")
print(f"Jack: {dictionary['jack']}\n")

del dictionary['jm'] # Similar to lists
dictionary['irv'] = 4127 # Add a new value
print(f"Dictionary minus jm plus irv: {dictionary}\n")

dict_as_list = list(dictionary)
print(f"Dictionary as list: {dict_as_list}")
sorted_dict = sorted(dictionary)
print(f"Sorted dictionary: {sorted_dict}\n")

print(f"'guido' in dictionary: {'guido' in dictionary}")
print(f"'jack' not in dictionary: {'jack' not in dictionary}\n")

# ALTERNATIVE: Initializing a dictionary
dict(jack=4098, jm=4139, guido=4127)

## Dictionary Comprehension
# Similar to lists, we can create dictionaries like this:
# {key_expression: value_expression for item in iterable if condition}
dictionary_comprehension = {key: key**2 for key in (2, 4, 6)}
print(f"Dictionary comprehension: {dictionary_comprehension}")
