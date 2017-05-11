def fibonacci_recursive(index):
  if(index<0):
    return -1
  if(index == 0):
    return 0
  elif(index ==1):
    return 1
  else:
    return (fibonacci_recursive(index-1) + fibonacci_recursive(index-2))

print(fibonacci_recursive(-1))
print(0 == fibonacci_recursive(0))
print(1 == fibonacci_recursive(1))
print(1 == fibonacci_recursive(2))
print(2 == fibonacci_recursive(3))
print(3 == fibonacci_recursive(4))
print(5 == fibonacci_recursive(5))
print(8 == fibonacci_recursive(6))
print(13 == fibonacci_recursive(7))
print(21 == fibonacci_recursive(8))
print(34 == fibonacci_recursive(9))
