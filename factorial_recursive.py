def factorial_recurrent(n):
  if(n < 0):
    return -1
  if(n == 0):
    return 1
  else:
    factorial = n * factorial_recurrent(n-1)
    return factorial


print(factorial_recurrent(-1))
print(1 == factorial_recurrent(0))
print(1 == factorial_recurrent(1))
print(2 == factorial_recurrent(2))
print(6 == factorial_recurrent(3))
print(24 == factorial_recurrent(4))
print(120 == factorial_recurrent(5))
print(720 == factorial_recurrent(6))
print(5040 == factorial_recurrent(7))
print(40320 == factorial_recurrent(8))
print(362880 == factorial_recurrent(9))

print(6227020800 == factorial_recurrent(13))
