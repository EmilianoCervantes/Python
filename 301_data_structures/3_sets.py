# WON'T CONTAIN duplicate values
basket_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"Set result: {basket_set}\n")
# Can print in any order
# Print result 1: {'pear', 'banana', 'orange', 'apple'}
# Print result 2: {'pear', 'apple', 'orange', 'banana'}
# Print result 3: {'banana', 'orange', 'apple', 'pear'}
# Print result 4: {'orange', 'banana', 'apple', 'pear'}

abracadabra_set = set('abracadabra')
print(f"Abracadabra Set: {abracadabra_set}")
alabama_set = set('alabama')
print(f"alabama Set: {alabama_set}\n")
print(f"Letters from abracadabra - alabama = {abracadabra_set - alabama_set}")
print(f"Letters in abracadabra OR alabama = {abracadabra_set | alabama_set}")
print(f"Letters in abracadabra AND alabama = {abracadabra_set & alabama_set}")
print(f"Letters in abracadabra or alabama but NOT both = {abracadabra_set ^ alabama_set}\n")

# Set comprehension
# Similar to list comprehensions
# {expression for item in iterable if condition}
set_comprehension = {letter for letter in 'abracadabra' if letter not in 'alabama'}
print(f"Set comprehension: {set_comprehension}")
