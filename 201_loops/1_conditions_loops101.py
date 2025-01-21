def functionWhereIllAddEverythingBelow():
    pass # TODO: work on this
    # pass is used to create empty blocks
    # https://docs.python.org/3/tutorial/controlflow.html#pass-statements

def print_point(point: tuple) -> None:
  # point is an (x, y) tuple
  match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

userInput = input("Give me a number from 1 to 10: ").strip() # Try sending nothing
inputNumber = int(float(userInput or 0))

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number == inputNumber:
        print("Found", number)
        break
    elif number > inputNumber:
        print("You'll never find it")
        break
    else:
        print("Not found yet, currently on:", number)

        if number % 2 == 0:
            print("Which is an even number")
            continue
        print("Which is odd")

print(" ----- ")
print(" ----- ")

for i in range(6): # range(n) - will go from 0 to n-1. This one will go from 0 to 5.
    match i:
        case 0:
            print("Z.E.R.O")
        case 1:
            print("READY")
        case 2:
            print("SET")
        case 3:
            print("GO!")
        case 4 | 5:
            print(i)

print(" ----- ")
print(" ----- ")
print(" ----- ")

list1 = list(range(5,10))
list2 = list(range(0, 30, 3))
list3 = list(range(0, 31, 3))
list4 = list(range(-10, -100, -15))

print("list(range(5,10)):", list1)
print("list(range(0, 30, 3)):", list2)
print("list(range(0, 31, 3)):", list3)
print("list(range(-10, -100, -15)):", list4)

print(" ----- ")
print(" ----- ")
print(" ----- ")

pets = ["dog", "cat", "bird", "fish"]

for i in range(len(pets)):
    print(f"Pet #{i+1} is a {pets[i]}")

functionWhereIllAddEverythingBelow()

print(" ----- ")
print(" ----- ")
print(" ----- ")

print_point((0,0))
print_point((0,1))
print_point((1,0))
print_point((1,1))
# print_point(None) # raise ValueError("Not a point") - ValueError: Not a point
