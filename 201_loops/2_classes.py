class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y


def print_point(point: Point = Point(0,0)):
    """
    def print_point(point: tuple = (0,0)): # What would happen if we do this instead of the line 7?
    
    The result would be "Not a point".

    Why?
    """
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

def cheese_shop(kind, *arguments, **keywords):
    """
    call with arguments unpacked from a list,
    *packed_arguments = unpacked arguments.
    
    And we also have a dictionary in the call,
    dictionaries can deliver keyword arguments with the **-operator
    """

    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# Lambda function:
def make_incrementor(n: int) -> int:
    print(f"make_incrementor > n: {n}")
    return lambda x: x + n

test_coordinate = 56789

Point(1, test_coordinate)
Point(x=1, y=test_coordinate)
Point(y=1, x=test_coordinate)

# Point(y=1, test_coordinate) # Positional argument cannot appear after keyword
# arguments ?? Is it because "y" is first?
# Point(x=1, test_coordinate) # Positional argument cannot appear after keyword
# arguments. But here "x" is first.
# Basically, a non-keyword argument cannot be after a keyword argument

Point(test_coordinate, y=1)

print_point()

print(" ----- " * 10)
print(" ----- " * 10)
print()

cheese_shop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Plain",
           client="John Cheese",
           sketch="Cheese Shop Sketch")

print(" ----- " * 10)

example_dictionary = {"voltage": "four million", "state": "bleeding demised",
                      "action": "VROOM"}
cheese_shop("Gouda", "It's good", "Truly good", **example_dictionary)

print(" ----- " * 10)
print(" ----- " * 10)
print()

print(f"result 1: {make_incrementor(100)}")
f = make_incrementor(100)

print(f"Result 2: {f(1)}")
print(f"Result 3: {f(2)}")
