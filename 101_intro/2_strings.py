single_quote_inside_single_quotes = 'doesn\'t'  # use \' to escape the single quote...

single_quote_inside_double_quotes = "doesn't"  # ...or use double quotes instead

double_quotes_inside_single_quotes = '"Yes," they said.'

double_quotes_inside_double_quotes = "\"Yes,\" they said."

double_plus_single_quotes_inside_quotes = '"Isn\'t," they said.'

print("single_quote_inside_single_quotes: ", single_quote_inside_single_quotes)
print("single_quote_inside_double_quotes: ", single_quote_inside_double_quotes)
print("double_quotes_inside_single_quotes: ", double_quotes_inside_single_quotes)
print("double_quotes_inside_double_quotes: ", double_quotes_inside_double_quotes)
print("double_plus_single_quotes_inside_quotes: ", double_plus_single_quotes_inside_quotes)
print(" ----- ")
print(" ----- ")
print(" ----- ")

print("One Line.\nLine after skip character.") # \n means newline
lets_do_a_tab = "My\tname"
print(lets_do_a_tab)

ignore_all_these = r"Line One.\nLine\tTwo"
print(ignore_all_these)

multi_line_text = """
In Python
we can do multiple lines
by using three consecutive double quotes (")
""" # This adds an extra new line at the end
print(multi_line_text)

ignore_first_line = """\
Line One
Line Two
Last Line """

print(ignore_first_line)
print("Test")
print(multi_line_text+ignore_first_line)

print(
  ('Put several strings within parentheses '
  'to have them joined together.')
)
print(" ----- ")
print(" ----- ")

text = "Learning Python"
print(text)
print("type(text[0]):", type(text[0])) # Different from other *languages*, one character is of type string.
print("text[0]:", text[0])
print("text[14]:", text[14])
print("text[-1]:", text[-1])
print("text[-2]:", text[-2])
print("text[-14]:", text[-14])
print("text[-15]:", text[-15])
print("text[0:2]:", text[0:2]) # [inclusive, exclusive]
print("text[0:-1]:", text[0:-1]) # [inclusive, exclusive]
print("text[3:]:", text[3:]) # [inclusive:] till the end
print("text[-2:]:", text[-2:]) # [inclusive:] till the end
print("text[-5:]:", text[-5:]) # [inclusive:] till the end
print("text[:2] + text[2:]:", text[:2] + text[2:])
print("text[5:100000]", text[5:100000]) # [start:out of bounds index] - in Python it doesn't matter
print("text[100000:]", text[100000:]) # [out of bounds index:] - because we are out of bounds, it won't return anything
print("type(text[100000:])", type(text[100000:]))

# text[0] = "Still Learning" # TypeError: 'str' object does not support item assignment

print("len(text):", len(text))