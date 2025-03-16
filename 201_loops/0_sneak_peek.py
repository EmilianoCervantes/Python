import sys


def fibonacci(target: int) -> int:
    a, b = 0, 1

    for i in range(target):
        print(f"Fibonacci {i}th element:", a)
        a, b = b, a+b

    return a


# target = sys.argv[1]
# print(f"Iterative res: {fibonacci(int(0))}")
# print(f"Iterative res: {fibonacci(0)}")
# print(f"Iterative res: {fibonacci(1)}")
# print(f"Iterative res: {fibonacci(2)}")
# print(f"Iterative res: {fibonacci(5)}")
# print(f"Iterative res: {fibonacci(6)}")
print(f"Iterative res - Fibonacci {10}th element: {fibonacci(10)}")


def fibonacciRecursive(target: int, counter=0, first=0, second=1) -> int:
    if counter == target:
        return first

    print(f"Fibonacci {counter}th element:", first)
    return fibonacciRecursive(target, counter+1, second, first+second)


# print(f"Recursive res: {fibonacciRecursive(0)}")
# print(f"Recursive res: {fibonacciRecursive(1)}")
# print(f"Recursive res: {fibonacciRecursive(2)}")
# print(f"Recursive res: {fibonacciRecursive(5)}")
# print(f"Recursive res: {fibonacciRecursive(6)}")
print(f"Recursive res - Fibonacci {10}th element: {fibonacciRecursive(10)}")
