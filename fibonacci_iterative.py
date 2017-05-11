def fibonacci_iterative(index):
  if(index<0):
    return -1
  if(index == 0):
    return 0
  elif(index ==1):
    return 1
  else:
    prevprev = 0
    prev = 1
    fibonacci_sum = 0
    for i in range(1,index-1):
      fibonacci_sum = prevprev + prev
      prevprev = prev
      prev = fibonacci_sum
    return fibonacci_sum

print(fibonacci_iterative(-1))
print(0 == fibonacci_iterative(0))
print(1 == fibonacci_iterative(1))
print(1 == fibonacci_iterative(2))
print(2 == fibonacci_iterative(3))
print(3 == fibonacci_iterative(4))
print(5 == fibonacci_iterative(5))
print(8 == fibonacci_iterative(6))
print(13 == fibonacci_iterative(7))
print(21 == fibonacci_iterative(8))
print(34 == fibonacci_iterative(9))
