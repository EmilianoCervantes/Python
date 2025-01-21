import sys

def fibonacci(target: int) -> int:
  a,b,res = 0,1,0

  for i in range(target):
    print(f"Fibonacci element #{i+1}:", a)
    a,b = b, a+b
    i+=1

  return res

target = sys.argv[1]
fibonacci(int(target))
