my_first_python_list = [1, 2, 3, 4, 5]

print("my_first_python_list:", my_first_python_list)
print("my_first_python_list[1]:", my_first_python_list[1])
print("my_first_python_list[-1]:", my_first_python_list[-1])

new_list = my_first_python_list[-3:] # This is called making a slice and in python, and performing it returns a slice.
print("new_list = my_first_python_list[-3:]:", new_list)

big_list = my_first_python_list + [36, 49, 64, 81, 100]
print("big_list:", big_list)

print(" ----- ")
print(" ----- ")
print(" ----- ")

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print("cubes before:", cubes)
print("ID cubes:", id(cubes))

# the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print("cubes after:", cubes)
print("ID cubes:", id(cubes)) # It won't change - memory address
print(" ----- ")
cubes.append(216)
cubes_duplicate1 = cubes
cubes_duplicate2 = cubes[:]
print("cubes_duplicate1 = cubes:", cubes_duplicate1)
print("cubes_duplicate2 = cubes[:]:", cubes_duplicate2)
print("id(cubes)", id(cubes))
print("id(cubes_duplicate1)", id(cubes_duplicate1))
print("id(cubes_duplicate2)", id(cubes_duplicate2))
print("id(cubes) == id(cubes_duplicate1)", id(cubes) == id(cubes_duplicate1))
print("id(cubes) == id(cubes_duplicate2)", id(cubes) == id(cubes_duplicate2))

print(" ----- ")
print(" ----- ")
print(" ----- ")

cubes[2:5] = [3, 4, 5]
print("cubes[2:5] = [3, 4, 5] -> cubes_duplicate1:", cubes_duplicate1)
cubes[3:5] = [64.4, 125.5, 216.6, 343.7, 512.8]
print(cubes_duplicate1)
cubes[:] = []
print("cubes[:] = []", cubes_duplicate1)
print("len(cubes_duplicate1)", len(cubes_duplicate1))
