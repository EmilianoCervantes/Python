# Besides the lists, Tuples are the other sequence data type in Python
my_tuple = 12345, 54321, 'hello!'
print(f"My first tuple: {my_tuple}")
print(f"1st item: {my_tuple[0]}\n")

# Tuples may be nested:
nested_tuples = my_tuple, (1, 2, 3, 4, 5)
print(f"Nested tuple: {nested_tuples}\n")

# Tuples are immutable:
# my_tuple[0] = 88888 # Error
# TypeError: 'tuple' object does not support item assignment


# but they can contain mutable objects:
mutable_tuple = ([1, 2, 3], [3, 2, 1])
print(f"Mutable tuple before: {mutable_tuple}")
mutable_tuple[0][0] = [100]
print(f"Mutable tuple after: {mutable_tuple} - what's mutable is the list to be precise.\n")

# Singleton
empty_tuple = ()
singleton = 'hello', # <-- note trailing comma
singleton_without_comma = 'hello'
print(f"Length empty tuple: {len(empty_tuple)}")
print(f"Length singleton: {len(singleton)}")
print(f"Singleton tuple: {singleton}")
print(f"Type of my first tuple: {type(my_tuple)}")
print(f"Type empty: {type(empty_tuple)}")
print(f"Type singleton: {type(singleton)}")
print(f"Type singleton without comma: {type(singleton_without_comma)}")
