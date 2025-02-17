# Usually you'll call a function
# Having the file path as a variable is a good practice.
FILE_PATH = "access.log"

# with helps properly managing the resources of opening a file
# Python will automatically close the file for us
with open(FILE_PATH) as file:
    content = file.read()
    print(f"File content:\n{content}")
    print("--- End of file ---\n")

# In with open(FILE_PATH, <method>) as file:
# There are several methods
# r is the default with t (text) being the default encoding mode.
# with open(FILE_PATH, "w") as file: # "w" for write only
#     """
#     "w" will override everything when opening!!
#     "w" and "w+" ARE NOT RECOMMENDED - unless you don't care about the content
#     And yes, it can happen that you don't care:
#     - Debug logs,
#     - No need to keep track,
#     - Just creating the file.
#     """
#     file.write("!")
#     pass

# with open(FILE_PATH, <method>, <encoding>) as file:
# The default encoding is UTF-8.
with open(FILE_PATH, "a", encoding="utf-8") as file: # "a" for appending only
    file.write("!") # Adds at the end of the file


# Let's dig deeper
with open(FILE_PATH, "r+", encoding="utf-8") as file:
    for line in file:
        print(f"Line: {line}\n")
    
    line = file.readline()
    print(f"One line: {line}\n") # What will this print?
    # Spoiler: nothing

    # Return to the beginning of the file
    file.seek(0)
    # Let's try again
    print(f"One line: {file.readline()}") # What will this print?
    print(f"Another line: {file.readline()}") # What will this print?
    file.write("\nThis is the 3rd LINE! Or is it?\n")

    file.seek(35)
    file.write("This is the 3rd LINE! Or is it?") # Writes and replaces

##############################
# Saving as JSON #
##############################

import json

a_list = [1,2,3,4]
my_json = json.dumps(a_list) # Serialize to a String
print(f"My JSON: {my_json}")
print(f"Type of my JSON: {type(my_json)}")

with open("json_file.json", "w", encoding="utf-8") as json_file:
    # json.dump(a_list, "json_file.json") # AttributeError: 'str' object has no attribute 'write
    # That's why remember to open the file first
    json.dump(a_list, json_file) # Serialize to a File