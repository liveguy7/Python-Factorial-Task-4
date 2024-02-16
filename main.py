# 5!

def factorialRecursion(value):
  if(value <= 1): # bas case
    return 1
  else:
    return value * factorialRecursion(value - 1)

n = factorialRecursion(5)

print("5! is {0}".format(n))


