def factorial_iterative(n):
  if(n < 0):
    return -1
  if(n == 0):
    return 1
  else:
    factorial = 1
    for i in range(1,n+1):
      factorial = factorial * i
    return factorial


print(factorial_iterative(-1))
print(1 == factorial_iterative(0))
print(1 == factorial_iterative(1))
print(2 == factorial_iterative(2))
print(6 == factorial_iterative(3))
print(24 == factorial_iterative(4))
print(120 == factorial_iterative(5))
print(720 == factorial_iterative(6))
print(5040 == factorial_iterative(7))
print(40320 == factorial_iterative(8))
print(362880 == factorial_iterative(9))

print(6227020800 == factorial_iterative(13))
