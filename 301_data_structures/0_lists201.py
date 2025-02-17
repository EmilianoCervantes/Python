# As you know, we can create a list as easy as
my_list = ["a", "b", "c", "d", "e"]

# And call it's methods like this: <list>.<method>()
my_list.append("f")
print(f"Append: {my_list}\n")

##############################
# There are other methods #
##############################

# Extend - ADD multiple elements at the END of the list
my_list.extend("g") # Looks similar to append, right?
print(f"Extend: {my_list}")
# But we can do this as well
my_list.extend(["h", "i", "j"])
print(f"Extend: {my_list}\n")

# If we try to do this
my_list.append(["h", "i", "j"])
# Now you see the difference
print(f"Append as extend: {my_list}\n")

# Index - search if an element exists in the list and return its index
# index = my_list.index("z") # You'll get an error!
# Do this instead:
if "z" in my_list:
    print(f"Index of z: {my_list.index("z")}\n")
else:
    print(f"There is no \"z\" in my list\n")

# Insert - ADD at a CERTAIN INDEX
my_list.insert(9, "a")
print(f"Insert at position 9: {my_list}")
print(f"Let's search for \"a\" now with Index: {my_list.index("a")}")

# But I wanna see the index for my other a
print(f"Let's search for the other \"a\" now with Index: {my_list.index("a", 1)}\n")

# Pop - remove last element on the list or at index and returns it
print(f"Before pop: {my_list}")
my_list.pop()
print(f"After pop: {my_list}")
my_list.pop(1)
print(f"Pop at index 1: {my_list}")
# Del - similar to pop but can remove a few at once and DOESN'T return the removed item(s)
del my_list[-1]
print(f"Del last item: {my_list}")
del my_list[6:8] # Removing MORE THAN one item at once
print(f"Del my_list[6:8]: {my_list}\n")

# Copy
new_list = my_list.copy()
print(f"Copy to new_list: {new_list}\n")

# Count - the number of times an item appears in the list
print(f"Count z: {my_list.count("z")}")
print(f"Count a: {my_list.count("a")}\n")

# Reverse - invert the list
my_list.reverse()
print(f"Reverse: {my_list}")
print(f"Just for reference - the other list: {new_list}\n")

# Sort
my_list.sort()
print(f"Sort: {my_list}\n")

# Remove - delete an item from the list
my_list.remove("a")
print(f"remove(a): {my_list}\n")

# Let's do some basic operations:
print(f"len: {len(my_list)}")
print(f"max: {max(my_list)}")
print(f"min: {min(my_list)}")
# print(f"sum: {sum(my_list)}\n") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(f"sum: {sum([1,2,3,4,5,6,7,8,9,10])}\n")

# Clear - remove all items
my_list.clear()
print(f"Clear: {my_list}\n")

# Getting back to "del", we can remove the variable
del my_list
# print(my_list)
# NameError: name 'my_list' is not defined

##############################
# Now, let's go with different ways to create lists #
##############################

## List Comprehension
# We can create lists as easily as this
# [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}\n")

# Not just of simple things, we can do conditions
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}\n")

# Initialize tuples
tuples = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# tuples = [x, y for x in [1,2,3] for y in [3,1,4] if x != y]
# SyntaxError: did you forget parentheses around the comprehension target?
print(f"Tuples: {tuples}\n")

# Initialize a series of sets
sets = [set() for _ in range(9)]
print(f"List of sets: {sets}\n")

# Other operations
fruit_list = ['  banana', '  loganberry ', 'passion fruit  ']
clean_list = [fruit.strip() for fruit in fruit_list]
print(f"Clean list: {clean_list}")
