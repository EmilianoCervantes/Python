# This is a simple comment
my_first_variable = 1 # This is a comment about my first variable
print(my_first_variable)
print("type(1):", type(1))
some_text = "# This is NOT a comment, this is a string. You can tell from the double quotes"
print("Some text:", some_text)
print("type(some_text)", type(some_text))
another_text = 'We can also do single quotes. No biggie. Just be consistent.'
print("Another text:", another_text)
print("type(another_text)", type(another_text))
num_as_string = "101"
print("Number as string:", num_as_string)
print("type(101):", type(num_as_string))
print(" ----- ")
print(" ----- ")
print(" ----- ")

math101 = 1 + 1
print("math101: 1 + 1 =", math101)
print("type(math101):", type(math101))
print(" ----- ")
a_more_complex_operation = 50 - 5 * 6
print("a_more_complex_operation: 50 - 5 * 6 =", a_more_complex_operation)
print("type(a_more_complex_operation):", type(a_more_complex_operation))
print(" ----- ")
is_this_a_float = a_more_complex_operation / 4
print("is_this_a_float: (50 - 5 * 6) / 4 =", is_this_a_float)
print("type(is_this_a_float):", type(is_this_a_float))
print(" ----- ")
another_float = 8 / 5
print("another_float: 8 / 5 =", another_float)
print("type(another_float):", type(another_float))
print(" ----- ")
print(" ----- ")
floor_division = 8 // 5
print("floor_division: 8 // 5 =", floor_division)
print("type(floor_division):", type(floor_division))
print(" ----- ")
reminder = 8 % 5
print("reminder: 8 % 5 =", reminder)
print("type(reminder):", type(reminder))
print(" ----- ")
print(" ----- ")
to_the_power_of_2 = 5 ** 2
print("to_the_power_of_2: 5 ** 2 =", to_the_power_of_2)
print("type(to_the_power_of_2):", type(to_the_power_of_2))
print(" ----- ")
to_the_power_of_10 = 2 ** 10
print("to_the_power_of_10: 2 ** 10 =", to_the_power_of_10)
print("type(to_the_power_of_10):", type(to_the_power_of_10))
print(" ----- ")
print(" ----- ")
tax = 12.5 / 1000
price = 101.433
final_price = price * tax
print("final price: 101.433 * 12.5 / 1000 =", final_price)
print("rounded price: round(final_price, 4) =", round(final_price, 4))
print("rounded price: round(final_price, 3) =", round(final_price, 3))
print("rounded price: round(final_price, 2) =", round(final_price, 2))
print(" ----- ")
print(" ----- ")
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(f"Using 'or' to get a non-empty string: {non_null}")
